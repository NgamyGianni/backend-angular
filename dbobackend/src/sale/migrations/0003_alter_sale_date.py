# Generated by Django 3.2.8 on 2022-01-20 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0002_alter_sale_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='date',
            field=models.DateField(default='2022-01-20 12:51:21.674803'),
        ),
    ]