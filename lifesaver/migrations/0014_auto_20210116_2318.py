# Generated by Django 3.1.5 on 2021-01-16 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lifesaver', '0013_remove_nurse_work_shift'),
    ]

    operations = [
        migrations.AddField(
            model_name='nurse',
            name='work_shift',
            field=models.OneToOneField(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='lifesaver.workshift'),
        ),
        migrations.AlterField(
            model_name='nurse',
            name='reports_to',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='lifesaver.doctor'),
        ),
    ]
