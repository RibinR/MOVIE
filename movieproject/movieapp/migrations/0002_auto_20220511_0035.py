# Generated by Django 3.2.12 on 2022-05-10 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='desc',
            field=models.TextField(default=77777),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='name',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.IntegerField(default=1234567890),
            preserve_default=False,
        ),
    ]
