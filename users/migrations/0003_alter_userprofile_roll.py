# Generated by Django 4.2.14 on 2024-07-31 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprofile_delete_userinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='roll',
            field=models.CharField(choices=[('User', 'User'), ('Staff', 'Staff'), ('Manger', 'Manger')], default='User', max_length=50),
        ),
    ]
