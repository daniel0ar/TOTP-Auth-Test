# Generated by Django 3.1.3 on 2021-12-13 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TOTPLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('token', models.TextField(max_length=6)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.user')),
            ],
        ),
        migrations.CreateModel(
            name='TOTP',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('secret', models.TextField(max_length=20)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.user')),
            ],
        ),
    ]
