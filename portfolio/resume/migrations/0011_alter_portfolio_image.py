# Generated by Django 3.2.8 on 2021-11-03 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0010_certificate_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Portfolio'),
        ),
    ]
