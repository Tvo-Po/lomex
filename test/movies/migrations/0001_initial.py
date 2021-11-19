# Generated by Django 3.2.9 on 2021-11-18 01:59

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('imdb_rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('description', models.TextField()),
                ('actors', models.ManyToManyField(related_name='movies', to='movies.Actor')),
                ('director', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.director')),
                ('genres', models.ManyToManyField(related_name='movies', to='movies.Genre')),
                ('writers', models.ManyToManyField(related_name='movies', to='movies.Writer')),
            ],
        ),
    ]
