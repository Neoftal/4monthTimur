"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to posts. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function posts
    1. Add an import:  from my_app import posts
    2. Add a URL to urlpatterns:  path('', posts.home, name='home')
Class-based posts
    1. Add an import:  from other_app.posts import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from posts.views import hellow_view

from posts.views import goodbyw_view

from posts.views import data_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hellow_view),
    path('goodby/', goodbyw_view),
    path('now_date/', data_view)

]
