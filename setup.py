import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'intuitx.settings')

import django
import pycountry

django.setup()
from django.contrib.auth.models import Group, Permission
from users.models import Organization
from crm.models import LeadStage, ConvertedLeadStage, Channel
from campaign.models import ThirdChoice
from django.apps import apps
from django.conf import settings

LEAD_STAGE_CHOICES = [
    ('Generated'),
    ('Contacted'),
    ('Contacted Us'),
    ('Presented'),
    ('Needs Follow Ups'),
    ('Converted'),
]
CONVERTED_LEAD_STAGE_CHOICES = [
    ('N/A'),
    ('Pending QA Survey'),
    ('Resell Potential'),
]
EXPOSURE_CHANNEL_CHOICES = [
    ('Google Ads'),
    ('Yektanet'),
    ('Tapsell'),
    ('Sheypoor'),
    ('Divar'),
    ('Evand'),
    ('Eseminar'),
    ('FarazSMS'),
    ('Jobinja'),
    ('Jobvision'),
    ('Mailchimp'),
    ('Facebook Ads'),
    ('Instagram Ads'),
    ('Instagram Influencers'),
    ('LinkedIn'),
    ('Blog'),
    ('Site'),
    ('Youtube/Aparat')
]
GROUPS = ['SuperAdmin',
          'HRSuperAdmin',
          'OrganizationSuperAdmin',
          'OrganizationSales_&_MarketingAdmin',
          'OrganizationHRAdmin',
          'Candidate',
          'HRPerson',
          'Sales_&_MarketingPerson',
          'reguser']
# models = apps.all_models['<app_name>']
# app_models = [model.__name__ for model in apps.get_models()] # comment
# apps = [app.app_label for app in settings.INSTALLED_APPS] # comment
# Company._meta.app_label
# Company._meta.model_name

GROUPS = {
    'SuperAdmin': [
        'add_user',
        'change_user',
        'delete_user',
        'view_user',
        'add_organization',
        'change_organization',
        'delete_organization',
        'view_organization'
    ],
    'HRSuperAdmin': [
        # '',
        # '',
        # ''
    ],
    'OrganizationSuperAdmin': [
        'add_orgazization',
        'change_orgazization',
        'view_orgazization',
        'add_company',
        'change_company',
        'delete_company',
        'view_company',
        'add_user',
        'change_user',
        'delete_user',
        'view_user',
        'add_team',
        'change_team',
        'delete_team',
        'view_team',
        'add_invite',
        'change_invite',
        'delete_invite',
        'view_invite',
        'add_strategy',
        'change_strategy',
        'delete_strategy',
        'view_strategy',
        'add_product',
        'change_product',
        'delete_product',
        'view_product',
        'view_project',
        'delete_project',
        'view_project',
        'change_project',
        'add_task',
        'view_kpi',

    ],
    'OrganizationSales_&_MarketingAdmin': [
        # '',
        # '',
        # ''
    ],
    'OrganizationHRAdmin': [
        # '',
        # '',
        # ''
    ],
    'Candidate': [
        'add_user',
        'change_user',
        'view_user',
        'add_invite',
        'view_invite',
        'view_company',
        'view_candidate',
        'view_product',
        'view_question',
        'view_answer',
        'add_answer',
        'add_document',
        'view_payment',
        'view_order',
        'view_expense',
    ],
    'HRPerson': [
        'view_project',
        'view_team',
        'add_team',
        'change_team',
        'delete_team',
        'view_resource',
        'add_resource',
        'change_resource',
        'delete_resource',
        'view_timelog',
        'add_timelog',
        'change_timelog',
        'delete_timelog',
        'view_candidate',
        'add_candidate',
        'change_candidate',
        'delete_candidate',
        'view_position',
        'add_position',
        'change_position',
        'delete_position',
        'view_milestone',
        'view_milestoneEntry',
        'view_milestoneTier',
        'view_task',
        'view_budget',
        'view_payroll',
        'dd_payroll',
        'change_payroll',
        'delete_payroll',
        'view_candidateSubmission',
    ],
    'Sales_&_MarketingPerson': [

    ],
    'reguser': [
        # '',
        # '',
        # ''
    ]
}

MODELS = ['user']

# for group in GROUPS:
#     new_group, created = Group.objects.get_or_create(name=group)
#     for permission in GROUPS[group]:
#         perm = Permission.objects.get(codename=permission) #name change to codename
#         new_group.permissions.add(perm)

# for choice in LEAD_STAGE_CHOICES:
#     LeadStage.objects.get_or_create(name=choice)

# for choice in CONVERTED_LEAD_STAGE_CHOICES:
#     ConvertedLeadStage.objects.get_or_create(name=choice)

# for choice in EXPOSURE_CHANNEL_CHOICES:
#     Channel.objects.get_or_create(name=choice)

# Organization.objects.get_or_create(name='intuitx', subdomain_prefix='paramind.cloud', active=True)

AUDIENCE_COUNTRY = [
    "China",
    "India",
    "United States",
    "Indonesia",
    "Brazil",
    "Nigeria",
    "Japan",
    "Russia",
    "Bangladesh",
    "Mexico",
    "Germany",
    "Philippines",
    "Turkey",
    "Vietnam",
    "Iran",
    'United Kingdom',
    'France',
    'Thailand',
    'Italy',
    'Egypt',
]

AUDIENCE_LANGUAGE = [
    'Arabic',
    'Bengali',
    'Bosnian',
    'Bulgarian',
    'Catalan',
    'Chinese',
    'Croatian ',
    'Czech ',
    'Danish',
    'Dutch ',
    'English',
    'Finnish',
    'French',
    'German',
    'Greek ',
    'Hebrew',
    'Hindi ',
    'Hungarian',
    'Indonesian',
    'Italian',
    'Japanese ',
    'Korean',
    'Latvian',
    'Macedonian',
    'Malay ',
    'Norwegian',
    'Persian',
    'Polish',
    'Portuguese',
    'Romanian ',
    'Russian',
    'Serbian',
    'Spanish',
    'Swedish',
    'Turkish',
    'Ukrainian',
]

INTEREST_TYPE = [
        'Location',
        'Food',
        'Product',
        'Topic',
        'Thing',
    ]

AGE_RANGE = [
        '0-6',
        '7-12',
        '13-15',
        '16-18',
        '19-22',
        '23-29',
        '30-34',
        '34-39',
        '40-49',
        '50-59',
        '60-69',
        '70-80',
        '> 80',
    ]

id = 1
for country in AUDIENCE_COUNTRY:
    ThirdChoice.objects.get_or_create(id=id, name=country, second_choice_id=14)
    id += 1

for language in AUDIENCE_LANGUAGE:
    ThirdChoice.objects.get_or_create(id=id, name=language, second_choice_id=15)
    id += 1

for agerange in AGE_RANGE:
    ThirdChoice.objects.get_or_create(id=id, name=agerange, second_choice_id=16)
    id += 1

for interest in INTEREST_TYPE:
    ThirdChoice.objects.get_or_create(id=id, name=interest, second_choice_id=17)
    id += 1