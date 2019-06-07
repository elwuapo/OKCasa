from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # INICIO
    path('', views.mostrarInicio, name="mostrarInicio"),

    # REGISTRO
    path('registro', views.mostrarRegistro, name="mostrarRegistro"),
    path('registro/registrar', views.registrarUser, name="registrarUser"),

    # LOGIN
    path('login', views.mostrarLogin, name="mostrarLogin"),
    path('login/iniciarSesion', views.iniciarSesion, name="iniciarSesion"),

    # SERVICIOS
    path('servicio', views.mostrarServicio, name="mostrarServicio"),

    # CUENTA
    path('cuenta', views.mostrarCuenta, name="mostrarCuenta"),

] + static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
