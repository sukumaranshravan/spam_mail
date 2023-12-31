# Generated by Django 3.2.12 on 2023-11-05 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_admin', '0003_hobby_factor_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='season_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='season_factor_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factor_name', models.CharField(max_length=20)),
                ('season_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_admin.season_tb')),
            ],
        ),
    ]
