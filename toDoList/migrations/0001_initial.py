# Generated by Django 3.1.4 on 2020-12-24 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=False)),
                ('settime', models.PositiveIntegerField()),
                ('passedtime', models.PositiveIntegerField()),
            ],
        ),
    ]