from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('contact',views.contact,name="contact"),
    path('login',views.Login,name="login"),
    path('profile',views.Profile,name="profile"),
    path('logout',views.Logout,name="logout"),




    
]
