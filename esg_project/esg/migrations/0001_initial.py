# Generated by Django 5.2.1 on 2025-05-30 08:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('sector', models.CharField(max_length=100)),
                ('reporting_period', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('function', models.CharField(help_text='What this unit does (e.g., Manufacturing, Sales)', max_length=255)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business_units', to='esg.company')),
            ],
        ),
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('environmental', 'Environmental'), ('social', 'Social'), ('governance', 'Governance')], max_length=20)),
                ('year', models.IntegerField()),
                ('value', models.FloatField()),
                ('unit', models.CharField(max_length=50)),
                ('business_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='metrics', to='esg.businessunit')),
            ],
        ),
        migrations.CreateModel(
            name='MetricValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reporting_period', models.CharField(max_length=100)),
                ('value', models.FloatField()),
                ('unit', models.CharField(help_text='e.g., kWh, %, incidents', max_length=50)),
                ('year', models.IntegerField()),
                ('business_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='metric_values', to='esg.businessunit')),
                ('metric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='values', to='esg.metric')),
            ],
        ),
    ]
