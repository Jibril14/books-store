# Generated by Django 3.1.7 on 2019-12-11 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(help_text='Enter the book genre(e.g Drama, Fiction)', max_length=200),
        ),
    ]
