# Generated by Django 4.2.4 on 2024-02-25 20:15

import chatgpt_config.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatgpt_config', '0015_alter_userconfig_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userconfig',
            name='content',
            field=models.JSONField(default=chatgpt_config.models.get_chatModel_list),
        ),
    ]
