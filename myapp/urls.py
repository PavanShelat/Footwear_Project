"""
URL configuration for myproject2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('men/', views.men, name='men'),
    path('women/', views.women, name='women'),
    path('addToWishlist/', views.addToWishlist, name='addToWishlist'),
    path('orderComplete/', views.orderComplete, name='orderComplete'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cpass/', views.cpass, name='cpass'),
    path('fpass/', views.fpass, name='fpass'),
    path('otp/', views.otp, name='otp'),
    path('newpass/', views.newpass, name='newpass'),
    path('profile/', views.profile, name='profile'),
    path('sindex/', views.sindex, name='sindex'),
    path('sadd_details/', views.sadd_details, name='sadd_details'),
    path('viewprod/', views.viewprod, name='viewprod'),
    path('spdetails/<int:pk>', views.spdetails, name='spdetails'),
    path('spupdate/<int:pk>', views.spupdate, name='spupdate'),
    path('spdelete/<int:pk>', views.spdelete, name='spdelete'),
    path('pdetails/<int:pk>', views.pdetails, name='pdetails'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('addwish/<int:pk>', views.addwish, name='addwish'),
    path('delwish/<int:pk>', views.delwish, name='delwish'),
    path('addcart/<int:pk>', views.addcart, name='addcart'),
    path('cart/', views.cart, name='cart'),
    path('dcart/<int:pk>', views.dcart, name='dcart'),
    path('changeqty/<int:pk>', views.changeqty, name='changeqty'),
    path('payment-success/', views.payment_success, name='payment_success'),

]