# Generated by Django 3.2.6 on 2021-08-05 21:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farm_food_auth', '0002_auto_20210803_1846'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProducerUserProfile',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField()),
                ('profile_image', models.ImageField(blank=True, upload_to='profiles')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='farm_food_auth.farmfooduser')),
            ],
        ),
        migrations.RemoveField(
            model_name='consumeruserprofile',
            name='id',
        ),
        migrations.AddField(
            model_name='consumeruserprofile',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='farm_food_auth.farmfooduser'),
            preserve_default=False,
        ),
    ]
