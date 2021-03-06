# Generated by Django 3.2.8 on 2021-11-23 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_videos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media')),
            ],
            options={
                'verbose_name': 'image',
                'verbose_name_plural': 'images',
            },
        ),
        migrations.AlterField(
            model_name='videos',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='videos',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
    ]
