from datetime import datetime

import timedelta as djangotimedelta
from django.db import models

from crm.models import Campaign, AudienceAgeRange, Interest
from users.models import GeneralModel


class SelectionProfile(GeneralModel):
    name = models.TextField(max_length=80)
    selector = models.ForeignKey('Selector', on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Selector(GeneralModel):
    name = models.TextField(max_length=80)
    content = models.TextField(max_length=300, null=True, blank=True)
    from_sender = models.TextField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Languages(GeneralModel):
    AUDIENCE_LANGUAGE_CHOICES = [
        ('english', 'English'),
        ('russian', 'Russian'),
        ('turkish', 'Turkish'),

    ]
    Audience_language = models.CharField(max_length=25, choices=AUDIENCE_LANGUAGE_CHOICES, default='27')


class Location(GeneralModel):
    AUDIENCE_LOCATION_CHOICES = [
        ('afghanistan', 'Afghanistan'),
        ('albania', 'Albania'),
        ('algeria', 'Algeria'),
    ]
    Audience_location = models.CharField(max_length=50, choices=AUDIENCE_LOCATION_CHOICES, default='113')


METHOD_TYPES = (
    ('filter', 'Include'),
    ('exclude', 'Exclude'),
)

LOOKUP_TYPES = (
    ('exact', 'exactly'),
    ('iexact', 'exactly (case insensitive)'),
    ('contains', 'contains'),
    ('icontains', 'contains (case insensitive)'),
    ('regex', 'regex'),
    ('iregex', 'contains (case insensitive)'),
    ('gt', 'greater than'),
    ('gte', 'greater than or equal to'),
    ('lt', 'less than'),
    ('lte', 'less than or equal to'),
    ('startswith', 'starts with'),
    ('endswith', 'starts with'),
    ('istartswith', 'ends with (case insensitive)'),
    ('iendswith', 'ends with (case insensitive)'),
)

Lead_Ownership = (
    ('project', 'Project'),
    ('company', 'Company'),
    ('allLead', 'All Lead'),
)

ATTRIBUTE = (
    ('age_range', 'age range'),
    ('interests', 'interests'),
    ('location', 'location'),
    ('language', 'language'),
)

INTERACTION = (
    ('last_purchase_date', 'last purchase date'),
    ('last_product_purchased', 'last product purchased'),
    ('last_page_visit', 'last page visit'),
    ('last_email_open', 'last email open'),
    ('last_touchpoint_date', 'last touchpoint date'),
    ('last_newsletter_signup', 'last newsletter signup'),
    ('purchased_product_combination', 'purchased product combination'),
    ('specific_product_last_purchase_date', 'specific product last purchase date'),
)


class FirstChoice(models.Model):
    name = models.CharField(max_length=130)

    def __str__(self):
        return self.name


class SecondChoice(models.Model):
    first_choice = models.ForeignKey('FirstChoice', on_delete=models.CASCADE)
    name = models.CharField(max_length=130)

    def __str__(self):
        return self.name


class ThirdChoice(models.Model):
    name = models.CharField(max_length=130)
    second_choice = models.ForeignKey('SecondChoice', on_delete=models.CASCADE)



class QuerySetRule(models.Model):
    selector = models.ForeignKey('Selector', related_name='queryset_rules', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    lastchanged = models.DateTimeField(auto_now=True)
    method_type = models.CharField(max_length=12, default='filter', choices=METHOD_TYPES)
    first_choice = models.ForeignKey('FirstChoice', on_delete=models.SET_NULL, null=True)
    second_choice = models.ForeignKey('SecondChoice', on_delete=models.SET_NULL, null=True)
    third_choice = models.ForeignKey('ThirdChoice', on_delete=models.SET_NULL, null=True)
    field_name = models.CharField(max_length=128, verbose_name='Field name of Selector')
    lookup_type = models.CharField(max_length=12, default='exact', choices=LOOKUP_TYPES)
    field_value = models.CharField(max_length=255,
                                   help_text=('Can be anything from a number, to a string. Or, do ' +
                                              '`now-7 days` or `today+3 days` for fancy timedelta.'))

    # def clean(self):
    #     User = get_user_model()
    #     try:
    #         self.apply(User.objects.all())
    #     except Exception as e:
    #         raise ValidationError(
    #             '%s raised trying to apply rule: %s' % (type(e).__name__, e))

    @property
    def annotated_field_name(self):
        field_name = self.field_name
        if field_name.endswith('__count'):
            agg, _, _ = field_name.rpartition('__')
            field_name = 'num_%s' % agg.replace('__', '_')

        return field_name

    def apply_any_annotation(self, qs):
        if self.field_name.endswith('__count'):
            field_name = self.annotated_field_name
            agg, _, _ = self.field_name.rpartition('__')
            qs = qs.annotate(**{field_name: models.Count(agg, distinct=True)})
        return qs

    def filter_kwargs(self, qs, now=datetime.now):
        # Support Count() as m2m__count
        field_name = self.annotated_field_name
        field_name = '__'.join([field_name, self.lookup_type])
        field_value = self.field_value

        # set time deltas and dates
        if self.field_value.startswith('now-'):
            field_value = self.field_value.replace('now-', '')
            field_value = now() - djangotimedelta.parse(field_value)
        elif self.field_value.startswith('now+'):
            field_value = self.field_value.replace('now+', '')
            field_value = now() + djangotimedelta.parse(field_value)
        elif self.field_value.startswith('today-'):
            field_value = self.field_value.replace('today-', '')
            field_value = now().date() - djangotimedelta.parse(field_value)
        elif self.field_value.startswith('today+'):
            field_value = self.field_value.replace('today+', '')
            field_value = now().date() + djangotimedelta.parse(field_value)

        # F expressions
        if self.field_value.startswith('F_'):
            field_value = self.field_value.replace('F_', '')
            field_value = models.F(field_value)

        # set booleans
        if self.field_value == 'True':
            field_value = True
        if self.field_value == 'False':
            field_value = False

        kwargs = {field_name: field_value}

        return kwargs

    def apply(self, qs, now=datetime.now):

        kwargs = self.filter_kwargs(qs, now)
        qs = self.apply_any_annotation(qs)

        if self.method_type == 'filter':
            return qs.filter(**kwargs)
        elif self.method_type == 'exclude':
            return qs.exclude(**kwargs)

        # catch as default
        return qs.filter(**kwargs)
