from django.db.models import Q

from campaign.models import Selector
from crm.models import Lead


class Select:

    def __init__(self, selector_name, campaign_name):
        self.campaign_name = campaign_name
        self.selector_name = selector_name

    def get_lead(self):
        selector = Selector.objects.get(name=self.selector_name)
        leads = Lead.objects.filter(
            Q(language=selector.language)
        )
