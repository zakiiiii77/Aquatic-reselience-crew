from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from . models import Articles
# Create your views here.

@login_required(login_url="login")
def HomePage(request):
    return render(request, 'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not the same!!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect("login")

def index(request):
    return render(request, 'index.html')

def quiz(request):
    return render(request, 'quiz.html')

def art1(request):
    return render(request, 'Water_Cycle_Phases.html')

def Contact(request):
    return render(request, 'ContactUs.html')

def art2(request):
    return render(request, 'art2.html')

class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Articles
    template_name = 'search_results.html'
    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Articles.objects.filter(
            Q(Article_name__icontains=query) | Q(Article_number__icontains=query)
        )
        return object_list