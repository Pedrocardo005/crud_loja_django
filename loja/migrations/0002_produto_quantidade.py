# Generated by Django 3.2.6 on 2021-10-03 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='quantidade',
            field=models.IntegerField(null=True),
        ),
    ]
