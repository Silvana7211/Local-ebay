# Generated by Django 3.1.5 on 2021-02-15 04:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mall', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='owner',
            new_name='placer',
        ),
        migrations.AddField(
            model_name='product',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bid',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='mall.product'),
        ),
    ]
