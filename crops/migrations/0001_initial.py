# Generated by Django 4.1.7 on 2023-04-15 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Biome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biome_name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Seasons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Seasons',
            },
        ),
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crop_name', models.CharField(max_length=50)),
                ('image', models.ImageField(null=True, upload_to='pics')),
                ('buy', models.PositiveIntegerField()),
                ('sell', models.PositiveIntegerField()),
                ('reharvest', models.PositiveIntegerField(default=1)),
                ('total_sell', models.PositiveIntegerField(blank=True)),
                ('premium_sell', models.PositiveIntegerField(null=True)),
                ('total_profit', models.PositiveIntegerField(blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('biome', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='biome', to='crops.biome')),
                ('grow_season', models.ManyToManyField(to='crops.seasons')),
            ],
        ),
    ]
