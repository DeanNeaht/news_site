# Generated by Django 3.2.8 on 2021-10-27 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_category_eng_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(blank=True, unique=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]
