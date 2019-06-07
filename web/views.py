from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as auth_login

# Create your views here.
def mostrarInicio(request):
    return render(request, 'inicio.html')

def mostrarLogin(request):
    return render(request, 'login.html')

def mostrarRegistro(request):
    return render(request, 'registro.html')

def mostrarServicio(request):
    return render(request, 'servicio.html')

def mostrarCuenta(request):
    return render(request, 'cuenta.html')

def registrarUser(request):
    # DATOS TOMADOS ATRAVES DEL FORMULARIO
    nombre = request.POST.get('registro_nombre','')
    email = request.POST.get('registro_email','')
    contraseña = request.POST.get('registro_contraseña','')
    primernombre = request.POST.get('registro_primernombre','')
    segundonombre = request.POST.get('registro_segundonombre','')

    # CREACION DEL OBJETO
    user = User.objects.create_user(username = nombre, email = email, password = contraseña, first_name = primernombre, last_name = segundonombre)
    user.save()

    return redirect('mostrarLogin')


def iniciarSesion(request):
    password = request.POST.get('login_contraseña', '')
    username = request.POST.get('login_usuario','')

    usuario = authenticate(request, username = username, password = password)

    if usuario is not None:
        auth_login(request, usuario)
        return redirect('mostrarInicio')
    else:
        return redirect('mostrarLogin')

def cerrarSesion(request):
    logout(request)
    return redirect('mostrarInicio')
