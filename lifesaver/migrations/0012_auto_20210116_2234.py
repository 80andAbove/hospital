# Generated by Django 3.1.1 on 2021-01-16 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lifesaver', '0011_auto_20210116_2230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nurse',
            name='end_datetime',
        ),
        migrations.RemoveField(
            model_name='nurse',
            name='start_datetime',
        ),
        migrations.AddField(
            model_name='nurse',
            name='work_shift',
            field=models.OneToOneField(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='lifesaver.workshift'),
        ),
    ]