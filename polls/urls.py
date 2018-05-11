#from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import (
    login, logout, password_reset, password_reset_done, password_reset_confirm,
    password_reset_complete
)

from django.conf.urls import url, include
from django.urls import path, re_path
from django.views.generic.base import RedirectView
#from django.conf import settings
#from django.conf.urls.static import static
from .import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'mensajes',views.MensajeView)



urlpatterns = [
    #index
    url(r'^index/$',views.index,name="index"),
    url(r'^api/',include(router.urls)),

    #log
    url(r'^$', views.login_view,name="login_view"),
    url(r'^login/$',views.login_view,name="login_view"),
    url(r'^logout/$',views.logout_view,name="logout"),

    #menu
    url(r'^archivo/$',views.archivo,name="archivo"),
    url(r'^trader/$',views.trader,name="trader"),
    url(r'^register/$',views.register,name="register"),
    url(r'^perfil/$',views.perfil,name="perfil"),

    url(r'^password/$',views.password,name="password"),
    url(r'^error/$',views.error,name="error"),
    url(r'^contraparte/$',views.contraparte,name="contraparte"),
    url(r'^estado/$',views.estado,name="estado"),
    url(r'^portafolio/$',views.portafolio,name="portafolio"),
    url(r'^producto/$',views.producto,name="producto"),
    url(r'^sistema/$',views.sistema,name="sistema"),
    url(r'^permiso/$',views.permiso,name="permiso"),
    #url(r'^parMoneda/$',views.parMoneda,name="parMoneda"),
    #url(r'^info/$',views.info,name="info"),

    #Manual
    url(r'^media/Manual.pdf$',views.manual,name="manual"),

    #password
    url(r'^reset-password/$', password_reset, {'template_name': 'reset_password.html', 'post_reset_redirect': 'password_reset_done', 'email_template_name': 'reset_password_email.html'}, name='reset-password'),
    url(r'^reset-password/done/$', password_reset_done, {'template_name': 'reset_password_done.html'}, name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'template_name': 'reset_password_confirm.html', 'post_reset_redirect': 'password_reset_complete'}, name='password_reset_confirm'),
    url(r'^reset-password/complete/$', password_reset_complete,{'template_name': 'reset_password_complete.html'}, name='password_reset_complete'),
    #controlar errores#    url(r'^.*$', RedirectView.as_view(pattern_name='error', permanent=False))
]
urlpatterns += router.urls

"""
if settings.DEBUG:
        urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""
