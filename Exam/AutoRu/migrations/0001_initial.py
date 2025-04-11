# Generated by Django 4.2.20 on 2025-04-11 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField()),
                ('brand', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Vehicle',
                'db_table': 'Vehicles',
            },
        ),
    ]
