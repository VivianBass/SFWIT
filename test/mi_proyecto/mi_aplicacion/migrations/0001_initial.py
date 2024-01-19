# Generated by Django 5.0.1 on 2024-01-18 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('lastname1', models.CharField(max_length=45)),
                ('lastname2', models.CharField(max_length=45)),
                ('username', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=128)),
                ('profile_picture', models.CharField(max_length=255)),
                ('birthdate', models.DateField()),
                ('creation_date', models.DateField()),
                ('update_date', models.DateField()),
            ],
        ),
    ]
