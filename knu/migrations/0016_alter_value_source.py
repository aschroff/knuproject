# Generated by Django 3.2.15 on 2022-10-24 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knu', '0015_alter_fact_fact_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='value',
            name='source',
            field=models.CharField(default='', max_length=201),
        ),
    ]
