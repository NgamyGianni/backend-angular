# Generated by Django 3.2.8 on 2022-01-20 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0003_alter_sale_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='date',
            field=models.DateField(default='2022-01-20'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='name',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='sale',
            name='owner',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='sale',
            name='price',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=1000),
        ),
    ]
