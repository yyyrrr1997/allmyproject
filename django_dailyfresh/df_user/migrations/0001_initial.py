# Generated by Django 3.0.4 on 2020-03-25 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uName', models.CharField(max_length=20)),
                ('uPWD', models.CharField(max_length=40)),
                ('uEmail', models.CharField(max_length=30)),
                ('uConsignee', models.CharField(max_length=30)),
                ('uAddress', models.CharField(max_length=100)),
                ('uPostcodes', models.CharField(max_length=6)),
                ('uPhone', models.CharField(max_length=11)),
            ],
        ),
    ]
