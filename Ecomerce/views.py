from django.shortcuts import render, redirect, HttpResponse
# tambahkan import settings agar bisa mengakses env
from django.conf import settings
from Ecomerce.models import Category, Product
from django.contrib import messages
from Ecomerce.forms import LoginForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from Ecomerce.filters import OrderProduct, SearchProduct
from Ecomerce.cart import Cart

# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    form_class = LoginForm


def index(request):
    # variable
    categorys = Category.objects.filter()[:3]
    products = Product.objects.all()
    dataSearch = SearchProduct(request.GET, queryset=products)
    cart = Cart(request)

    konteks = {
        'categorys': categorys,
        'dataSearch': dataSearch,
        'cart': cart,
    }

    return render(request, 'index.html', konteks)


def register(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'success created account, please login')
            return redirect('login')
        else:
            messages.error(request, 'error 404')
            return redirect('register')
    else:
        form = UserCreationForm()
        konteks = {
            'form': form
        }
    return render(request, 'register.html', konteks)

# page ecomerce


def category(request):
    categorys = Category.objects.all()
    products = Product.objects.all()
    dataSearch = SearchProduct(request.GET, queryset=products)
    cart = Cart(request)

    konteks = {
        'categorys': categorys,
        'cart': cart,
    }

    return render(request, 'category.html', konteks)


def shop(request):
    categorys = Category.objects.all()
    products = Product.objects.all()
    dataFilter = OrderProduct(request.GET, queryset=products)
    dataSearch = SearchProduct(request.GET, queryset=products)
    cart = Cart(request)

    konteks = {
        'categorys': categorys,
        'products': products,
        'dataFilter': dataFilter,
        'dataSearch': dataSearch,
        'cart': cart,
    }
    return render(request, 'shop.html', konteks)


def about(request):
    return render(request, 'about.html')


def detail_product(request, id_product):
    product = Product.objects.get(id=id_product)
    products = Product.objects.all()
    dataSearch = SearchProduct(request.GET, queryset=products)
    cart = Cart(request)

    konteks = {
        'product': product,
        'dataSearch': dataSearch,
        'cart': cart
    }

    return render(request, 'detail_product.html', konteks)

# this function for cart


@login_required(login_url=settings.LOGIN_URL)
def cart(request):
    cart = Cart(request)
    products = Product.objects.all()
    dataSearch = SearchProduct(request.GET, queryset=products)

    konteks = {
        'cart': cart,
        'dataSearch': dataSearch
    }
    return render(request, 'cart_detail.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def cart_add(request, id_product):
    cart = Cart(request)
    quantity = request.GET.get('qty')
    product = Product.objects.get(id=id_product)

    cart.add(product, product.price, quantity)
    return redirect('home')


@login_required(login_url=settings.LOGIN_URL)
def cart_remove(request, id_product):
    product = Product.objects.get(id=id_product)
    cart = Cart(request)
    cart.remove(product)
    return redirect('cart')


@login_required(login_url=settings.LOGIN_URL)
def cart_increment(request, id_product):
    product = Product.objects.get(id=id_product)
    quantity = 1
    cart = Cart(request)
    cart.increment(product, quantity)
    return redirect('cart')


@login_required(login_url=settings.LOGIN_URL)
def cart_decrement(request, id_product):
    product = Product.objects.get(id=id_product)
    quantity = 1
    cart = Cart(request)
    cart.decrement(product, quantity)
    return redirect('cart')
