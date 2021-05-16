# Generated by Django 3.1.3 on 2021-04-12 08:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('hrm', '0001_initial'),
        ('crm', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='touchpoint',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='crm_company_touchpoint', to='users.company'),
        ),
        migrations.AddField(
            model_name='touchpoint',
            name='lead',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lead_touch_point', to='crm.lead'),
        ),
        migrations.AddField(
            model_name='touchpoint',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='strategy',
            name='audience',
            field=models.ManyToManyField(to='crm.Audience'),
        ),
        migrations.AddField(
            model_name='strategy',
            name='available_channels',
            field=models.ManyToManyField(to='crm.Channel'),
        ),
        migrations.AddField(
            model_name='strategy',
            name='color_palette',
            field=models.ManyToManyField(to='crm.ColorPalette'),
        ),
        migrations.AddField(
            model_name='strategy',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_strategies', to='users.company'),
        ),
        migrations.AddField(
            model_name='strategy',
            name='culture_tone',
            field=models.ManyToManyField(to='crm.CultureTone'),
        ),
        migrations.AddField(
            model_name='strategy',
            name='language',
            field=models.ManyToManyField(to='crm.Language'),
        ),
        migrations.AddField(
            model_name='strategy',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='product',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_products', to='users.company'),
        ),
        migrations.AddField(
            model_name='product',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='product',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_products', to='hrm.project'),
        ),
        migrations.AddField(
            model_name='partnerteammembercommissionrule',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='crm_company_partnerteammembercommissionrule', to='users.company'),
        ),
        migrations.AddField(
            model_name='partnerteammembercommissionrule',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='partnerteammembercommissionrule',
            name='partner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='partner_partner_team_member_commission_rules', to='crm.partner'),
        ),
        migrations.AddField(
            model_name='partnerteammembercommissionrule',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_partner_team_members_commission_rules', to='crm.product'),
        ),
        migrations.AddField(
            model_name='partnerteammembercommissionrule',
            name='team_member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_member_partner_team_member_commission_rules', to='hrm.candidate'),
        ),
        migrations.AddField(
            model_name='partnercommissionrule',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='crm_company_partnercommissionrule', to='users.company'),
        ),
        migrations.AddField(
            model_name='partnercommissionrule',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='partnercommissionrule',
            name='partner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='partner_partner_commission_rules', to='crm.partner'),
        ),
        migrations.AddField(
            model_name='partnercommissionrule',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_partner_commission_rules', to='crm.product'),
        ),
        migrations.AddField(
            model_name='partner',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='crm_company_partner', to='users.company'),
        ),
        migrations.AddField(
            model_name='partner',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='partner',
            name='partner_to_companies',
            field=models.ManyToManyField(to='users.Company'),
        ),
        migrations.AddField(
            model_name='partner',
            name='partners_company',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='partners_company_partner', to='users.company'),
        ),
        migrations.AddField(
            model_name='pagevisit',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.company'),
        ),
        migrations.AddField(
            model_name='pagevisit',
            name='lead',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.lead'),
        ),
        migrations.AddField(
            model_name='pagevisit',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='pagevisit',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.funnelcomp'),
        ),
        migrations.AddField(
            model_name='pagevisit',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='opendemails',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.company'),
        ),
        migrations.AddField(
            model_name='opendemails',
            name='lead',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.lead'),
        ),
        migrations.AddField(
            model_name='opendemails',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='opendemails',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='leadstage',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='crm_company_leadstage', to='users.company'),
        ),
        migrations.AddField(
            model_name='leadstage',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='lead',
            name='acquired_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='acquired_by_Leads', to='hrm.candidate'),
        ),
        migrations.AddField(
            model_name='lead',
            name='audience',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='audience_leads', to='crm.audience'),
        ),
        migrations.AddField(
            model_name='lead',
            name='audienceInteraction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.audienceinteraction'),
        ),
        migrations.AddField(
            model_name='lead',
            name='campaigns',
            field=models.ManyToManyField(blank=True, to='crm.Campaign'),
        ),
        migrations.AddField(
            model_name='lead',
            name='candidate',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='candidate_lead', to='hrm.candidate'),
        ),
        migrations.AddField(
            model_name='lead',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='crm_company_lead', to='users.company'),
        ),
        migrations.AddField(
            model_name='lead',
            name='converted_lead_stage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='converted_lead_stage_leads', to='crm.convertedleadstage'),
        ),
        migrations.AddField(
            model_name='lead',
            name='initial_capture_campaign',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='initial_capture_campaign_leads', to='crm.campaign'),
        ),
        migrations.AddField(
            model_name='lead',
            name='lead_stage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lead_stage_leads', to='crm.leadstage'),
        ),
        migrations.AddField(
            model_name='lead',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='language',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='crm_company_language', to='users.company'),
        ),
        migrations.AddField(
            model_name='language',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='kpi',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='crm_company_kpi', to='users.company'),
        ),
        migrations.AddField(
            model_name='kpi',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='interest',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='crm_company_interest', to='users.company'),
        ),
        migrations.AddField(
            model_name='interest',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='funnelcomp',
            name='channel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='channel_funnel_comps', to='crm.channel'),
        ),
        migrations.AddField(
            model_name='funnelcomp',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='crm_company_funnelcomp', to='users.company'),
        ),
        migrations.AddField(
            model_name='funnelcomp',
            name='funnel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='funnel_funnel_comps', to='crm.funnel'),
        ),
        migrations.AddField(
            model_name='funnelcomp',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='funnel',
            name='campaigns',
            field=models.ManyToManyField(to='crm.Campaign'),
        ),
        migrations.AddField(
            model_name='funnel',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='crm_company_funnel', to='users.company'),
        ),
        migrations.AddField(
            model_name='funnel',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='culturetone',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='crm_company_culturetone', to='users.company'),
        ),
        migrations.AddField(
            model_name='culturetone',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='convertedleadstage',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='crm_company_convertedleadstage', to='users.company'),
        ),
        migrations.AddField(
            model_name='convertedleadstage',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='commission',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='crm_company_commission', to='users.company'),
        ),
        migrations.AddField(
            model_name='commission',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='commission',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_commissions', to='crm.product'),
        ),
        migrations.AddField(
            model_name='commission',
            name='receiver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='candidate_commissions', to='hrm.candidate'),
        ),
        migrations.AddField(
            model_name='colorpalette',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='crm_company_colorpalette', to='users.company'),
        ),
        migrations.AddField(
            model_name='colorpalette',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='channel',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='crm_company_channel', to='users.company'),
        ),
        migrations.AddField(
            model_name='channel',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='crm_company_campaign', to='users.company'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_campaigns', to='crm.product'),
        ),
        migrations.AddField(
            model_name='audienceinteraction',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='crm_company_audienceinteraction', to='users.company'),
        ),
        migrations.AddField(
            model_name='audienceinteraction',
            name='last_product_purchased',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.product'),
        ),
        migrations.AddField(
            model_name='audienceinteraction',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='audiencecenter',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='crm_company_audiencecenter', to='users.company'),
        ),
        migrations.AddField(
            model_name='audiencecenter',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='audienceagerange',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='crm_company_audienceagerange', to='users.company'),
        ),
        migrations.AddField(
            model_name='audienceagerange',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='audience',
            name='age_ranges',
            field=models.ManyToManyField(to='crm.AudienceAgeRange'),
        ),
        migrations.AddField(
            model_name='audience',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='crm_company_audience', to='users.company'),
        ),
        migrations.AddField(
            model_name='audience',
            name='found_at',
            field=models.ManyToManyField(to='crm.AudienceCenter'),
        ),
        migrations.AddField(
            model_name='audience',
            name='interests',
            field=models.ManyToManyField(to='crm.Interest'),
        ),
        migrations.AddField(
            model_name='audience',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
    ]
