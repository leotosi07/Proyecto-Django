
class Carrito:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        else:
            self.carrito = carrito

def agregar (self,producto):
    id = str(producto.id)
    if id not in self.carrito.keys():
        self.carrito[id]= {
            'producto_id':producto.id,
            'nombre':producto.nombre,
            'precio':str(producto.precio),
            'cantidad':1
        }
    else:
        for key, value in self.carrito.item():
            if key == str(producto.id):
                value['cantidad'] = value['cantidad']+1
                self.guardar_carrito()
                break
    self.guardar_carrito()
    
def guardar_carrito(self):
    self.session['carrito'] = self.carrito
    self.session.modified = True
    
def eliminar(self,producto):
    id = str(producto.id)
    if id in self.carrito:
        del self.carrito[id]
        self.guardar_carrito()

def restar(self,producto):
        for key, value in self.carrito.item():
            if key == str(producto.id):
                value['cantidad'] = value['cantidad'] - 1
                if value['cantidad']<1:
                    self.eliminar(producto)
                    self.guardar_carrito()
                else:
                    self.guardar_carrito()
                break
            else:
                print('El producto no existe en el carrito')
                
def limpiar(self):
    self.session['carrito'] = {}
    self.session.modified = True
    
