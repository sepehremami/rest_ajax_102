from django.urls import re_path
from . import views

urlpatterns = [

    re_path(r'api/products/$', views.ProductAPIListView.as_view()),
]

