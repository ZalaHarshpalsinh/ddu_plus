# Generated by Django 4.2.10 on 2024-03-09 06:47

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilePhoto', models.ImageField(upload_to='profile_photos/Departments')),
                ('name', models.CharField(max_length=100)),
                ('about', models.TextField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilePhoto', models.ImageField(upload_to='profile_photos/People')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('STUDENT', 'student'), ('EMPLOYEE', 'employee')], default='STUDENT', max_length=8),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)])),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.person')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='account',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='person',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.department'),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=50)),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.person')),
            ],
        ),
    ]