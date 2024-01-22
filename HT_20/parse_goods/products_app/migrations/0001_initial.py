# Generated by Django 5.0.1 on 2024-01-21 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('brand_name', models.CharField(max_length=100)),
                ('regular_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('link', models.CharField(max_length=100)),
                ('category', models.TextField()),
            ],
        ),
    ]
