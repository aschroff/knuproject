# Generated by Django 3.2.15 on 2022-10-23 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('knu', '0009_impact_scenario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='impact',
            name='fact',
        ),
        migrations.AddField(
            model_name='impact',
            name='scenario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='knu.scenario'),
        ),
        migrations.AddField(
            model_name='impact',
            name='value',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='knu.value'),
        ),
        migrations.AlterField(
            model_name='scenario',
            name='inheritance',
            field=models.ManyToManyField(related_name='mothers', to='knu.Scenario'),
        ),
    ]
