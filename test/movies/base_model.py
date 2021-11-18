from django.db.models import Model, CharField

class PersonModel(Model):
    
    first_name = CharField(max_length=50)
    middle_name = CharField(max_length=50, blank=True)
    last_name = CharField(max_length=50)
    
    class Meta:
        absract = True
    
    def __str__(self):
        if self.middle_name:
            return f'{self.first_name} {self.middle_name[0]}. {self.last_name}'
        else:
            return f'{self.first_name} {self.last_name}'
