# Generated by Django 3.1.3 on 2021-04-12 08:17

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=80)),
                ('description', models.CharField(max_length=500)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AudienceAgeRange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age_range', models.CharField(choices=[('0', '0-6'), ('1', '7-12'), ('2', '13-15'), ('3', '16-18'), ('4', '19-22'), ('5', '23-29'), ('6', '30-34'), ('7', '34-39'), ('8', '40-49'), ('9', '50-59'), ('10', '60-69'), ('11', '70-80'), ('12', '> 80')], default='5', max_length=12)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AudienceCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=80)),
                ('center_type', models.CharField(choices=[('location', 'Location'), ('platform', 'Platform'), ('influencer', 'Influencer'), ('influencer-type', 'Influencer Type'), ('thing', 'Thing')], default='5', max_length=25)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AudienceInteraction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_purchase_date', models.DateTimeField()),
                ('last_page_visit', models.DateTimeField()),
                ('last_email_open', models.CharField(max_length=100)),
                ('last_touchpoint_date', models.DateTimeField()),
                ('last_newsletter_signup', models.CharField(max_length=100)),
                ('specific_product_last_purchase_date', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign_name', models.CharField(max_length=80)),
                ('roi', models.FloatField()),
                ('budget', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ColorPalette',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(max_length=7)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Commission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('paid', 'Paid'), ('pending-payout', 'Pending Payout')], default='5', max_length=25)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ConvertedLeadStage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CultureTone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=80)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Funnel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('funnel_name', models.CharField(max_length=80)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FunnelComp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=80)),
                ('interest_type', models.CharField(choices=[('location', 'Location'), ('food', 'Food'), ('product', 'Product'), ('topic', 'Topic'), ('thing', 'Thing')], default='5', max_length=12)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Kpi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reach', models.IntegerField()),
                ('engagement', models.IntegerField()),
                ('clicks', models.IntegerField()),
                ('click_conversion', models.FloatField()),
                ('cpc', models.FloatField()),
                ('cpm', models.IntegerField()),
                ('sales', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=80)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('lastname', models.CharField(max_length=80)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=25)),
                ('city', models.CharField(max_length=25)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=18, null=True)),
                ('street_number', models.CharField(blank=True, max_length=10, null=True)),
                ('suite', models.CharField(blank=True, max_length=25, null=True)),
                ('floor', models.CharField(blank=True, max_length=25, null=True)),
                ('instagram', models.CharField(blank=True, max_length=80, null=True)),
                ('acquired_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LeadStage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='opendEmails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_date', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PageVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Page_visit_date', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PartnerCommissionRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PartnerTeamMemberCommissionRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('is_subscription_based', models.BooleanField(default=False)),
                ('price', models.FloatField()),
                ('availability_start_date', models.DateTimeField()),
                ('availability_end_date', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(max_length=250)),
                ('demo_video_link', models.URLField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Strategy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=80)),
                ('vision', models.CharField(max_length=250)),
                ('mission', models.CharField(max_length=250)),
                ('values', jsonfield.fields.JSONField()),
                ('logo', models.ImageField(upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TouchPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('note', models.TextField(max_length=1500)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
