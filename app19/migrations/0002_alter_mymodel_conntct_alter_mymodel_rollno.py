# Generated by Django 4.2.2 on 2023-06-19 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app19', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='Conntct',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='Rollno',
            field=models.BigIntegerField(),
        ),
    ]
