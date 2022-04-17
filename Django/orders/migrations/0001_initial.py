# Generated by Django 2.1.5 on 2020-06-07 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=64)),
                ('employer', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=64)),
                ('typeOrder', models.CharField(max_length=64)),
                ('cost', models.CharField(max_length=64)),
                ('createDate', models.CharField(max_length=64)),
                ('startDate', models.CharField(max_length=64)),
                ('endDate', models.CharField(max_length=64)),
                ('priority', models.CharField(max_length=64)),
            ],
        ),
    ]