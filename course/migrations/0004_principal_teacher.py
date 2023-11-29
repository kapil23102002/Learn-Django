# Generated by Django 4.2.7 on 2023-11-29 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_remove_principal_commoninfo_ptr_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Principal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('expenses', models.IntegerField()),
                ('superuser', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('salary', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
