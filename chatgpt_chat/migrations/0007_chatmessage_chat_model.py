# Generated by Django 4.2.4 on 2024-02-13 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatgpt_chat', '0006_alter_chatmessage_total_tokens'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='chat_model',
            field=models.CharField(blank=True, help_text='会话模型', max_length=32, null=True, verbose_name='会话模型'),
        ),
    ]
