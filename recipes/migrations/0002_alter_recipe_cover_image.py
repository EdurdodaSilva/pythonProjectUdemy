# Generated by Django 5.0.1 on 2024-02-05 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cover_image',
            field=models.ImageField(blank=True, upload_to='recipes/cover/%Y/%m/%d/'),
        ),
    ]
