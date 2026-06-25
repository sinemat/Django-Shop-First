from django.contrib.auth import views as auth_views
from accounts.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View

class LoginView(auth_views.LoginView):
    template_name = "accounts/login.html"
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    
# usually means you're accessing Django's LogoutView with a GET request, but newer Django versions require POST for logout by default.    
# class LogoutView(auth_views.LogoutView):
#     print(666)
#     pass

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')