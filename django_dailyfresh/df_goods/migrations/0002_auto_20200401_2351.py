# Generated by Django 3.0.4 on 2020-04-01 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='gprice',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gunit',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]