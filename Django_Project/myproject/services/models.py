from django.db import models
from django.contrib.auth.models import User

# نموذج يمثل الملف الشخصي للمستخدم
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # ربط بمستخدم Django الافتراضي
    hours_balance = models.PositiveIntegerField(default=0)  # رصيد الساعات
    bio = models.TextField(blank=True)  # وصف مختصر
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)


    def __str__(self):
        return f"{self.user.username} - Balance: {self.hours_balance} hours"

# نموذج يمثل الخدمات التي يقدمها المستخدمون
class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # صاحب الخدمة
    title = models.CharField(max_length=100)  # عنوان الخدمة
    description = models.TextField()  # وصف الخدمة
    hours_required = models.PositiveIntegerField()  # عدد الساعات المطلوبة للخدمة
    created_at = models.DateTimeField(auto_now_add=True)  # تاريخ الإضافة

    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('completed', 'Completed')], default='active')


    def __str__(self):
        return f"{self.title} by {self.user.username} - {self.hours_required} hours"

# نموذج يمثل التبادلات الزمنية بين المستخدمين
class Transaction(models.Model):
    from_user = models.ForeignKey(User, related_name='sent_transactions', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='received_transactions', on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)  # الخدمة المقدمة
    hours_exchanged = models.PositiveIntegerField()  # عدد الساعات المتبادلة
    timestamp = models.DateTimeField(auto_now_add=True)  #تاريخ التبادل

    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='pending')

    transaction_id = models.CharField(max_length=100, unique=True)


    def __str__(self):
        return f"{self.from_user.username} → {self.to_user.username} : {self.hours_exchanged} hours"
    
   # تحديث رصيد الساعات بناءً على المعاملات
    def update_balance(self):
        # جمع جميع الساعات التي أرسلها المستخدم (المعاملات المرسلة)
        self.hours_balance = self.sent_transactions.aggregate(Sum('hours_exchanged'))['hours_exchanged__sum'] or 0
        self.save()
