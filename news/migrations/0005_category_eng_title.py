# Generated by Django 3.2.8 on 2021-10-27 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='eng_title',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
