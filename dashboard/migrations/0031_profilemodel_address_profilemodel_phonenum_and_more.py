# Generated by Django 4.1.1 on 2023-02-10 14:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0030_alter_predictiondata_dpf'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='phoneNum',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='avatar',
            field=models.ImageField(default='', upload_to='profile', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg'])]),
        ),
    ]
