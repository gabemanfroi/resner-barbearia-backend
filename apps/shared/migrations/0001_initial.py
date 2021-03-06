# Generated by Django 3.2.9 on 2021-11-20 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Preço')),
                ('estimated_time', models.TimeField(verbose_name='Tempo Estimado')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
