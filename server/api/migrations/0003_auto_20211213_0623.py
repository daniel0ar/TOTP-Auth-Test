# Generated by Django 3.1.3 on 2021-12-13 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_totp_totplog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='totp',
            name='userId',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='totplog',
            name='userId',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
