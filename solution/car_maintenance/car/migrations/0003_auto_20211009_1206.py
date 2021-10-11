# Generated by Django 3.2 on 2021-10-09 15:06

from django.db import migrations, models
import utils.validators.validators


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_auto_20211009_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='gas_count',
            field=models.PositiveIntegerField(default=100, validators=[utils.validators.validators.PorcentagemValidator]),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]