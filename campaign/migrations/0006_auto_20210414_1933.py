# Generated by Django 3.1.3 on 2021-04-14 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0005_auto_20210414_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thirdchoice',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]