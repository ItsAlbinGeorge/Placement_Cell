# Generated by Django 5.0.4 on 2024-07-16 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0002_alter_candidate_c_passoutyear'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='c_Marklist',
            field=models.FileField(upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='c_Photo',
            field=models.ImageField(upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='c_Resume',
            field=models.FileField(upload_to='pics'),
        ),
    ]
