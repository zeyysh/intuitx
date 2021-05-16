from django.forms import inlineformset_factory
from django.forms.formsets import formset_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from campaign.forms import QuerySetRuleForm, SelectorForm
from campaign.models import QuerySetRule, Selector, SecondChoice, ThirdChoice


class QuerySetRuleListView(ListView):
    model = QuerySetRule
    context_object_name = 'people'


class QuerySetRuleCreateView(CreateView):
    model = QuerySetRule
    form_class = QuerySetRuleForm
    success_url = reverse_lazy('QuerySetRule_changelist')


class QuerySetRuleUpdateView(UpdateView):
    model = QuerySetRule
    form_class = QuerySetRuleForm
    success_url = reverse_lazy('QuerySetRule_changelist')


def selector(request, pk_test):
    selector = Selector.objects.get(id=pk_test)

    query_set_rule = selector.order_set.all()
    query_set_rule_count = query_set_rule.count()

    context = {'selector': selector, 'query_set_rule': query_set_rule, 'query_set_rule_count': query_set_rule_count}
    return render(request, 'campaign/selector.html', context)


def create_query_set_rule(request, pk):
    query_set_rule_FormSet = inlineformset_factory(Selector, QuerySetRule, fields=(
        'selector', 'method_type', 'first_choice', 'second_choice', 'third_choice', 'field_name', 'lookup_type',
        'field_value'), extra=3)
    selector = Selector.objects.get(id=pk)
    formset = query_set_rule_FormSet(queryset=QuerySetRule.objects.none(), instance=selector)
    # form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        # form = OrderForm(request.POST)
        formset = query_set_rule_FormSet(request.POST, instance=selector)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'form': formset}
    return render(request, 'campaign/templates/campaign/querysetrule_form.html', context)


# def load_cities(request):
#     country_id = request.GET.get('country')
#     cities = City.objects.filter(country_id=country_id).order_by('name')
#     return render(request, 'hr/city_dropdown_list_options.html', {'cities': cities}

def selector_view(request):
    query_set_rule = formset_factory(QuerySetRuleForm)
    if request.method == 'POST':
        query_set_formset = query_set_rule(request.POST, prefix='query_set_formset')
        selector_form = SelectorForm(request.POST, prefix='selector_form')
        # validate your forms, etc
    else:
        selector_form = SelectorForm()
        query_set_formset = query_set_rule(prefix='phone_formset')
    return render(request, 'campaign/templates/campaign/selector.html', {'query_set_formset': query_set_formset})

def load_secondchoices(request):
    firstchoice_id = request.GET.get('first_choice')
    secondchoices = SecondChoice.objects.filter(first_choice_id=firstchoice_id).order_by('name')
    return render(request, 'campaign/secondchoice_dropdown_list_options.html', {'secondchoices': secondchoices})

def load_thirdchoices(request):
    secondchoice_id = request.GET.get('second_choice')
    thirdchoices = ThirdChoice.objects.filter(second_choice_id=secondchoice_id).order_by('name')
    return render(request, 'campaign/thirdchoice_dropdown_list_options.html', {'thirdchoices': thirdchoices})