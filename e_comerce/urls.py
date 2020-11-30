from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from Ecomerce.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name='home'),
    path('index/', index),
    path('admin/', admin.site.urls),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page=('home')), name='logout'),
    path('register/', register, name='register'),
    path('category/', category, name='category'),
    path(r'^shop/$', shop, name='shop'),
    path('about/', about, name='about'),
    path('shop/detail-product/<int:id_product>',
         detail_product, name='detail-product'),
    path('cart/', cart, name='cart'),
    path('cart/cart-remove/<int:id_product>',
         cart_remove, name='cart-remove'),
    path('cart/cart-add/<int:id_product>', cart_add, name='cart-add'),
    path('cart/cart-increment/<int:id_product>',
         cart_increment, name='cart-increment'),
    path('cart/cart-decrement/<int:id_product>',
         cart_decrement, name='cart-decrement'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
