# Generated by Django 5.1.2 on 2024-10-24 10:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='street_address',
            new_name='district_address',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.address'),
        ),
    ]
