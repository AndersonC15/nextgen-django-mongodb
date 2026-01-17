from django.shortcuts import render, redirect
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["nextgen_db"]

# Definición de todas las colecciones
productos_col = db["producto"]
empleados_col = db["empleado"]
marcas_col = db["marca"]
pedidos_col = db["pedido"]
sucursales_col = db["sucursal"]

def inicio(request):
    return render(request, "inicio.html")

def lista_productos(request):
    productos = list(productos_col.find().sort("id_producto", 1))
    return render(request, "productos.html", {"productos": productos})

def get_next_id(colleccion, campo_id):
    last = colleccion.find_one(sort=[(campo_id, -1)])
    if last and campo_id in last:
        return int(last[campo_id]) + 1
    return 1
def crear_producto(request):
    if request.method == "POST":
        nuevo_id = get_next_id(productos_col, "id_producto")
        nuevo = {
            "id_producto": nuevo_id,
            "nombre": request.POST.get("nombre"),
            "descripcion": request.POST.get("descripcion"),
            "stock": int(request.POST.get("stock", 0)),
            "precio_unitario": float(request.POST.get("precio_unitario", 0.0)),
            "id_marca": int(request.POST.get("id_marca", 1)),
            "id_categoria": int(request.POST.get("id_categoria", 1)),
        }
        productos_col.insert_one(nuevo)
        return redirect("lista_productos")
    return render(request, "producto_form.html")

def editar_producto(request, id):
    id_entero = int(id)
    if request.method == "POST":
        productos_col.update_one(
            {"id_producto": id_entero}, 
            {"$set": {
                "nombre": request.POST.get("nombre"),
                "descripcion": request.POST.get("descripcion"),
                "stock": int(request.POST.get("stock", 0)),
                "precio_unitario": float(request.POST.get("precio_unitario", 0.0)),
                "id_marca": int(request.POST.get("id_marca", 1)),
                "id_categoria": int(request.POST.get("id_categoria", 1)),
            }}
        )
        return redirect("lista_productos")
    producto = productos_col.find_one({"id_producto": id_entero})
    return render(request, "editar_producto.html", {"producto": producto})

def eliminar_producto(request, id):
    productos_col.delete_one({"id_producto": int(id)})
    return redirect("lista_productos")

# --- EMPLEADOS ---
def lista_empleados(request):
    empleados = list(empleados_col.find().sort("id_empleado", 1))
    return render(request, "empleados.html", {"empleados": empleados})

def crear_empleado(request):
    if request.method == "POST":
        nuevo = {
            "id_empleado": get_next_id(empleados_col, "id_empleado"),
            "nombre": request.POST.get("nombre"),
            "apellido": request.POST.get("apellido"),
            "puesto": request.POST.get("puesto")
        }
        empleados_col.insert_one(nuevo)
        return redirect("lista_empleados")
    return render(request, "empleado_form.html")

def editar_empleado(request, id):
    id_entero = int(id)
    if request.method == "POST":
        empleados_col.update_one(
            {"id_empleado": id_entero},
            {"$set": {
                "nombre": request.POST.get("nombre"),
                "apellido": request.POST.get("apellido"),
                "puesto": request.POST.get("puesto")
            }}
        )
        return redirect("lista_empleados")
    empleado = empleados_col.find_one({"id_empleado": id_entero})
    return render(request, "empleado_form.html", {"empleado": empleado})

def eliminar_empleado(request, id):
    empleados_col.delete_one({"id_empleado": int(id)})
    return redirect("lista_empleados")

# --- MARCAS ---
def lista_marcas(request):
    marcas = list(marcas_col.find().sort("id_marca", 1))
    return render(request, "marcas.html", {"marcas": marcas})

def crear_marca(request):
    if request.method == "POST":
        nuevo = {
            "id_marca": get_next_id(marcas_col, "id_marca"), # Genera ID automático
            "nombre_marca": request.POST.get("nombre_marca")
        }
        marcas_col.insert_one(nuevo)
        return redirect("lista_marcas")
    return render(request, "marca_form.html")

def eliminar_marca(request, id):
    marcas_col.delete_one({"id_marca": int(id)})
    return redirect("lista_marcas")

# --- SUCURSALES ---
def lista_sucursales(request):
    sucursales = list(sucursales_col.find().sort("id_sucursal", 1))
    return render(request, "sucursales.html", {"sucursales": sucursales})

def crear_sucursal(request):
    if request.method == "POST":
        nuevo = {
            "id_sucursal": get_next_id(sucursales_col, "id_sucursal"), # Genera ID automático
            "nombre": request.POST.get("nombre"),
            "ciudad": request.POST.get("ciudad"),
            "direccion": request.POST.get("direccion"),
            "telefono": request.POST.get("telefono")
        }
        sucursales_col.insert_one(nuevo)
        return redirect("lista_sucursales")
    return render(request, "sucursal_form.html")

def editar_sucursal(request, id):
    # 'sucursales_col' debe ser el nombre de tu variable de coleccion de mongo
    sucursal = sucursales_col.find_one({"id_sucursal": int(id)})
    if request.method == "POST":
        sucursales_col.update_one(
            {"id_sucursal": int(id)},
            {"$set": {
                "nombre": request.POST.get('nombre'),
                "ciudad": request.POST.get('ciudad'),
                "direccion": request.POST.get('direccion'),
                "telefono": request.POST.get('telefono'),
            }}
        )
        return redirect('lista_sucursales')
    return render(request, "sucursal_form.html", {"sucursal": sucursal})

def eliminar_sucursal(request, id):
    sucursales_col.delete_one({"id_sucursal": int(id)})
    return redirect("lista_sucursales")

# --- PEDIDOS ---
def lista_pedidos(request):
    pedidos = list(pedidos_col.find().sort("id_pedido", 1))
    return render(request, "pedidos.html", {"pedidos": pedidos})

def eliminar_pedido(request, id):
    pedidos_col.delete_one({"id_pedido": int(id)})
    return redirect("lista_pedidos")
def crear_pedido(request):
    if request.method == "POST":
        from datetime import datetime
        nuevo = {
            "id_pedido": get_next_id(pedidos_col, "id_pedido"),
            "fecha_hora": datetime.now(),
            "metodo_pago": request.POST.get("metodo_pago"),
            "productos": []  # Se crea vacío para que no de error
        }
        pedidos_col.insert_one(nuevo)
        return redirect("lista_pedidos")
    return render(request, "pedido_form.html")