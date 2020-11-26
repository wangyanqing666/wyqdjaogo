"""wyqDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url, include
from wyqapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wyqapp/', include('wyqapp.urls')),
    path(r'login/',views.login,name='login'),
    path(r'loginq/',views.loginq,name='loginq'),
    path(r'index',views.index),
    path(r'cutr',views.cutr),
    path(r'get_session/',views.get_session),
    path(r'set_session/',views.set_session),
    path(r'login1/',views.login1.as_view()),
    path(r'getname/',views.getname),
    path(r'setname/',views.setname),
    path(r'grades.html/',views.grades),
    path(r'loginadd',views.loginadd),
    path(r'logout/',views.logout),
    # path('wyq/', views.grades),
    path('alsk/', views.alsk),
    path('wyqlogin', views.wyqlogin),
    path('fenye/', views.fenye),
    path('wyqadduser', views.wyqadduser),

]
