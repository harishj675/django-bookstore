# Generated by Django 4.2.14 on 2024-08-01 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0003_remove_bookspecifications_book_publishing_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_img',
            field=models.ImageField(blank=True, null=True, upload_to='books/images/'),
        ),
    ]