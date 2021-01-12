from django.shortcuts import redirect, HttpResponse


def indice(Request):
    return HttpResponse("marcador de posición para luego mostrar una lista de todos los blogs")

def nuevo (Request):
    return HttpResponse("marcador de posición para mostrar un nuevo formulario para crear un nuevo blog")

def create(request):
	return redirect("/")

def show (Request, my_val):
    return HttpResponse(f"marcador de posicion para mostrar el numero de blog: {my_val}")

def editar (Request):
    return HttpResponse("marcador de posición para editar el blog")

def destruir (Request):
    return redirect("/")


# Create your views here.
