# Generated by Django 3.2.4 on 2021-06-24 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('band', models.CharField(max_length=50)),
            ],
        ),
    ]
