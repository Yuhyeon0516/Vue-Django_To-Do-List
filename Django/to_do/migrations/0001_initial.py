# Generated by Django 4.2.5 on 2023-09-30 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=5, verbose_name='NAME')),
                ('todo', models.CharField(max_length=50, verbose_name='TODO')),
            ],
        ),
    ]
