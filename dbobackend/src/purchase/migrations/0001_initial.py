# Generated by Django 4.0.1 on 2022-01-20 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.IntegerField(default='-1')),
                ('price', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('owner', models.TextField(max_length=100)),
                ('name', models.TextField(max_length=100)),
                ('quantity_sold', models.IntegerField(default='0')),
                ('date', models.DateField(default='2022-01-20 14:58:47.593960')),
            ],
            options={
                'ordering': ('date',),
            },
        ),
    ]
