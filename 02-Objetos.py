class Catalogo:
    productos = [] # atriburto de clase
    
    def agregar_producto(self, codigo, descripcion, cantidad, precio, imagen, proveedor):
        if self.consultar_producto(codigo):
            return False
        
        nuevo_producto = { #diccionario de datos
            'codigo': codigo,
            'descripcion': descripcion,
            'cantidad': cantidad,
            'precio': precio,
            'imagen': imagen,
            'proveedor': proveedor,
        }
        self.productos.append(nuevo_producto)
        return True  
    
    def consultar_producto(self, codigo):
        for producto in self.productos:
            if producto['codigo'] == codigo: # si es igual lo encontro
                return producto
        return False 
    
    def listar_productos(self):
        print("_"*50)
        for producto in self.productos:
            print(f"codigo.......: {producto['codigo']}")
            print(f"descripcion..: {producto['descripcion']}")
            print(f"cantidad.....: {producto['cantidad']}")
            print(f"precio.......: {producto['precio']}")
            print(f"imagen.......: {producto['imagen']}")
            print(f"proveedor....: {producto['proveedor']}")
            print("_"*50)

    def modificar_producto(self, codigo, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen, nuevo_proveedor):
        for producto in self.productos:
            if producto['codigo'] == codigo:
                producto['descripcion'] = nueva_descripcion
                producto['cantidad'] = nueva_cantidad
                producto['precio'] = nuevo_precio
                producto['imagen'] = nueva_imagen
                producto['proveedor'] = nuevo_proveedor
                return True
            return False    
    def eliminar_producto(self, codigo):
        for producto in self.productos:
            if producto['codigo'] == codigo:
                self.productos.remove(producto)
                return True
        return False 

    def mostrar_producto(self, codigo):
        producto = self.consultar_producto(codigo) 
        if producto:
            print("_"*50)
            print(f"codigo.......: {producto['codigo']}")
            print(f"descripcion..: {producto['descripcion']}")
            print(f"cantidad.....: {producto['cantidad']}")
            print(f"precio.......: {producto['precio']}")
            print(f"imagen.......: {producto['imagen']}")
            print(f"proveedor....: {producto['proveedor']}")
            print("_"*50)


#programa principal

# Agregamos productos a la lista:
catalogo = Catalogo()
catalogo.agregar_producto(1, 'Teclado USB 101 teclas', 10, 4500, 'teclado.jpg',
101)
catalogo.agregar_producto(2, 'Mouse USB 3 botones', 5, 2500, 'mouse.jpg', 102)  

catalogo.mostrar_producto(2)

