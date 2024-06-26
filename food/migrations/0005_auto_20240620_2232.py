# Generated by Django 3.2.16 on 2024-06-20 19:32

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20240529_1624'),
        ('food', '0004_auto_20240620_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='brdishes',
            name='br_child',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='users.children', verbose_name='Ребенок'),
        ),
        migrations.AddField(
            model_name='brdishes',
            name='br_day',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата дня'),
        ),
        migrations.AddField(
            model_name='dindishes',
            name='din_child',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='users.children', verbose_name='Ребенок'),
        ),
        migrations.AddField(
            model_name='dindishes',
            name='din_day',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата'),
        ),
        migrations.AddField(
            model_name='lundishes',
            name='lun_child',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='users.children', verbose_name='Ребенок'),
        ),
        migrations.AddField(
            model_name='lundishes',
            name='lun_day',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата'),
        ),
    ]
