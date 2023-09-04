# Generated by Django 4.2.1 on 2023-09-01 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('desc', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='products_images/')),
            ],
        ),
    ]
