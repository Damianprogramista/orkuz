# Generated by Django 4.0.4 on 2022-05-24 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.TextField()),
                ('engine', models.TextField()),
                ('vin', models.TextField()),
                ('production_date', models.DateField()),
                ('is_4x4', models.BooleanField()),
            ],
        ),
    ]
