# Generated by Django 3.2.8 on 2021-11-23 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0031_alter_media_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
