# Generated by Django 3.2.8 on 2021-11-22 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0018_remove_portfolio_is_featured'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificate',
            old_name='name',
            new_name='academy',
        ),
    ]
