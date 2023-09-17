from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Productos, Clientes, Vendedores

# Create your views here.



################### funciones  #########################

def cliente(req, nombre, apellido, dni, mail ):
    cliente = Clientes(nombre=nombre, apellido=apellido, dni=dni, mail=mail)
    cliente.save()
    return HttpResponse(f'''
    <p>Cliente: {cliente.nombre} - apellido: {cliente.apellido} creado con exito!</P>''')        

def producto(req, bodega, etiqueta, precio):
    producto = Productos(bodega=bodega, etiqueta=etiqueta, precio=precio)
    producto.delete()
    return HttpResponse(f'''
    <p>Bodega: {producto.bodega} - etiqueta: {producto.etiqueta} creado con exito!</P>''')  

def vendedor(req, nombre, apellido, legajo):
    vendedor = Vendedores(nombre=nombre, apellido=apellido, legajo=legajo)
    vendedor.save()
    return HttpResponse(f'''
    <p>Vendedor: {vendedor.nombre}{vendedor.apellido} creado con exito!</P>''')  

################### funciones agregar #########################


def agregar_producto(req):

    print('method', req.method)
    print('POST', req.POST)
    if req.method == 'POST':
        producto = Productos(bodega=req.POST["bodega"], etiqueta=req.POST["etiqueta"], precio=req.POST["precio"])
        producto.save()
        return render(req, "inicio.html")

    else:  
        return render(req, "agregar_producto.html")


def agregar_cliente(req):

    print('method', req.method)
    print('POST', req.POST)
    if req.method == 'POST':
        cliente = Clientes(nombre=req.POST["nombre"], apellido=req.POST["apellido"], dni=req.POST["dni"], mail=req.POST["mail"])
        cliente.save()
        return render(req, "inicio.html")

    else:  
        return render(req, "agregar_cliente.html")

def agregar_vendedor(req):

    print('method', req.method)
    print('POST', req.POST)
    if req.method == 'POST':
        vendedor = Vendedores(nombre=req.POST["nombre"], apellido=req.POST["apellido"], legajo=req.POST["legajo"])
        vendedor.save()
        return render(req, "inicio.html")

    else:  
        return render(req, "agregar_vendedor.html")
            
################### funciones listar #########################

def inicio(req):
    return render(req, "inicio.html")    

def listar_clientes(req):
    lista = Clientes.objects.all()
    return render(req, "listar_clientes.html", {"listar_clientes": lista})

def listar_productos(req):
    lista = Productos.objects.all()
    return render(req, "listar_productos.html", {"listar_productos": lista})

def listar_vendedores(req):
    lista = Vendedores.objects.all()
    return render(req, "listar_vendedores.html", {"listar_vendedores": lista})


################### funciones busqueda  #########################

def busquedaProducto(req):
    return render (req, "busquedaProducto.html")


def buscar(req: HttpRequest):

    if req.GET["bodega"]:
        bodega = req.GET["bodega"]
        productob = Productos.objects.filter(bodega__icontains = bodega)
        return render(req, "resultadoBusqueda.html", {"bodega": productob})

    else:
        return HttpResponse (f'no existe..')
    
################### funciones listar  #########################
 
def listarVendedores(req):
    Vendedor = Vendedores.objects.all
    return render(req, "listarVendedores.html", {"Vendedores" : Vendedor})