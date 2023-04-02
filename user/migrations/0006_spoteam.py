# Generated by Django 4.1.6 on 2023-04-02 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpoTeam',
            fields=[
                ('sportevent', models.TextField(max_length=20)),
                ('name', models.TextField(max_length=20, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('team_mark', models.ImageField(null=True, upload_to='')),
                ('team_intro', models.TextField(max_length=200)),
            ],
        ),
    ]