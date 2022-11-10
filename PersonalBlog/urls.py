"""PersonalBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path

from Blog.views import BlogHome, BlogPost, CreateBlog, Like
from Home.views import HomePage, Signup, Signout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage, name="Home"),
    path('Signup', Signup, name="Signup"),
    path('Signout', Signout, name="Signout"),
    path('Blog', BlogHome, name="BlogHome"),
    path('Blog/<slug:id>', BlogPost, name="BlogPost"),
    path('CreateBlog', CreateBlog, name="CreateBlog"),
    path("Like/<slug:ID>", Like)
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
