# Generated by Django 3.1.1 on 2021-01-15 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lifesaver', '0007_auto_20210115_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nurse',
            name='workshift',
        ),
    ]
