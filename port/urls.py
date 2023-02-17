from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.home, name= "home"),
    path('about', views.about, name= "about"),
    path('blog', views.blog, name= "blog"),
    path('contact', views.contact, name= "contact"),
    path('portfolio', views.portfolio, name= "portfolio"),
    
]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
