from django.db import models
from users.models import GeneralModel
from crm.models import Lead, Product, Company
from hrm.models import Candidate, Payroll
from users.models import User

class Order(GeneralModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, related_name='company_orders')
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, null=True, related_name='lead_orders')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user_orders')
    created_at = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('pending-payment', 'Pending Payment'),
        ('cancelled', 'Cancelled'),
        ('pending-delivery', 'Pending Delivery'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=20, choices = STATUS_CHOICES, default='placed')
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.lead.name


class Payment(GeneralModel):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, null=True, related_name='order_payments')
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()

    def __str__(self):
        return self.order


class Expense(GeneralModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, related_name='company_expenses')
    description = models.TextField(max_length=55)
    amount = models.FloatField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, related_name='category_expenses')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user_expenses')
    created_at = models.DateTimeField(auto_now_add=True)
    payroll = models.ForeignKey(Payroll, on_delete=models.CASCADE, null=True, related_name='payroll_expenses')

    def __str__(self):
        return self.description


class Category(GeneralModel):
    name = models.TextField(max_length=80)

    def __str__(self):
        return self.name
