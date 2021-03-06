# Generated by Django 3.2.8 on 2021-10-27 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0008_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Certificate',
                'verbose_name_plural': 'Certificates',
            },
        ),
    ]
