# Generated by Django 3.0.7 on 2020-06-15 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200615_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
