# Generated by Django 4.2.7 on 2023-11-29 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_principal_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='principal',
            name='superuser',
        ),
    ]
