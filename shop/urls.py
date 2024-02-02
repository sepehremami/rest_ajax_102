from django.urls import re_path, path
from . import views

app_name = 'shop'

urlpatterns = [

    re_path(r'api/products/$', views.ProductAPIListView.as_view(), name='products'),
    re_path(r'api/orders/$', views.OrderAPIListCreateView.as_view(), name='orders'),
    path("api/order/<str:id>/", views.OrderAPIRetriveView.as_view(), name='order'),
    re_path(r'api/addresses/$', views.AddressAPIListCreateView.as_view(), name='addresses')
]
