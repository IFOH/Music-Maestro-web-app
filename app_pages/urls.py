from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('contact/', views.contact, name = "contact"),
    path('account/', views.account, name = "account"),
    path('about/', views.about, name = "about"),
    path('login/', views.login, name = "login"),
    path('logout/', views.logout, name = "logout"),
    path('recommend-a-friend/', views.rec_friend, name = "rec_friend"),
]