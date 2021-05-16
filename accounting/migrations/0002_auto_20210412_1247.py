# Generated by Django 3.1.3 on 2021-04-12 08:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('accounting', '0001_initial'),
        ('hrm', '0001_initial'),
        ('crm', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accounting_company_payment', to='users.company'),
        ),
        migrations.AddField(
            model_name='payment',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_payments', to='accounting.order'),
        ),
        migrations.AddField(
            model_name='payment',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='order',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_orders', to='users.company'),
        ),
        migrations.AddField(
            model_name='order',
            name='lead',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lead_orders', to='crm.lead'),
        ),
        migrations.AddField(
            model_name='order',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='crm.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_orders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='expense',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_expenses', to='accounting.category'),
        ),
        migrations.AddField(
            model_name='expense',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_expenses', to='users.company'),
        ),
        migrations.AddField(
            model_name='expense',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='expense',
            name='payroll',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payroll_expenses', to='hrm.payroll'),
        ),
        migrations.AddField(
            model_name='expense',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_expenses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='category',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accounting_company_category', to='users.company'),
        ),
        migrations.AddField(
            model_name='category',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
    ]
