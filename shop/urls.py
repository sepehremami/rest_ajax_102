from django.urls import re_path
from . import views

app_name = 'shop'

urlpatterns = [

    re_path(r'api/products/$', views.ProductAPIListView.as_view(), name='products'),
]

