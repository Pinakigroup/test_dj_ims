# Generated by Django 3.1.13 on 2022-12-28 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=12, unique=True)),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
    ]
