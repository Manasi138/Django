# Generated by Django 4.2.17 on 2024-12-18 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empName', models.CharField(max_length=100)),
                ('empsalary', models.FloatField(default=0.0)),
                ('designation', models.CharField(max_length=100)),
            ],
        ),
    ]