from django.urls import path

from campaign import views

urlpatterns = [
    path('', views.QuerySetRuleListView.as_view(), name='person_changelist'),
    path('add/', views.QuerySetRuleCreateView.as_view(), name='person_add'),
    path('<int:pk>/', views.QuerySetRuleUpdateView.as_view(), name='person_change'),

    path('test/', views.selector_view),

    path('selector/<str:pk_test>/', views.selector, name="selector"),
    path('create_query_set_rule/<str:pk>/', views.create_query_set_rule, name="create_query_set_rule"),
    path('ajax/load-secondchoices/', views.load_secondchoices, name='ajax_load_secondchoices'),
    path('ajax/load-thirdchoices/', views.load_thirdchoices, name='ajax_load_thirdchoices'),
]
