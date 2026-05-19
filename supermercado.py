def menu_supermercado():
    print("==============================")
    print("SUPERMERCADO PYTHON MARKET")
    print("==============================")

    print("1. Cargar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto por código")
    print("4. Ordenar productos por precio")
    print("5. Mostrar producto con menor stock")
    print("6. Calcular valor total del inventario")
    print("7. Salir")

    opcion = int(input("Ingresa una opcion: "))
    return opcion

def buscar_elemento(lista,elemento):
    esta = False
    for i in range(len(lista)):
        if lista[i] == elemento:
            esta = True
    return esta

def cargar_producto(codigos,productos,precios,stocks):
    cant = int(input("Ingrese una cantidad de productos a cargar: "))
    while cant <= 0:
        print("Por favor, ingrese una cantidad válida")
        cant = int("Ingrese una cantidad de productos a cargar: ")

    while cant > 0:    
        codigo = int(input("Ingresa el código del producto: "))
        while buscar_elemento(codigos,codigo) == True:
            print("Por favor, ingresa un código que no esté cargado")
            codigo = int(input("Ingresa el código del producto: "))
        codigos.append(codigo)

        nombre = input("Ingresa el nombre del producto: ")
        productos.append(nombre)

        precio = int(input("Ingresar el precio del producto: "))
        while precio <= 0:
            print("Por favor, ingresa un precio positivo")
            precio = int(input("Ingresar el precio del producto: "))
        precios.append(precio)

        stock = int(input("Ingresar cantidad de productos de este tipo a agregar: "))
        while precio <= 0:
            print("Por favor, ingresa un stock positivo")
            stock = int(input("Ingresar cantidad de productos de este tipo a agregar: "))
        stocks.append(stock)
        cant -= 1
    print("Productos cargados correctamente")

def mostrar_productos(codigos,productos,precios,stocks):
    if productos == []:
        print("No hay productos cargados")
    else:
        print(f"Productos: {productos}")
        print(f"Codigos: {codigos}")
        print(f"Precios: {precios}")
        print(f"Stocks: {stocks}")

def buscar_producto_por_codigo(codigos,productos):
    codigo = int(input("Introduce un codigo: "))
    while buscar_elemento(codigos,codigo) == False:
        print("Por favor, introduce un codigo cargado anteriormente")
        codigo = int(input("Introduce un codigo: "))
    
    for i in range(len(codigos)):
        if codigos[i] == codigo:
            print(f"El producto del codigo {codigo} es {productos[i]}")


def ordenar_productos_por_precio(productos,precios,stocks,codigos):
    for i in range(len(productos)):
        for j in range(i+1,len(productos)-1):
            if precios[i] > precios[j]:
                producto_con_precio_mayor = productos[i]
                productos[i] = productos[j]
                productos[j] = producto_con_precio_mayor
                precio_mayor = precios[i]
                precios[i] = precios[j]
                precios[j] = precio_mayor
                stock_con_precio_mayor = stocks[i]
                stocks[i] = stocks[j]
                stocks[j] = stock_con_precio_mayor
                codigo_con_precio_mayor = codigos[i]
                codigos[i] = codigos[j]
                codigos[j] =codigo_con_precio_mayor

    print("Productos ordenados por precio")
    print(f"Productos: {productos}")
    print(f"Precios: {precios}")
    
    
def mostrar_producto_con_menor_stock(productos,stocks):
    producto_con_menor_stock = productos[0]
    menor_stock = stocks[0]
    for i in range(1,len(productos)):
        if stocks[i] < menor_stock:
            producto_con_menor_stock = productos[i]
            menor_stock = stocks[i]
    print(f"El producto con menor stock es {producto_con_menor_stock}, que tiene {menor_stock}")

def calcular_total_del_inventario(productos,precios,stocks):
    total = 0
    for i in range(0,len(precios)):
        total_del_producto = precios[i]*stocks[i]
        total += precios[i]*stocks[i]
        print(f"El precio total de {productos[i]} es {total_del_producto}")
    print(f"El precio total del inventario es: {total}")         


def main():
    codigos = []
    productos = []
    precios = []
    stocks = []

    opcion = menu_supermercado()
    while opcion != 7:
        match opcion:
            case 1:
                cargar_producto(codigos,productos,precios,stocks)
            case 2:
                mostrar_productos(codigos,productos,precios,stocks)
            case 3:
                buscar_producto_por_codigo(codigos,productos)
            case 4:
                ordenar_productos_por_precio(productos,precios,stocks,codigos)
            case 5:
                mostrar_producto_con_menor_stock(productos,stocks)
            case 6:
                calcular_total_del_inventario(productos,precios,stocks)
            case _:
                print("Por favor, ingresa una opción válida(del 1 al 7)")
        opcion = menu_supermercado()
    print("Saliste del supermercado")

main()