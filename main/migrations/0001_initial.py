# Generated by Django 4.2.5 on 2023-09-19 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('amount', models.IntegerField()),
                ('category', models.TextField(max_length=100)),
                ('image', models.URLField()),
                ('berat', models.TextField(max_length=100)),
            ],
        ),
    ]
