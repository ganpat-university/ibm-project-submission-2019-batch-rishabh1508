# Generated by Django 3.2.12 on 2023-02-22 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('A', models.CharField(blank=True, max_length=512)),
                ('B', models.CharField(blank=True, max_length=512)),
                ('service', models.CharField(blank=True, max_length=512)),
                ('Day', models.CharField(blank=True, max_length=2)),
                ('Month', models.CharField(blank=True, max_length=2)),
                ('Year', models.CharField(blank=True, max_length=2)),
                ('Sign', models.ImageField(blank=True, upload_to='Sign/')),
                ('To', models.CharField(blank=True, max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
