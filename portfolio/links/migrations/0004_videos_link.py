# Generated by Django 3.2.8 on 2021-11-23 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0003_auto_20211123_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
