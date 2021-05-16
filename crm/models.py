from django.db import models
from jsonfield import JSONField

from hrm.models import Company, Project, Candidate
from users.models import GeneralModel, User


# from modeler.models import Modeler


class Product(GeneralModel):
    name = models.CharField(max_length=80)
    is_subscription_based = models.BooleanField(default=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, related_name='company_products')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, related_name='project_products')
    #modeler relation is used to relate courses to assessments (for admission and suggestions)
    #modeler = models.ForeignKey(Modeler, on_delete=models.CASCADE, null=True, blank=True, related_name='modeler_products')
    price = models.FloatField()
    availability_start_date = models.DateTimeField()
    availability_end_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(max_length=250)
    demo_video_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Lead(GeneralModel):
    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE, null=True, blank=True, related_name='candidate_lead')
    name = models.CharField(max_length=80)
    lastname = models.CharField(max_length=80)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    country = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    address = models.CharField(max_length=250, blank=True, null=True)
    postal_code = models.CharField(max_length=18, blank=True, null=True)
    street_number = models.CharField(max_length=10, blank=True, null=True)
    suite = models.CharField(max_length=25, blank=True, null=True)
    floor = models.CharField(max_length=25, blank=True, null=True)
    instagram = models.CharField(max_length=80, blank=True, null=True)
    acquired_at = models.DateTimeField(auto_now_add=True)
    acquired_by = models.ForeignKey(Candidate, on_delete=models.CASCADE, null=True, related_name='acquired_by_Leads')
    initial_capture_campaign = models.ForeignKey("Campaign", on_delete=models.CASCADE, null=True, blank=True,
                                                 related_name='initial_capture_campaign_leads')
    campaigns = models.ManyToManyField("Campaign", blank=True)
    lead_stage = models.ForeignKey("LeadStage", on_delete=models.CASCADE, null=True, related_name='lead_stage_leads')
    converted_lead_stage = models.ForeignKey("ConvertedLeadStage", on_delete=models.CASCADE, null=True,
                                             related_name='converted_lead_stage_leads')
    audience = models.ForeignKey('Audience', on_delete=models.CASCADE, null=True, related_name='audience_leads')
    interaction = models.ForeignKey('AudienceInteraction', on_delete=models.CASCADE, blank=True, null=True,
                                    related_name='interaction_leads')

    def __str__(self):
        return self.name


class LeadStage(GeneralModel):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class ConvertedLeadStage(GeneralModel):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Campaign(GeneralModel):
    campaign_name = models.CharField(max_length=80)
    product = models.ForeignKey("Product", on_delete=models.CASCADE, null=True, related_name='product_campaigns')
    roi = models.FloatField()
    budget = models.FloatField()

    def __str__(self):
        return self.campaign_name


class Funnel(GeneralModel):
    funnel_name = models.CharField(max_length=80)
    campaigns = models.ManyToManyField("Campaign")

    def __str__(self):
        return self.funnel_name


class FunnelComp(GeneralModel):
    name = models.CharField(max_length=80)
    funnel = models.ForeignKey("Funnel", on_delete=models.CASCADE, null=True, related_name='funnel_funnel_comps')
    channel = models.ForeignKey("Channel", on_delete=models.CASCADE, null=True, related_name='channel_funnel_comps')

    def __str__(self):
        return self.funnel.funnel_name + ' ' + self.channel.name


class Channel(GeneralModel):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Kpi(GeneralModel):
    reach = models.IntegerField()
    engagement = models.IntegerField()
    clicks = models.IntegerField()
    click_conversion = models.FloatField()
    cpc = models.FloatField()
    cpm = models.IntegerField()
    sales = models.FloatField()


class TouchPoint(GeneralModel):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, null=True, related_name='lead_touch_point')
    created_at = models.DateTimeField(auto_now_add=True)
    note = models.TextField(max_length=1500)

    def __str__(self):
        return self.lead.name


#########################################################################################
################################ Partner Sales Features #################################
#########################################################################################


class Partner(GeneralModel):
    name = models.CharField(max_length=80)
    partner_to_companies = models.ManyToManyField(Company)
    partners_company = models.OneToOneField(Company, on_delete=models.CASCADE, related_name='partners_company_partner')

    def __str__(self):
        return self.name


class PartnerCommissionRule(GeneralModel):
    percentage = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='product_partner_commission_rules')
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, null=True, related_name='partner_partner_commission_rules')

    def __str__(self):
        return self.partner.name + ' ' + self.product.name


