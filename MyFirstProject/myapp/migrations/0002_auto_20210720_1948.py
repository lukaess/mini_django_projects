# Generated by Django 3.2.5 on 2021-07-20 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='details',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='feature',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]