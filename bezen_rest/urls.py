from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.addrecord,name="index"),
    path('addrecord/',views.addrecord,name="record"),
    # path('addrecord/upload/',views.upload_img),
    path('getallrecords/',views.getallrecords)


]