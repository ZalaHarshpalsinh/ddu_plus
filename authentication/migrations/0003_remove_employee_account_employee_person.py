# Generated by Django 4.2.10 on 2024-04-05 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_department_admins'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='account',
        ),
        migrations.AddField(
            model_name='employee',
            name='person',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='authentication.person'),
            preserve_default=False,
        ),
    ]
