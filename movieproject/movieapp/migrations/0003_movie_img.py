# Generated by Django 3.2.12 on 2022-05-15 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_auto_20220511_0035'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default=1, upload_to='gallery'),
            preserve_default=False,
        ),
    ]