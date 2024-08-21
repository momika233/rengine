# Generated by Django 3.2.23 on 2024-06-19 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('startScan', '0001_initial'),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoNote',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_done', models.BooleanField(default=False)),
                ('is_important', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.project')),
                ('scan_history', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='startScan.scanhistory')),
                ('subdomain', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='startScan.subdomain')),
            ],
        ),
    ]
