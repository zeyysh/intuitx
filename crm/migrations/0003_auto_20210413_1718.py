# Generated by Django 3.1.3 on 2021-04-13 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20210412_1247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='audienceInteraction',
        ),
        migrations.AddField(
            model_name='lead',
            name='interaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='interaction_leads', to='crm.audienceinteraction'),
        ),
    ]
