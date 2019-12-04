# Generated by Django 2.2.7 on 2019-12-02 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('name', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('department', models.CharField(max_length=10)),
                ('job_position', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pc_assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pc_type', models.CharField(max_length=20)),
                ('sn', models.CharField(max_length=10, unique=True)),
                ('assets_num', models.IntegerField(max_length=15, null=True, unique=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.Person')),
            ],
        ),
    ]
