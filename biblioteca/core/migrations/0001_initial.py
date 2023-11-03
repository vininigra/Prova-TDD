# Generated by Django 4.2.6 on 2023-10-16 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LivroModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('editora', models.CharField(max_length=200, verbose_name='editora')),
                ('autor',   models.CharField(max_length=200, verbose_name='autor')),
                ('isbn',    models.CharField(max_length=13,  verbose_name='isbn')),
                ('paginas', models.CharField(max_length=3,   verbose_name='paginas')),
                ('ano',     models.CharField(max_length=4,   verbose_name='ano')),
            ],
        ),
    ]
