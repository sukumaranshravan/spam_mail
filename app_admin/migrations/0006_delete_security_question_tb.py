# Generated by Django 3.2.12 on 2023-11-06 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_admin', '0005_security_question_tb'),
    ]

    operations = [
        migrations.DeleteModel(
            name='security_question_tb',
        ),
    ]
