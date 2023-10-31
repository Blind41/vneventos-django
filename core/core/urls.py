from django.contrib import admin
from django.urls import path
from vneventos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('send_mail/', views.form, name="send_mail")
]
