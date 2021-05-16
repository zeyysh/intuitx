from django.contrib import admin
import salesed.models as omodels
from users.admin import BaseModelAdmin

admin.site.register(omodels.SalesScript, BaseModelAdmin)
admin.site.register(omodels.Question, BaseModelAdmin)
admin.site.register(omodels.Answer, BaseModelAdmin)