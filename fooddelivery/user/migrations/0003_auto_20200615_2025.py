# Generated by Django 3.0.7 on 2020-06-15 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200615_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='id',
            field=models.Field(primary_key=True, serialize=False),
        ),
    ]
