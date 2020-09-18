# Generated by Django 3.0.3 on 2020-09-17 03:57

import django.core.validators
from django.db import migrations, models
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200909_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfilePic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, validators=[myapp.models.validate_name])),
                ('image', models.ImageField(upload_to='%Y/%m/%d')),
            ],
        ),
        migrations.RenameModel(
            old_name='AcccessDetails',
            new_name='AccessDetails',
        ),
        migrations.AlterField(
            model_name='topic',
            name='Topic_name',
            field=models.CharField(max_length=30, unique=True, validators=[django.core.validators.MaxLengthValidator(12)]),
        ),
    ]