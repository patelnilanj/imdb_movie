# Generated by Django 2.0 on 2018-09-19 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='moview_details',
            fields=[
                ('imdbID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('Title', models.CharField(max_length=250)),
                ('Year', models.IntegerField()),
                ('Genre', models.TextField()),
                ('Ratings', models.CharField(max_length=6)),
                ('Response', models.CharField(max_length=25)),
            ],
        ),
    ]
