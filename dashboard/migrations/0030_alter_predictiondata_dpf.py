# Generated by Django 4.1.1 on 2023-02-08 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0029_alter_predictiondata_dpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictiondata',
            name='dpf',
            field=models.FloatField(default=0),
        ),
    ]
