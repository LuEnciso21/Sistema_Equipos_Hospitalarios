# Generated by Django 3.2 on 2024-11-06 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hce', '0004_auto_20241103_1750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='imagen',
        ),
    ]