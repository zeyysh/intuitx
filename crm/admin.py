from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

import crm.models as cmodels
from admin_helpers import AdminChangeLinksMixin
from users.admin import BaseModelAdmin

admin.site.site_header = "Rastava - Admin Panel"


class ProductAdmin(BaseModelAdmin):
    list_display = ('name', 'description', 'price', 'is_subscription_based', 'project_link')
    list_filter = ('availability_start_date', 'availability_end_date', 'is_subscription_based', 'company')
    search_fields = ('name', 'company', 'project')
    autocomplete_fields = ('company', 'project')
    list_editable = ('is_subscription_based',)

    def project_link(self, campaign):
        url = reverse("admin:hrm_project_change", args=[campaign.project.id])
        link = '<a href="%s">%s</a>' % (url, campaign.project.name)
        return mark_safe(link)
    project_link.short_description = 'Project'


class LeadAdmin(AdminChangeLinksMixin, BaseModelAdmin):
    list_display = ('name', 'lastname', 'phone', 'lead_stage', 'converted_lead_stage', 'initial_capture_campaign_link')
    list_editable = ('lastname', 'lead_stage', 'converted_lead_stage', 'phone')
    list_filter = ('lead_touch_point__created_at', 'acquired_at', 'initial_capture_campaign', 'lead_stage', 'converted_lead_stage')
    filter_horizontal = ('campaigns',)
    autocomplete_fields = ('initial_capture_campaign',)
    search_fields = ('name', 'lastname', 'phone', 'email',)
    changelist_links = ('lead_touch_point',)
    #list_select_related = ('initial_capture_campaign',)

    #actions = ['make_published']

    #def make_published(self, request, queryset):
    #    queryset.update(status='p')
    #make_published.short_description = "Mark selected stories as published"

    def initial_capture_campaign_link(self, lead):
        url = reverse("admin:crm_campaign_change", args=[lead.initial_capture_campaign.id])
        link = '<a href="%s">%s</a>' % (url, lead.initial_capture_campaign.campaign_name)
        return mark_safe(link)
    initial_capture_campaign_link.short_description = 'Capture Campaign'


class CampaignAdmin(BaseModelAdmin):
    list_display = ('campaign_name', 'roi', 'budget', 'product_link')
    search_fields = ('campaign_name',)
    list_filter = ('roi', 'budget')
    autocomplete_fields = ('product',)

    def product_link(self, campaign):
        url = reverse("admin:crm_product_change", args=[campaign.product.id])
        link = '<a href="%s">%s</a>' % (url, campaign.product.name)
        return mark_safe(link)
    product_link.short_description = 'Product'


class FunnelAdmin(AdminChangeLinksMixin, BaseModelAdmin):
    list_display = ['funnel_name', 'funnel_funnel_comps_link']
    changelist_links = ['funnel_funnel_comps',]
    list_filter = ('campaigns', 'funnel_funnel_comps')
    filter_horizontal = ('campaigns',)
    search_fields = ('funnel_name', 'campaigns')


class FunnelCompAdmin(AdminChangeLinksMixin, BaseModelAdmin):
    list_display = ['name', 'channel_link', 'funnel_link']
    change_links = ['funnel', 'channel',]
    autocomplete_fields = ('channel', 'funnel')


class ChannelAdmin(AdminChangeLinksMixin, BaseModelAdmin):
    list_display = ['name', 'channel_funnel_comps_link']
    changelist_links = ['channel_funnel_comps',]
    search_fields = ('name',)


class KpiAdmin(BaseModelAdmin):
    pass


class TouchPointAdmin(AdminChangeLinksMixin, BaseModelAdmin):
    list_display = ['lead_link', 'created_at']
    change_links = ['lead',]
    list_filter = ('created_at', 'lead__lead_stage')
    autocomplete_fields = ('lead',)


class PartnerAdmin(AdminChangeLinksMixin, BaseModelAdmin):
    list_display = ['name',]
    filter_horizontal = ('partner_to_companies',)
    autocomplete_fields = ('partners_company',)
    search_fields = ('name',)
    list_filter = ('partner_to_companies',)


class PartnerCommissionRuleAdmin(AdminChangeLinksMixin, BaseModelAdmin):
    list_display = ['partner_link', 'percentage', 'product_link']
    changelist_links = ('partner', 'product')
    autocomplete_fields = ('partner', 'product')
    list_filter = ('product', 'partner')
    search_fields = ('partner__name', 'product__name')


class PartnerTeamMemberCommissionRuleAdmin(AdminChangeLinksMixin, BaseModelAdmin):
    list_display = ['partner_link', 'percentage', 'product_link', 'team_member_link']
    changelist_links = ('partner', 'product', 'team_member')
    autocomplete_fields = ('partner', 'product', 'team_member')
    list_filter = ('product', 'partner')
    search_fields = ('partner__name', 'product__name', 'team_member__user__name')


class CommissionAdmin(AdminChangeLinksMixin, BaseModelAdmin):
    list_display = ['receiver_link', 'product_link', 'status']
    changelist_links = ('receiver', 'product')
    autocomplete_fields = ('receiver', 'product')
    list_filter = ('product', 'status')
    list_editable = ('status',)
    search_fields = ('receiver__user__name', 'product__name')


admin.site.register(cmodels.Product, ProductAdmin)
admin.site.register(cmodels.Lead, LeadAdmin)
admin.site.register(cmodels.Campaign, CampaignAdmin)
admin.site.register(cmodels.Funnel, FunnelAdmin)
admin.site.register(cmodels.FunnelComp, FunnelCompAdmin)
admin.site.register(cmodels.Channel, ChannelAdmin)
admin.site.register(cmodels.Kpi)
admin.site.register(cmodels.ConvertedLeadStage)
admin.site.register(cmodels.LeadStage)
admin.site.register(cmodels.TouchPoint, TouchPointAdmin)

admin.site.register(cmodels.Partner, PartnerAdmin)
admin.site.register(cmodels.PartnerCommissionRule, PartnerCommissionRuleAdmin)
admin.site.register(cmodels.PartnerTeamMemberCommissionRule, PartnerTeamMemberCommissionRuleAdmin)
admin.site.register(cmodels.Commission, CommissionAdmin)

admin.site.register(cmodels.Strategy)
admin.site.register(cmodels.Audience)
admin.site.register(cmodels.AudienceCenter)
admin.site.register(cmodels.AudienceAgeRange)
admin.site.register(cmodels.Interest)
admin.site.register(cmodels.Language)
admin.site.register(cmodels.CultureTone)
admin.site.register(cmodels.ColorPalette)
admin.site.register(cmodels.PageVisit)
