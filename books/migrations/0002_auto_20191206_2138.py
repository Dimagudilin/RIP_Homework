# Generated by Django 2.2.7 on 2019-12-06 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, upload_to='books/%Y/%m/%d'),
        ),
    ]