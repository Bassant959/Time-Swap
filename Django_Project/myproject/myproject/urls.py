
from django.contrib import admin
from django.urls import path, include  # تأكد من استيراد 'include' لتضمين المسارات من تطبيقات أخرى

urlpatterns = [
    path('admin/', admin.site.urls),  # المسار الخاص بلوحة الإدارة
    path('accounts/', include('accounts.urls')),  # تضمين روابط المصادقة الخاصة بتطبيق 'accounts'
    path('services/', include('services.urls')),
]


