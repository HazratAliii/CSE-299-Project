# Generated by Django 3.1.3 on 2021-05-17 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_tourists'),
    ]

    operations = [
        migrations.AddField(
            model_name='guides',
            name='hotel',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
