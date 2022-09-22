from django.urls import path
from . import  views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('service/',views.service, name="service"),
    path('register',views.Singup , name = 'register')
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
