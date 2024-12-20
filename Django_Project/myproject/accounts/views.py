from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# عرض صفحة التسجيل
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # تسجيل الدخول تلقائيًا بعد التسجيل
            return redirect('home')  # توجيه المستخدم إلى الصفحة الرئيسية بعد التسجيل
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})
