# Generated by Django 2.0.5 on 2018-07-01 21:41

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('django_freeradius', '0015_radiusbatch'),
    ]

    operations = [
        migrations.CreateModel(
            name='RadiusProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(db_index=True, help_text='A unique profile name', max_length=128, verbose_name='name')),
                ('daily_session_limit', models.BigIntegerField(blank=True, null=True, verbose_name='daily session limit')),
                ('daily_bandwidth_limit', models.BigIntegerField(blank=True, null=True, verbose_name='daily bandwidth limit')),
                ('max_all_time_limit', models.BigIntegerField(blank=True, null=True, verbose_name='maximum all time session limit')),
                ('default', models.BooleanField(default=False, verbose_name='Use this profile as the default profile')),
            ],
            options={
                'verbose_name': 'radius profile',
                'verbose_name_plural': 'radius profiles',
                'abstract': False,
                'swappable': 'DJANGO_FREERADIUS_RADIUSPROFILE_MODEL',
            },
        ),
    ]
