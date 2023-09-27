# Generated by Django 4.2.4 on 2023-09-22 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatgpt_image', '0003_imagemessage_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemessage',
            name='number',
            field=models.CharField(blank=True, help_text='生成数量', max_length=255, null=True, verbose_name='生成数量'),
        ),
        migrations.AlterField(
            model_name='imagemessage',
            name='prompt',
            field=models.TextField(blank=True, help_text='提示语', null=True, verbose_name='提示语'),
        ),
        migrations.AlterField(
            model_name='imagemessage',
            name='res_data',
            field=models.JSONField(null=True, verbose_name='返回的图片数据'),
        ),
        migrations.AlterField(
            model_name='imagemessage',
            name='size',
            field=models.CharField(blank=True, help_text='生成分辨率', max_length=255, null=True, verbose_name='生成分辨率'),
        ),
        migrations.AlterField(
            model_name='imagemessage',
            name='username',
            field=models.EmailField(blank=True, help_text='用户名', max_length=64, null=True, verbose_name='用户名'),
        ),
        migrations.AlterField(
            model_name='imagemessage',
            name='uuid',
            field=models.CharField(blank=True, help_text='唯一编码', max_length=255, null=True, verbose_name='唯一编码'),
        ),
    ]
