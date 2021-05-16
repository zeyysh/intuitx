"""assessmentservice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from feedback.views import messages
from filemanager import views as fviews
from users import views as uviews

# from django.views.decorators.csrf import csrf_exempt
# from asgiref.sync import sync_to_async


router = routers.DefaultRouter()
router.register('organizations', uviews.OrganizationViewSet)
router.register('users', uviews.UserViewSet, basename='user-list')
router.register('api/login', uviews.LoginView, basename='login')
# router.register(r'import-nodes-return-params-sheet',mviews.ImportNodesReturnParamsSheet, basename='import-nodes')
# router.register(r'import-links',mviews.ImportLinks, basename='import-links')
# router.register(r'import-unassigned-ipip-inputs',mviews.ImportUnassignedIpipInputs, basename='import-ipip')

messages.csrf_exempt = True
urlpatterns = [
    # Rest Api Route
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('campaign/', include('campaign.urls')),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    # path('account/logout/', uviews.LogoutView.as_view(), name='logout'),

    path('api/messages', messages),
    url(r'^uploads/form/$', fviews.model_form_upload, name='model_form_upload'),
    path("", include("feedback.urls")),
    path("", include("users.urls")),
    # url('', include('pwa.urls')),
]
