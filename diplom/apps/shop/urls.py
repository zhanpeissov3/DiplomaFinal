from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('services/', views.get_services, name='get_services'),
    path('send_message/', views.send_message, name='send_message'),
    path('send_service/', views.send_service, name='send_service'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    url(r'^(?P<category_slug>[-\w]+)/$',
        views.product_list,
        name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='product_detail'),
]
