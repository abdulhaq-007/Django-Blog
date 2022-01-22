from django.shortcuts import render
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, "index.html")
    else:
        form = UserRegisterForm()
    return render(request, "account/register.html", {"form":form})

class LoginView(LoginView):
    template_name = 'account/login.html'  
    success_url = '/'

class LogoutView(LogoutView):
    template_name = 'account/logout.html'

@login_required(login_url="/account/login/")
def profile(request):
    u = request.user
    user = Profile.objects.get(user=u)
    if user:
        return render(request, "account/detail.html", {"user": user})
    else:
        return render(request, "account/detail.html")



def edit(request,user_id):
    if request.method == "POST":
        profile_edit_form = ProfileEditForm(request.POST)
        if profile_edit_form.is_valid():
            profile_edit_form.save()
            return redirect("/account/profile/")
    else:

        profile_edit_form = ProfileEditForm()

    context = {
        "form":profile_edit_form
    }
    return render(request, "account/edit.html", context)