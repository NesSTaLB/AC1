# Generated by Django 5.1.4 on 2025-01-07 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_alter_customuser_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='engineer',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='البريد الإلكتروني'),
        ),
        migrations.AddField(
            model_name='engineer',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='الهاتف'),
        ),
    ]
