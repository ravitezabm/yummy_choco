
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index),
    path('reg',views.reg),
    path('login',views.login),
    path('details',views.details),
    path('edit',views.edit),
    path('update',views.update),
    path('delete',views.delete),
    path('chocoupload',views.chocoupload),
    path('chocoview',views.chocoview),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)