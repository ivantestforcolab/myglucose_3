# Generated by Django 4.1.1 on 2023-02-11 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0040_rename_age_profilemodel_profileage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='', max_length=100),
        ),
    ]
