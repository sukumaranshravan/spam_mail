# Generated by Django 3.2.12 on 2023-11-14 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0009_blocklist_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='agefactor_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_age', models.IntegerField()),
                ('max_age', models.IntegerField()),
                ('factor_name', models.CharField(max_length=20)),
            ],
        ),
    ]
