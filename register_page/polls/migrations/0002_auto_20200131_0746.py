# Generated by Django 3.0.2 on 2020-01-31 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='password1',
            new_name='conform_password',
        ),
        migrations.RenameField(
            model_name='registration',
            old_name='password2',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='last_name',
        ),
        migrations.AddField(
            model_name='registration',
            name='user_name',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
    ]
