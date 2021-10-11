# Generated by Django 3.2 on 2021-10-11 20:18

from django.db import migrations, models
import utils.validators.car
import utils.validators.tyre


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0007_auto_20211011_0246'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tyremodel',
            options={'ordering': ('-in_use',), 'verbose_name': 'Tyre', 'verbose_name_plural': 'Tyres'},
        ),
        migrations.RemoveField(
            model_name='carmodel',
            name='description',
        ),
        migrations.RemoveField(
            model_name='carmodel',
            name='manufacturer',
        ),
        migrations.RemoveField(
            model_name='carmodel',
            name='price',
        ),
        migrations.RemoveField(
            model_name='carmodel',
            name='year',
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='gas_count',
            field=models.FloatField(default=100, validators=[utils.validators.car.MinGasCountValidator(0), utils.validators.car.MaxGasCountValidator(100)]),
        ),
        migrations.AlterField(
            model_name='tyremodel',
            name='degradation',
            field=models.FloatField(default=0, validators=[utils.validators.tyre.MaxDegradationValidator(100)]),
        ),
    ]
