# Generated by Django 5.0.7 on 2024-08-08 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=255)),
                ('weather', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('google_map_link', models.URLField(max_length=2000)),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.TextField()),
            ],
        ),
    ]
