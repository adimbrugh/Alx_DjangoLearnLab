# Generated by Django 5.1.2 on 2024-11-27 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publication_year',
            field=models.IntegerField(),
        ),
    ]
