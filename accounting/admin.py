from django.contrib import admin
import accounting.models as amodels
from admin_helpers import AdminChangeLinksMixin
from users.admin import BaseModelAdmin


class OrderAdmin(AdminChangeLinksMixin, BaseModelAdmin):
    list_display = ('lead_link', 'user_link', 'status', 'created_at')
    list_filter = ('status', 'company')
    change_links = ('lead', 'company', 'user')
    filter_horizontal = ('products',)
    autocomplete_fields = ('lead', 'company', 'user')
    search_fields = ('lead__name', 'company__name')


class PaymentAdmin(AdminChangeLinksMixin, BaseModelAdmin):
    list_display = ('order_link', 'created_at', 'amount')
    list_filter = ('created_at',)
    change_links = ('order',)
    autocomplete_fields = ('order',)


class ExpenseAdmin(AdminChangeLinksMixin, BaseModelAdmin):
    list_display = ('company', 'category', 'created_at', 'amount')
    list_filter = ('created_at', 'category', 'company')
    change_links = ('order',)
    autocomplete_fields = ('company', 'category', 'user')
    search_fields = ('description',)


class CategoryAdmin(AdminChangeLinksMixin, BaseModelAdmin):
    list_display = ('name',)
    changelist_links = ('category_expenses',)
    search_fields = ('name',)


admin.site.register(amodels.Order, OrderAdmin)
admin.site.register(amodels.Payment, PaymentAdmin)
admin.site.register(amodels.Expense, ExpenseAdmin)
admin.site.register(amodels.Category, CategoryAdmin)