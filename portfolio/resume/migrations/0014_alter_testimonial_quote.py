# Generated by Django 3.2.8 on 2021-11-21 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0013_alter_testimonial_quote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='quote',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
