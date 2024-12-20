from django.shortcuts import render, get_object_or_404
from .models import Service  # استيراد نموذج الخدمة

# عرض قائمة بالخدمات
def service_list(request):
    services = Service.objects.all()  # جلب جميع الخدمات من قاعدة البيانات
    return render(request, 'services/service_list.html', {'services': services})

# عرض تفاصيل الخدمة
def service_detail(request, service_id):
    # الحصول على الخدمة باستخدام id (أو يمكنك استخدام slug إذا كنت تفضل ذلك)
    service = get_object_or_404(Service, id=service_id)
    
    # تمرير الخدمة إلى القالب
    return render(request, 'services/service_detail.html', {'service': service})
