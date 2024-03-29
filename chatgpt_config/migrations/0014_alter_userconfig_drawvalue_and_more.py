# Generated by Django 4.2.4 on 2024-02-25 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatgpt_config', '0013_userconfig_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userconfig',
            name='drawvalue',
            field=models.CharField(blank=True, help_text='绘画模型', max_length=255, null=True, verbose_name='绘画模型'),
        ),
        migrations.AlterField(
            model_name='userconfig',
            name='proxyAdress',
            field=models.CharField(blank=True, help_text='配置值', max_length=255, null=True, verbose_name='配置值'),
        ),
        migrations.AlterField(
            model_name='userconfig',
            name='secretKey',
            field=models.CharField(blank=True, help_text='配置键', max_length=64, null=True, verbose_name='配置键'),
        ),
    ]
