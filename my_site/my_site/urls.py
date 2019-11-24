"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from p_library import views
# from p_library.urls import urlpatterns as library_urls
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index/', views.index),
    path('index/book_increment/', views.book_increment),
    path('index/book_decrement/', views.book_decrement),
    path('redaction/', views.redaction, name='redaction'),
    path('', include('p_library.urls', namespace='p_library')),
    path('rent/', views.rent, name='rent'),
    path('rent/rent_delete/', views.rent_delete),

]

# urlpatterns += library_urls