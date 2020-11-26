# Generated by Django 2.0.8 on 2020-03-18 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wyqapp', '0002_auto_20200208_1749'),
    ]

    operations = [
        migrations.CreateModel(
            name='ages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('sname', models.CharField(max_length=20)),
                ('sgender', models.BooleanField(default=True)),
                ('sage', models.IntegerField()),
                ('scontend', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
                ('sgrade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wyqapp.Grades')),
            ],
            options={
                'db_table': 'ages',
                'ordering': ['id'],
            },
        ),
    ]
