# Generated by Django 3.1.2 on 2021-05-31 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0002_auto_20210531_1707'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='gender',
            new_name='rating',
        ),
    ]
