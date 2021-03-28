# Generated by Django 3.1.3 on 2021-03-28 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('meals', models.CharField(max_length=100)),
                ('review', models.CharField(max_length=100)),
            ],
        ),
    ]