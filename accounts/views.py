from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from .forms import SignUpForm, CustomLoginForm

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('upload_resume')
        
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('upload_resume')
    else:
        form = SignUpForm()
        
    return render(request, 'accounts/signup.html', {'form': form})


class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'accounts/login.html'