# Generated by Django 2.0 on 2018-09-20 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0002_auto_20180920_0134'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='moview_details',
            options={'verbose_name': 'Movie', 'verbose_name_plural': 'Movies'},
        ),
    ]
