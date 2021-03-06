# Generated by Django 3.2.4 on 2021-06-25 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='music',
            options={'verbose_name_plural': 'Musica'},
        ),
        migrations.AlterField(
            model_name='music',
            name='author',
            field=models.CharField(max_length=50, verbose_name='Autor da musica'),
        ),
        migrations.AlterField(
            model_name='music',
            name='band',
            field=models.CharField(max_length=50, verbose_name='Banda'),
        ),
        migrations.AlterField(
            model_name='music',
            name='music',
            field=models.CharField(max_length=50, verbose_name='Nome da musica'),
        ),
    ]
