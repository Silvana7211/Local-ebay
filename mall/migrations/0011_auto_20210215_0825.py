# Generated by Django 3.1.5 on 2021-02-15 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0010_auto_20210215_0821'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bid',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='bid',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='bid',
            name='order',
        ),
    ]
