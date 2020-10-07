# Generated by Django 3.1.2 on 2020-10-07 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('inclination', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='people',
            field=models.ManyToManyField(to='main_app.Person'),
        ),
    ]
