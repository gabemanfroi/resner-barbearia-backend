# Generated by Django 3.2.9 on 2021-11-21 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_alter_appointment_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='contact_number',
            field=models.CharField(default='', max_length=14),
            preserve_default=False,
        ),
    ]
