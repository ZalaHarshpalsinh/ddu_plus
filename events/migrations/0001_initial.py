# Generated by Django 4.2.10 on 2024-03-30 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilePhoto', models.ImageField(upload_to='profile_photos/Clubs')),
                ('name', models.CharField(max_length=100)),
                ('about', models.TextField(max_length=5000)),
                ('admins', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('poster', models.ImageField(upload_to='events/')),
                ('description', models.TextField(max_length=5000)),
                ('dateTime', models.DateTimeField()),
                ('venue', models.TextField(max_length=500)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.club')),
            ],
        ),
    ]
