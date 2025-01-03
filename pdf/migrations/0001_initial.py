# Generated by Django 5.1.3 on 2024-11-11 10:39

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
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.IntegerField()),
                ('summary', models.TextField(max_length=2000)),
                ('degree', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('experience', models.CharField(max_length=500)),
                ('skills', models.CharField(max_length=1000)),
            ],
        ),
    ]
