# Generated by Django 3.1.3 on 2020-12-01 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='imageUrl',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]
