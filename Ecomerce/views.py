from django.shortcuts import render,redirect
from django.conf import settings #tambahkan import settings agar bisa mengakses env
from Ecomerce.models import Category
from django.contrib import messages

# Create your views here.
from Ecomerce.forms import LoginForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    form_class = LoginForm

def index(request):
    #variable
    categorys = Category.objects.filter()[:3]

    konteks = {
        'categorys':categorys
    }

    return render(request,'index.html',konteks)

def register(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'success created account, please login')
            return redirect('login')
        else:
            messages.error(request,'error 404')
            return redirect('register')
    else:
        form = UserCreationForm()
        konteks = {
            'form':form
        }
    return render(request,'register.html',konteks)

# page ecomerce

def category(request):
    categorys = Category.objects.all()

    konteks = {
        'categorys':categorys
    }

    return render(request,'category.html',konteks)

def shop(request):
    return render(request,'shop.html')

