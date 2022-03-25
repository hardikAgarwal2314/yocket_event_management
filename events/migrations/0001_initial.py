# Generated by Django 4.0.3 on 2022-03-24 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(max_length=100)),
                ('starting_time', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('duration', models.IntegerField(default=0, help_text='The duration of the event in minutes')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]