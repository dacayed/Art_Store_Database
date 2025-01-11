from django.contrib import admin
from django.urls import path , include
from . import views
from .models import Product , Review , Order
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:product_id>/', views.details, name='details'),

    path('<int:product_id>/add_review/', views.add_review, name='add_review'),

    path('register/', views.register, name='register'),

    path('<int:product_id>/add_order/', views.add_order, name='add_order'),

    path('<int:order_id>/delete_order', views.delete_order, name='delete_order'),

    path('order_list/', views.order_list, name='order_list'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)