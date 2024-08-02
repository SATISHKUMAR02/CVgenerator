# Generated by Django 5.0.6 on 2024-06-30 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=15)),
                ('about', models.TextField(max_length=5000)),
                ('school', models.CharField(max_length=200)),
                ('college', models.CharField(max_length=200)),
                ('experience', models.TextField(max_length=1000)),
                ('skills', models.TextField(max_length=2000)),
            ],
        ),
    ]
