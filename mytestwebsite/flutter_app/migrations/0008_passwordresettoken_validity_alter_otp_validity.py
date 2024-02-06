# Generated by Django 4.2.9 on 2024-02-06 21:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('flutter_app', '0007_alter_token_user_passwordresettoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='passwordresettoken',
            name='validity',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='otp',
            name='validity',
            field=models.DateField(auto_now_add=True),
        ),
    ]