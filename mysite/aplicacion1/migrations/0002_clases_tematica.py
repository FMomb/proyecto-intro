# Generated by Django 4.2.5 on 2023-10-26 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clases',
            name='tematica',
            field=models.TextField(null=True),
        ),
    ]
