from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):

    return render(request, "proyectoWebAPP/home.html")






def tienda(request):

    return render(request, "proyectoWebAPP/tienda.html")






def contacto(request):

    return render(request, "proyectoWebAPP/contacto.html")