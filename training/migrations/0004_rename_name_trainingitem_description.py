# Generated by Django 3.2.11 on 2022-01-30 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0003_trainingcategory_training_level'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trainingitem',
            old_name='name',
            new_name='description',
        ),
    ]
