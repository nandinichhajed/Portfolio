# Generated by Django 3.2.8 on 2021-11-21 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(max_length=200)),
                ('instagram', models.CharField(max_length=200)),
                ('linkdin', models.CharField(max_length=200)),
                ('twitter', models.CharField(max_length=200)),
                ('github', models.CharField(max_length=200)),
            ],
        ),
    ]