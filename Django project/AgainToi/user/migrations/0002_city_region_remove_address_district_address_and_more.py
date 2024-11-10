# Generated by Django 5.1.2 on 2024-11-10 10:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('map_link', models.URLField(blank=True, help_text='Link to the map of the city', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('map_link', models.URLField(blank=True, help_text='Link to the map of the region', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='address',
            name='district_address',
        ),
        migrations.AddField(
            model_name='address',
            name='map_link',
            field=models.URLField(blank=True, help_text='Link to the specific address location', null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.address'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='profile_images/profile.jpeg', null=True, upload_to='profile_images/'),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.city'),
        ),
        migrations.AddField(
            model_name='city',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='user.region'),
        ),
        migrations.AddField(
            model_name='address',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.region'),
        ),
    ]