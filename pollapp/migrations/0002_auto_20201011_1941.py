# Generated by Django 3.1.2 on 2020-10-11 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='vote_count',
            field=models.IntegerField(default=0),
        ),
    ]
