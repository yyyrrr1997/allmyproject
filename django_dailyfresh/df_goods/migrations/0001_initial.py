# Generated by Django 3.0.4 on 2020-03-26 08:28

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ttitle', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gtitle', models.CharField(max_length=20)),
                ('gpic', models.CharField(max_length=100)),
                ('gprice', models.DecimalField(decimal_places=2, max_digits=5)),
                ('gunit', models.CharField(max_length=20)),
                ('gclick', models.IntegerField()),
                ('gbrief', models.CharField(max_length=200)),
                ('gstock', models.IntegerField()),
                ('gcontent', tinymce.models.HTMLField()),
                ('isDelete', models.BooleanField(default=False)),
                ('gtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df_goods.TypeInfo')),
            ],
        ),
    ]
