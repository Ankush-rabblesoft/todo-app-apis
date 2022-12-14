# Generated by Django 4.0.4 on 2022-05-11 04:35

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=255)),
                ('status', models.IntegerField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 5, 11, 4, 35, 11, 375379, tzinfo=utc))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2022, 5, 11, 4, 35, 11, 375391, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('phone', models.BigIntegerField()),
                ('password', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 5, 11, 4, 35, 11, 374783, tzinfo=utc))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2022, 5, 11, 4, 35, 11, 374800, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=255)),
                ('phone', models.BigIntegerField()),
                ('subject', models.TextField(max_length=255)),
                ('message', models.TextField(max_length=2550)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 5, 11, 4, 35, 11, 375075, tzinfo=utc))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2022, 5, 11, 4, 35, 11, 375085, tzinfo=utc))),
                ('full_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
        ),
    ]
