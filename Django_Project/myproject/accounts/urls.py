from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # تسجيل الدخول
    path('login/', auth_views.LoginView.as_view(), name='login'),
    
    # تسجيل الخروج
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # التسجيل
    path('signup/', views.signup, name='signup'),

    
    # صفحات استعادة كلمة المرور
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    


]
