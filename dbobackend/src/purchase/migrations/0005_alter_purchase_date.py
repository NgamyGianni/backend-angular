# Generated by Django 3.2.8 on 2022-01-20 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0004_alter_purchase_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='date',
            field=models.DateField(default='2022-01-20 13:53:16.219868'),
        ),
    ]
