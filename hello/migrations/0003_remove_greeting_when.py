# Generated by Django 2.2.2 on 2019-06-21 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_auto_20190621_1958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='greeting',
            name='when',
        ),
    ]
