# Generated by Django 3.0.7 on 2022-02-03 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=500)),
                ('nombre', models.CharField(max_length=500)),
                ('puesto', models.CharField(max_length=500)),
            ],
        ),
    ]
