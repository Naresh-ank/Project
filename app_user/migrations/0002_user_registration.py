# Generated by Django 2.1.2 on 2019-04-24 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Registration',
            fields=[
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=30)),
                ('address', models.TextField(max_length=300)),
                ('contact', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('nominee', models.CharField(max_length=30)),
            ],
        ),
    ]
