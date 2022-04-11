# Generated by Django 4.0.3 on 2022-04-11 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='date_joined',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]
