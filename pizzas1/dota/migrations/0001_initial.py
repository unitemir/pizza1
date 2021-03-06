# Generated by Django 3.2.5 on 2021-07-09 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'dota.restaurants',
            },
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, verbose_name='name')),
                ('cheese', models.CharField(blank=True, max_length=128, verbose_name='cheese')),
                ('pastry', models.CharField(blank=True, max_length=128, verbose_name='pastry')),
                ('secret_ingredient', models.CharField(max_length=128)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dota.restaurant')),
            ],
            options={
                'db_table': 'dota.pizzas1',
            },
        ),
    ]
