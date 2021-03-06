# Generated by Django 3.1.3 on 2021-04-12 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('hrm', '0001_initial'),
        ('crm', '0001_initial'),
        ('campaign', '0002_selector_age_ranges'),
    ]

    operations = [
        migrations.AddField(
            model_name='selector',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='campaign_company_selector', to='users.company'),
        ),
        migrations.AddField(
            model_name='selector',
            name='companys',
            field=models.ManyToManyField(to='users.Company'),
        ),
        migrations.AddField(
            model_name='selector',
            name='interest',
            field=models.ManyToManyField(to='crm.Interest'),
        ),
        migrations.AddField(
            model_name='selector',
            name='languages',
            field=models.ManyToManyField(to='campaign.Languages'),
        ),
        migrations.AddField(
            model_name='selector',
            name='locations',
            field=models.ManyToManyField(to='campaign.Location'),
        ),
        migrations.AddField(
            model_name='selector',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='selector',
            name='projects',
            field=models.ManyToManyField(to='hrm.Project'),
        ),
        migrations.AddField(
            model_name='selectionprofile',
            name='campaign',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.campaign'),
        ),
        migrations.AddField(
            model_name='selectionprofile',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='campaign_company_selectionprofile', to='users.company'),
        ),
        migrations.AddField(
            model_name='selectionprofile',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='selectionprofile',
            name='selector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaign.selector'),
        ),
        migrations.AddField(
            model_name='querysetrule',
            name='selector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='queryset_rules', to='campaign.selector'),
        ),
        migrations.AddField(
            model_name='location',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='campaign_company_location', to='users.company'),
        ),
        migrations.AddField(
            model_name='location',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='languages',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='campaign_company_languages', to='users.company'),
        ),
        migrations.AddField(
            model_name='languages',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
    ]
