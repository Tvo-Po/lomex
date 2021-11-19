import os 
import django 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configuration.settings')
django.setup()


#------------------------------------------------------------------#


import sqlite3
from json import loads as structurize

from movies.models import Actor, Writer, Director, Genre, Movie


def process_name(full_name: str) -> tuple:
    full_name = full_name.split()
    if len(full_name) < 2:
        raise ValueError(
            'Full name must contain at least first name and last_name'
        )
    first_name = full_name[0]
    middle_name = full_name[1:-1]
    last_name = full_name[-1]
    if not middle_name:
        middle_name = ''
    else:
        middle_name = middle_name[0]
    return first_name, middle_name, last_name


def process_uuid(raw_uuid: str) -> str:
    raw_uuid = raw_uuid.removeprefix('0b60f2f3')
    if len(raw_uuid) != 32:
        raise ValueError(
            'Raw UUID must be 32 symbols lenght'
        )
    uuid = '{}-{}-{}-{}-{}'.format(
        raw_uuid[:8],
        raw_uuid[8:12],
        raw_uuid[12:16],
        raw_uuid[16:20],
        raw_uuid[20:]
    )
    return uuid


def process_genre(genres: str) -> dict:
    genres = [genre.rstrip(',') for genre in genres.split()]
    genres = {
        'm2m': [Genre.objects.get_or_create(name=genre)[0] for genre in genres]
    }
    return genres


def process_director(director: str):
    if director == 'N/A':
        return None
    else:
        names = process_name(director)
        return Director.objects.get_or_create(
            first_name=names[0],
            middle_name=names[1],
            last_name=names[2],
        )[0]


def process_writers(writers):
    if not writers:
        return None
    m2m_writers = []
    if writers[0] == '[':
        struct_writers = structurize(writers)
        for writer in struct_writers:
            m2m_writers.append(
                Writer.objects.get(
                    id=process_uuid(writer['id'])
                )
            )
    else:
        m2m_writers.append(
            Writer.objects.get(
                id=process_uuid(writers)
            )
        )
    writers = {'m2m': m2m_writers}
    return writers


class ExtractTableData:
    
    DB_NAME = 'db.sqlite'
    
    def __init__(self, table_name: str):
        self.__table_name = table_name
        self.__raw_data = []
        self._extract_data()
    
    def __iter__(self):
        for a in self.__raw_data:
            yield a    
    
    def change_table(self, table_name: str):
        self.__table_name = table_name
        self._extract_data()
    
    def _extract_data(self):
        with sqlite3.connect(self.DB_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute(f'SELECT * FROM {self.__table_name};')
            self.__raw_data = cursor.fetchall()
    
    @property
    def raw_data(self):
        return self.__raw_data


class CleanDataFromTableRow:
    
    __field_procesors = {
        'name': process_name,
        'uuid': process_uuid,
        'genre': process_genre,
        'director': process_director,
        'writers': process_writers,
    }
    
    def __init__(self, *fields: dict):
        self.__fields = fields
        self.__cleaned_fields = []
        self._clean_fields()
    
    def _clean_fields(self):
        for field in self.__fields:
            process_function = self.__field_procesors.get(
                field['type']
            )
            if field['type'] == 'redudant':
                continue
            if not process_function:
                self.__cleaned_fields.append(
                    field['value']
                )
                continue
            cleaned_field = process_function(
                field['value']
            )
            if isinstance(cleaned_field, tuple):
                self.__cleaned_fields.extend(
                    cleaned_field
                )
            else:
                self.__cleaned_fields.append(
                    cleaned_field
                )
    
    @property
    def data(self) -> list:
        return self.__cleaned_fields


class LoadDataToDjangoDataBase:
    
    def __init__(self):
        self.__instance_data = {}
        self.__many_to_many_data = {}
    
    def create_instance(self, cleaned_row, fields, model):
        for j in range(len(fields)):
            if (cleaned_row[j] is None or
                cleaned_row[j] == '' or
                cleaned_row[j] == []):
                continue
            if isinstance(cleaned_row[j], dict) and cleaned_row[j].get('m2m'):
                self.__many_to_many_data[fields[j]] = cleaned_row[j]['m2m']
                continue
            self.__instance_data[fields[j]] = cleaned_row[j]
        instance = model.objects.create(
            **self.__instance_data
        )
        for field_name in self.__many_to_many_data:
            set_field = getattr(instance, field_name)
            set_field.add(*self.__many_to_many_data[field_name])
            instance.save()
        self.__instance_data = {}
        self.__many_to_many_data = {}


if __name__ == '__main__':
    
    EXPORT_DB = {
        'actors': [
            {'field_type': 'simple_id'},
            {'field_type': 'name'},
        ],
        'writers': [
            {'field_type': 'uuid'},
            {'field_type': 'name'},
        ],
        'movies': [
            {'field_type': 'movie_id'},
            {'field_type': 'genre'},
            {'field_type': 'director'},
            {'field_type': 'writers'},
            {'field_type': 'title'},
            {'field_type': 'text'},
            {'field_type': 'redudant'},
            {'field_type': 'decimal'},
            {'field_type': 'writers'},
        ],
    }
    
    IMPORT_DB = [
        {
            'name': Actor,
            'fields': [
                'id',
                'first_name',
                'middle_name',
                'last_name',
            ]
        },
        {
            'name': Writer,
            'fields': [
                'id',
                'first_name',
                'middle_name',
                'last_name',
            ]
        },
        {
            'name': Movie,
            'fields': [
                'id',
                'genres',
                'director',
                'writers',
                'title',
                'description',
                'imdb_rating',
                'writers',
            ]
        }
    ]
    
    for i, table in enumerate(EXPORT_DB):
        for row in ExtractTableData(table):
            try:
                row_properties = []
                for j in range(len(EXPORT_DB[table])):
                    row_properties.append({
                        'type': EXPORT_DB[table][j]['field_type'],
                        'value': row[j],
                    })
                row_cleaner = CleanDataFromTableRow(
                    *row_properties
                )
                cleaned_row = row_cleaner.data
                db_load = LoadDataToDjangoDataBase()
                db_load.create_instance(
                    cleaned_row, IMPORT_DB[i]['fields'],
                    IMPORT_DB[i]['name']
                )
            except Exception as E:
               print(E)

        print(f'[Table {table}] ... extracted!')   
            
    for row in ExtractTableData('movie_actors'):
        try:
            movie = Movie.objects.get(id=row[0])
            actor = Actor.objects.get(id=row[1])
            movie.actors.add(actor)
            movie.save()
        except Exception as E:
            print(E)

    print(f'[Table movie_actors] ... extracted!')