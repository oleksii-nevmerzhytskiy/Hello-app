# Generated by Django 4.0.1 on 2022-01-18 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greeting', '0002_alter_contactmodel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
