# Generated by Django 3.1.3 on 2021-04-12 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crm', '0002_auto_20210412_1247'),
        ('users', '0001_initial'),
        ('salesed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingmaterial',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salesed_company_trainingmaterial', to='users.company'),
        ),
        migrations.AddField(
            model_name='trainingmaterial',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='salesscript',
            name='answers',
            field=models.ManyToManyField(to='salesed.Answer'),
        ),
        migrations.AddField(
            model_name='salesscript',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salesed_company_salesscript', to='users.company'),
        ),
        migrations.AddField(
            model_name='salesscript',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='salesscript',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_sales_scripts', to='crm.product'),
        ),
        migrations.AddField(
            model_name='salesscript',
            name='questions',
            field=models.ManyToManyField(to='salesed.Question'),
        ),
        migrations.AddField(
            model_name='question',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salesed_company_question', to='users.company'),
        ),
        migrations.AddField(
            model_name='question',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='answer',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salesed_company_answer', to='users.company'),
        ),
        migrations.AddField(
            model_name='answer',
            name='follow_up_questions',
            field=models.ManyToManyField(to='salesed.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_answers', to='salesed.question'),
        ),
    ]
