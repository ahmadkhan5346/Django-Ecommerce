# Generated by Django 4.0.5 on 2022-07-14 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(default='', max_length=100),
        ),
    ]
