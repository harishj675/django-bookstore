# Generated by Django 4.2.14 on 2024-08-01 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0004_alter_book_cover_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocklevel',
            name='remaining_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stocklevel',
            name='sell_quantity',
            field=models.IntegerField(default=0),
        ),
    ]