# Generated by Django 3.2.8 on 2021-11-21 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0014_alter_testimonial_quote'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='certificate_link',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
