#from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import login
from django.conf.urls import url, include
from django.urls import path, re_path
#from django.conf import settings
#from django.conf.urls.static import static
from .import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'mensajes',views.MensajeView)



urlpatterns = [
    #index
    url(r'^index',views.index,name="index"),
    url(r'^api/',include(router.urls)),

    #log
    #url(r'^$', views.login_view,name="login_view"),
    url(r'^login',views.login_view,name="login_view"),
    url(r'^logout/$',views.logout_view,name="logout"),

    #menu
    url(r'^archivo/',views.archivo,name="archivo"),
    url(r'^contraparte/$',views.contraparte,name="contraparte"),
    url(r'^estado/$',views.estado,name="estado"),
    url(r'^portafolio/$',views.portafolio,name="portafolio"),
    url(r'^producto/$',views.producto,name="producto"),
    url(r'^trader/$',views.trader,name="trader"),
    url(r'^sistema/$',views.sistema,name="sistema"),
    url(r'^register/$',views.register,name="register"),
    url(r'^esperar/$',views.esperar,name="esperar")


]
urlpatterns += router.urls

"""
if settings.DEBUG:
        urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""
