from django.db import models
from users.models import GeneralModel
from crm.models import Channel, Lead, Product


class SalesScript(GeneralModel):
    name = models.TextField(max_length=80)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='product_sales_scripts')
    questions = models.ManyToManyField('Question')
    answers = models.ManyToManyField('Answer')


class Question(GeneralModel):
    prompt = models.CharField(max_length=1000)


class Answer(GeneralModel):
    case = models.CharField(max_length=80)
    prompt = models.CharField(max_length=1000)
    question = models.ForeignKey('Question', on_delete=models.CASCADE, null=True, related_name='question_answers')
    follow_up_questions = models.ManyToManyField('Question')


class TrainingMaterial(GeneralModel):
    name = models.TextField(max_length=80)
    notes_file = models.FileField()