class PartnerTeamMemberCommissionRule(GeneralModel):
    percentage = models.FloatField()
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, null=True, related_name='partner_partner_team_member_commission_rules')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='product_partner_team_members_commission_rules')
    team_member = models.ForeignKey(Candidate, on_delete=models.CASCADE, null=True, related_name='team_member_partner_team_member_commission_rules')

    def __str__(self):
        return self.partner.name + ' ' + self.product.name + ' ' + self.team_member.user.name


class Commission(GeneralModel):
    receiver = models.ForeignKey(Candidate, on_delete=models.CASCADE, null=True, related_name='candidate_commissions')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='product_commissions')
    STATUS_CHOICES = [
        ('paid', 'Paid'),
        ('pending-payout', 'Pending Payout'),
    ]
    status = models.CharField(max_length=25, choices = STATUS_CHOICES, default='5')

    def __str__(self):
        return self.receiver.user.name + ' ' + self.product.name


#########################################################################################
############################## Company Marketing Strategy ###############################
#########################################################################################


class Strategy(GeneralModel):
    name = models.TextField(max_length=80)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, related_name='company_strategies')
    vision = models.CharField(max_length=250)
    mission = models.CharField(max_length=250)
    values = JSONField()
    logo = models.ImageField()
    language = models.ManyToManyField('Language')
    culture_tone = models.ManyToManyField('CultureTone')
    color_palette = models.ManyToManyField('ColorPalette')
    audience = models.ManyToManyField('Audience')
    available_channels = models.ManyToManyField(Channel)

    def __str__(self):
        return self.name


class Audience(GeneralModel):
    name = models.TextField(max_length=80)
    description = models.CharField(max_length=500)
    found_at = models.ManyToManyField('AudienceCenter')
    interests = models.ManyToManyField('Interest')
    age_ranges = models.ManyToManyField('AudienceAgeRange')

    def __str__(self):
        return self.name


class AudienceCenter(GeneralModel):
    name = models.TextField(max_length=80)
    CENTER_TYPE_CHOICES = [
        ('location', 'Location'),
        ('platform', 'Platform'),
        ('influencer', 'Influencer'),
        ('influencer-type', 'Influencer Type'),
        ('thing', 'Thing'),
    ]
    center_type = models.CharField(max_length=25, choices = CENTER_TYPE_CHOICES, default='5')

    def __str__(self):
        return self.name


class Interest(GeneralModel):
    name = models.TextField(max_length=80)
    INTEREST_TYPE_CHOICES = [
        ('location', 'Location'),
        ('food', 'Food'),
        ('product', 'Product'),
        ('topic', 'Topic'),
        ('thing', 'Thing'),
    ]
    interest_type = models.CharField(max_length=12, choices = INTEREST_TYPE_CHOICES, default='5')

    def __str__(self):
        return self.name


class AudienceAgeRange(GeneralModel):
    AGE_RANGE_CHOICES = [
        ('0', '0-6'),
        ('1', '7-12'),
        ('2', '13-15'),
        ('3', '16-18'),
        ('4', '19-22'),
        ('5', '23-29'),
        ('6', '30-34'),
        ('7', '34-39'),
        ('8', '40-49'),
        ('9', '50-59'),
        ('10', '60-69'),
        ('11', '70-80'),
        ('12', '> 80'),
    ]
    age_range = models.CharField(max_length=12, choices = AGE_RANGE_CHOICES, default='5')

    def __str__(self):
        return self.age_range


class Language(GeneralModel):
    name = models.TextField(max_length=80)

    def __str__(self):
        return self.name


class CultureTone(GeneralModel):
    name = models.TextField(max_length=80)

    def __str__(self):
        return self.name


class ColorPalette(GeneralModel):
    code = models.TextField(max_length=7)


class AudienceInteraction(GeneralModel):
    # lead = models.ForeignKey('Lead', on_delete=models.CASCADE)
    last_purchase_date = models.DateTimeField()
    last_product_purchased = models.ForeignKey(Product, on_delete=models.CASCADE)
    last_page_visit = models.DateTimeField()
    last_email_open = models.CharField(max_length=100)
    last_touchpoint_date = models.DateTimeField()
    last_newsletter_signup = models.CharField(max_length=100)
    # purchased_product_combination = models.ForeignKey(Product, on_delete=models.CASCADE)
    specific_product_last_purchase_date = models.DateTimeField()


class PageVisit(GeneralModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    Page_visit_date = models.DateTimeField()
    page = models.ForeignKey(FunnelComp, on_delete=models.CASCADE)


class opendEmails(GeneralModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    # email = models.()   ??????????????????
    email_date = models.DateTimeField()
