# Generated by Django 3.2.8 on 2021-11-03 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0009_certificate'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='Certificate'),
        ),
    ]