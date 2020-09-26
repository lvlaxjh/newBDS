# Generated by Django 3.1 on 2020-08-24 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_examineimg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examineimg',
            name='aimId',
        ),
        migrations.AddField(
            model_name='examineimg',
            name='examine',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='mainapp.toexamine', verbose_name='该图片所属信息'),
        ),
    ]
