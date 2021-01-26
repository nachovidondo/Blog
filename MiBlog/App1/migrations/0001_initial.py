# Generated by Django 3.1.3 on 2021-01-25 21:24

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Contenido')),
                ('image', models.ImageField(upload_to='Blog', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Editado')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
                'ordering': ['-created'],
            },
        ),
    ]
