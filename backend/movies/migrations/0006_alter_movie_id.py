# Generated by Django 3.2.9 on 2021-11-21 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_alter_movie_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
