from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from Ecomerce.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',index,name='home'),
    path('index/',index),
    path('admin/', admin.site.urls),
    path('login/',CustomLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page=('home')),name='logout'),
    path('register/',register,name='register'),
    path('category/',category,name='category'),
    path(r'^shop/$',shop,name='shop'),
    path('about/',about,name='about'),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
