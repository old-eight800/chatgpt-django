# Generated by Django 4.2.4 on 2024-02-18 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatgpt_image', '0008_imagemessage_image_quality'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagemessage',
            old_name='image_quality',
            new_name='imageQuality',
        ),
    ]
