# Generated by Django 3.2.8 on 2021-11-22 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0020_auto_20211122_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='issue_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]