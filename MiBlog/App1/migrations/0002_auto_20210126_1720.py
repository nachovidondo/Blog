# Generated by Django 3.1.3 on 2021-01-26 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.CharField(max_length=200, verbose_name='Contenido'),
        ),
    ]
