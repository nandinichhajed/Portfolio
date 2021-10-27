# Generated by Django 3.2.8 on 2021-10-27 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('message', models.TextField(verbose_name='Message')),
            ],
            options={
                'verbose_name': 'Contact Profile',
                'verbose_name_plural': 'Contact Profiles',
                'ordering': ['timestamp'],
            },
        ),
    ]
