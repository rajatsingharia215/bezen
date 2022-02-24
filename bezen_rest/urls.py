from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.addrecord,name="index"),
    path('addrecord/',views.addrecord,name="record"),
    path('schedule/',views.schedule,name="schedule"),
    path('getallrecords/media/images/<id>',views.get_processed_image,name="get_processed_image"),
    # path('addrecord/upload/',views.upload_img),
    path('getallrecordsjson/',views.getallrecordsjson),
    path('getallrecords/',views.getallrecords)


]