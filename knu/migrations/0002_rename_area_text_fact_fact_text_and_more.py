# Generated by Django 4.1 on 2022-09-02 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knu', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fact',
            old_name='area_text',
            new_name='fact_text',
        ),
        migrations.RemoveField(
            model_name='value',
            name='description',
        ),
        migrations.AddField(
            model_name='value',
            name='source',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='value',
            name='unit',
            field=models.CharField(default='', max_length=20),
        ),
    ]
