from django.urls import path
from django.urls.resolvers import URLPattern
import main1.views as views

urlpatterns = [
    path('', views.view_index, name = 'index'),

]
