# Generated by Django 5.0.6 on 2024-06-04 21:56

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JuristName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('specialization', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=255, null=True)),
                ('rating', models.FloatField(default=0.0)),
            ],
            options={
                'db_table': 'juristName',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.BigIntegerField()),
                ('user_name', models.CharField(max_length=255)),
                ('tg_name', models.CharField(max_length=255)),
                ('user_phone', models.CharField(blank=True, max_length=255, null=True)),
                ('user_mail', models.CharField(blank=True, max_length=255, null=True)),
                ('active', models.IntegerField(default=1)),
                ('user_coin', models.IntegerField(default=0)),
                ('wallet', models.IntegerField(default=0)),
                ('date_register', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'users',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('currency', models.CharField(default='RUB', max_length=10)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')], default='pending', max_length=10)),
                ('date_created', models.DateField(default=django.utils.timezone.now)),
                ('date_completed', models.DateField(blank=True, null=True)),
                ('jurist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='bot.juristname')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='bot.user')),
            ],
            options={
                'db_table': 'payments',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_path', models.CharField(max_length=255)),
                ('upload_date', models.DateField(default=django.utils.timezone.now)),
                ('jurist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='bot.juristname')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='bot.user')),
            ],
            options={
                'db_table': 'documents',
                'managed': True,
            },
        ),
    ]