# Generated by Django 4.1.1 on 2023-02-11 03:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0039_alter_profilemodel_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilemodel',
            old_name='age',
            new_name='profileAge',
        ),
    ]
