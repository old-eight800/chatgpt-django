# Generated by Django 4.2.4 on 2024-02-01 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatgpt_config', '0007_rename_describtion_userconfig_chatmodel_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userconfig',
            old_name='customerId',
            new_name='baseUserId',
        ),
    ]
