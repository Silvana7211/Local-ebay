# Generated by Django 3.1.5 on 2021-02-15 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0002_auto_20210215_0541'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='owner',
        ),
    ]
