"""
URL configuration for crudpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from crudapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_shoe/',views.saveshoes,name='add_shoe'),
    path('show_shoe/',views.getAllShoes,name='show_shoe'),
    path('update_shoe/',views.updateshoes,name='update_shoe'),
    path("show_shoe/edit/<int:sId>",views.getShoeById,name='edit'),
    path("show_shoe/delete/<int:sId>",views.deleteShoeById,name='delete')
]
