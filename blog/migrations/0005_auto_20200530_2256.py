# Generated by Django 3.0.6 on 2020-05-30 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200530_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='profile.jpg', upload_to='images/'),
        ),
    ]