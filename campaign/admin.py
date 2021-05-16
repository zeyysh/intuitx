from django.contrib import admin

import campaign.models as cmodels

admin.site.register(cmodels.Selector)
admin.site.register(cmodels.SelectionProfile)
