# Generated by Django 3.0.8 on 2021-03-15 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Covid_Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.TextField()),
                ('in_treatmeant', models.IntegerField(default=0)),
                ('treated', models.IntegerField(default=0)),
                ('death', models.IntegerField(default=0)),
            ],
        ),
    ]
