from django.contrib import admin
from .models import UserProfile, Service, Transaction

# تسجيل النموذج Service مع تخصيص طريقة عرض البيانات في لوحة الإدارة
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'hours_required', 'created_at')  # تغيير 'hours' إلى 'hours_required'
    search_fields = ('title',)  # تمكين البحث عن الخدمات باستخدام العنوان
    list_filter = ('created_at',)  # إضافة فلتر لعرض الخدمات حسب تاريخ الإنشاء

# تسجيل النماذج الأخرى
admin.site.register(UserProfile)
admin.site.register(Transaction)


