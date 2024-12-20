from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.service_list, name='service_list'),  # عرض جميع الخدمات
    path('service/<int:service_id>/', views.service_detail, name='service_detail'),  # عرض تفاصيل الخدمة
    path('', views.home, name='home'),  # الصفحة الرئيسية

]
