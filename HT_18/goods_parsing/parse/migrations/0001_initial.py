# Generated by Django 5.0 on 2024-01-03 23:30

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
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('brandName', models.CharField(blank=True, max_length=50, null=True, verbose_name='Brand')),
                ('regularPrice', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Regular Price')),
                ('link', models.URLField(max_length=255, verbose_name='Product link')),
            ],
        ),
    ]
