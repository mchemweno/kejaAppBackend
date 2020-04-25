# Generated by Django 3.0.5 on 2020-04-16 12:36

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0010_auto_20200416_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='master_image',
            field=imagekit.models.fields.ProcessedImageField(upload_to='media/master_image/%y/%m/%d'),
        ),
    ]
