# Generated by Django 3.1.1 on 2021-01-15 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lifesaver', '0006_workshift_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nurse',
            name='workshift',
            field=models.OneToOneField(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='lifesaver.workshift'),
        ),
    ]