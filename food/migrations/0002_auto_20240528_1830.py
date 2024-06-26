# Generated by Django 3.2.16 on 2024-05-28 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brdishes',
            name='br_addition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='br_addition', to='food.dishes', verbose_name='Дополнительное'),
        ),
        migrations.AlterField(
            model_name='brdishes',
            name='br_drink',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='br_drink', to='food.dishes', verbose_name='Напиток завтрака'),
        ),
        migrations.AlterField(
            model_name='brdishes',
            name='br_main',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='br_main', to='food.dishes', verbose_name='Основное завтрака'),
        ),
        migrations.AlterField(
            model_name='dindishes',
            name='din_addition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='din_addition', to='food.dishes', verbose_name='Дополнительное'),
        ),
        migrations.AlterField(
            model_name='dindishes',
            name='din_drink',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='din_drink', to='food.dishes', verbose_name='Напиток ужина'),
        ),
        migrations.AlterField(
            model_name='dindishes',
            name='din_main',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='din_main', to='food.dishes', verbose_name='Основное ужина'),
        ),
        migrations.AlterField(
            model_name='lundishes',
            name='lun_addition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lun_addition', to='food.dishes', verbose_name='Дополнительное'),
        ),
        migrations.AlterField(
            model_name='lundishes',
            name='lun_drink',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lun_drink', to='food.dishes', verbose_name='Напиток обеда'),
        ),
        migrations.AlterField(
            model_name='lundishes',
            name='lun_first',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lun_first', to='food.dishes', verbose_name='Первое обеда'),
        ),
        migrations.AlterField(
            model_name='lundishes',
            name='lun_second_garnish',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lun_second_garnish', to='food.dishes', verbose_name='Гарнир обеда'),
        ),
        migrations.AlterField(
            model_name='lundishes',
            name='lun_second_main',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lun_second_main', to='food.dishes', verbose_name='Основное обеда'),
        ),
    ]
