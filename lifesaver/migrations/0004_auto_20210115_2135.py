# Generated by Django 3.1.1 on 2021-01-15 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lifesaver', '0003_auto_20210115_2133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nurse',
            old_name='boss',
            new_name='reports_to',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='email',
        ),
    ]
