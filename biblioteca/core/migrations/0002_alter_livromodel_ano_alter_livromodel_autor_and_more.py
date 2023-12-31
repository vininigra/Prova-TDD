# Generated by Django 4.2.6 on 2023-11-03 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livromodel',
            name='ano',
            field=models.CharField(max_length=4, verbose_name='Ano    '),
        ),
        migrations.AlterField(
            model_name='livromodel',
            name='autor',
            field=models.CharField(max_length=200, verbose_name='Autor  '),
        ),
        migrations.AlterField(
            model_name='livromodel',
            name='editora',
            field=models.CharField(max_length=200, verbose_name='Editora'),
        ),
        migrations.AlterField(
            model_name='livromodel',
            name='isbn',
            field=models.CharField(max_length=13, verbose_name='ISBN   '),
        ),
        migrations.AlterField(
            model_name='livromodel',
            name='paginas',
            field=models.CharField(max_length=3, verbose_name='Páginas'),
        ),
        migrations.AlterField(
            model_name='livromodel',
            name='titulo',
            field=models.CharField(max_length=200, verbose_name='Título '),
        ),
    ]
