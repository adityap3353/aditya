# Generated by Django 2.1.2 on 2019-03-26 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deco', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='a',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]