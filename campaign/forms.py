from django import forms

from campaign.models import QuerySetRule, Selector
from campaign.models import SecondChoice, ThirdChoice

class QuerySetRuleForm(forms.ModelForm):
    third_choice = forms.MultipleChoiceField(choices = [(choice.pk, choice) for choice in ThirdChoice.objects.none()])
    
    class Meta:
        model = QuerySetRule
        fields = (
            'selector', 'method_type', 'first_choice', 'second_choice', 'third_choice', 'lookup_type',
            'field_value')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['second_choice'].queryset = SecondChoice.objects.none()


class SelectorForm(forms.ModelForm):
    class Meta:
        model = Selector
        fields = ('name', 'content', 'from_sender')

        # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['city'].queryset = City.objects.none()
    #
    #     if 'country' in self.data:
    #         try:
    #             country_id = int(self.data.get('country'))
    #             self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
    #         except (ValueError, TypeError):
    #             pass  # invalid input from the client; ignore and fallback to empty City queryset
    #     elif self.instance.pk:
    #         self.fields['city'].queryset = self.instance.country.city_set.order_by('name')