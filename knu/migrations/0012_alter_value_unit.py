# Generated by Django 3.2.15 on 2022-10-23 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('knu', '0011_alter_impact_scenario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='value',
            name='unit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='knu.unit'),
            preserve_default=False,
        ),
    ]