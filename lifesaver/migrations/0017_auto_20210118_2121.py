# Generated by Django 3.1.5 on 2021-01-18 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lifesaver', '0016_auto_20210116_2324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nurse',
            old_name='department',
            new_name='sector',
        ),
    ]
