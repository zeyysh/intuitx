from django.db import models
from users.models import GeneralModel


class Document(GeneralModel):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)