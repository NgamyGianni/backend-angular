# Generated by Django 4.0.1 on 2022-01-20 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0003_alter_purchase_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='date',
            field=models.DateField(default='2022-01-20 15:55:15.947965'),
        ),
    ]