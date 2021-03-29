from django.shortcuts import render, redirect
from .models import Articulo, Usuario
from .forms import ArticuloForm, UsuarioForm

def firstView(request):
    return render(request, 'index.html')

def articulo(request):
    articulos = Articulo.objects.all()
    ctx = {
        'articulos' : articulos
    }
    return render(request, 'articulos.html', ctx)

def createArticulo(request):
    if request.method == 'GET':
        form = ArticuloForm()
        ctx = {
            'form': form
        }
    else:
        form = ArticuloForm(request.POST)
        ctx = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('articulos')

    return render(request, 'manage_articulos.html', ctx)

def editArticulo (request, id):
    articulo = Articulo.objects.get (id = id)
    if request.method == 'GET':
        form = ArticuloForm(instance= articulo)
        ctx = {
            'form' : form
        }
    else:
        form = ArticuloForm(request.POST, instance= articulo)
        ctx = {
            'form' : form
        }
        if form.is_valid():
            form.save()
            return redirect('articulos')

    return  render(request, 'manage_articulos.html', ctx)

def deleteArticulo(request, id):
    articulo = Articulo.objects.get(id = id)
    articulo.delete()
    return redirect('articulos')

def usuario(request):
    usuarios = Usuario.objects.all()
    ctx = {
        'usuarios' : usuarios
    }
    return render(request, 'usuarios.html', ctx)

def createUsuario(request):
    if request.method == 'GET':
        form = UsuarioForm()
        ctx = {
            'form': form
        }
    else:
        form = UsuarioForm(request.POST)
        ctx = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('usuario')

    return render(request, 'manage_usuarios.html', ctx)

def editUsuario (request, id):
    usuario = Usuario.objects.get (id = id)
    if request.method == 'GET':
        form = UsuarioForm(instance= usuario)
        ctx = {
            'form' : form
        }
    else:
        form = UsuarioForm(request.POST, instance= usuario)
        ctx = {
            'form' : form
        }
        if form.is_valid():
            form.save()
            return redirect('usuario')

    return  render(request, 'manage_usuarios.html', ctx)

def deleteUsuario(request, id):
    usuario = Usuario.objects.get(id = id)
    usuario.delete()
    return redirect('usuario')


