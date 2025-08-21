
from django.contrib import admin
from django.urls import path
from main import views   # import from main app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),           # homepage
    path('about/', views.about, name='about'),   # /about/
    path('contact/', views.contact, name='contact'), # /contact/
    path('projects/', views.projects, name='projects'), # /projects/
]
