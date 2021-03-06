# Generated by Django 3.1.3 on 2021-04-13 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_auto_20210413_1718'),
        ('campaign', '0003_auto_20210412_1247'),
    ]

    operations = [
        migrations.CreateModel(
            name='FirstChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130)),
            ],
        ),
        migrations.CreateModel(
            name='SecondChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130)),
                ('first_choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaign.firstchoice')),
            ],
        ),
        migrations.RenameField(
            model_name='languages',
            old_name='Audiance_language',
            new_name='Audience_language',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='Audiance_location',
            new_name='Audience_location',
        ),
        migrations.RemoveField(
            model_name='querysetrule',
            name='attribute',
        ),
        migrations.RemoveField(
            model_name='querysetrule',
            name='interaction',
        ),
        migrations.RemoveField(
            model_name='querysetrule',
            name='lead_ownership',
        ),
        migrations.RemoveField(
            model_name='selector',
            name='age_ranges',
        ),
        migrations.RemoveField(
            model_name='selector',
            name='companys',
        ),
        migrations.RemoveField(
            model_name='selector',
            name='include_or_exclude',
        ),
        migrations.RemoveField(
            model_name='selector',
            name='interest',
        ),
        migrations.RemoveField(
            model_name='selector',
            name='languages',
        ),
        migrations.RemoveField(
            model_name='selector',
            name='locations',
        ),
        migrations.RemoveField(
            model_name='selector',
            name='projects',
        ),
        migrations.AddField(
            model_name='selector',
            name='content',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='selector',
            name='from_sender',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='ThirdChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age_ranges', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='crm.audienceagerange')),
                ('interest', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='crm.interest')),
                ('languages', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='campaign.languages')),
                ('locations', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='campaign.location')),
                ('second_choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaign.secondchoice')),
            ],
        ),
        migrations.AddField(
            model_name='querysetrule',
            name='first_choice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='campaign.firstchoice'),
        ),
        migrations.AddField(
            model_name='querysetrule',
            name='second_choice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='campaign.secondchoice'),
        ),
        migrations.AddField(
            model_name='querysetrule',
            name='third_choice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='campaign.thirdchoice'),
        ),
    ]
