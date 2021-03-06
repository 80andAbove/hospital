# Generated by Django 3.1.5 on 2021-01-16 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lifesaver', '0014_auto_20210116_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nurse',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lifesaver.department'),
        ),
        migrations.AlterField(
            model_name='nurse',
            name='reports_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lifesaver.doctor'),
        ),
    ]
