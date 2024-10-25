from tkinter import *
from tkinter import ttk

def abrir_tienda(self):
        
    self.tienda = Toplevel(self.raiz)
    self.raiz.title("Tienda")
    self.tienda.resizable(0,0)
    
    self.cantidades = {
        "pocion"                  : IntVar(value=0),
        "super pocion"            : IntVar(value=0),
        "eter"                    : IntVar(value=0),
        "elixir"                  : IntVar(value=0),
        "teclado"                 : IntVar(value=0),
        "teclado gaming"          : IntVar(value=0),
        "teclado 60"              : IntVar(value=0),
        "libro coding"            : IntVar(value=0),
        "libro coding avanzado"   : IntVar(value=0),
        "libro algoritmica divina": IntVar(value=0)
    }
    
    self.precios = {
        "pocion"                  : IntVar(value=3),
        "super pocion"            : IntVar(value=9),
        "eter"                    : IntVar(value=3),
        "elixir"                  : IntVar(value=18),
        "teclado"                 : IntVar(value=6),
        "teclado gaming"          : IntVar(value=15),
        "teclado 60"              : IntVar(value=33),
        "libro coding"            : IntVar(value=5),
        "libro coding avanzado"   : IntVar(value=13),
        "libro algoritmica divina": IntVar(value=38)
    }
    
    self.precio_total = IntVar(value=0)
    
    self.marco_imagen = ttk.Frame(self.tienda)
    self.marco_productos = ttk.Frame(self.tienda)
    
    goron = PhotoImage(file="MediGoron.png")
    
    def calcular():
            
        total = 0
            
        for descripcion, unidades in self.cantidades.items():
            precio = self.precios[descripcion].get()
            total = total + unidades.get()*precio
        
        self.precio_total.set(total)
    
    self.dependiente = ttk.Label(self.marco_imagen, image=goron)
    
    self.etiq1        = ttk.Label(self.marco_productos, text='Consumibles: ')
    self.consumible1  = ttk.Label(self.marco_productos, text='Pocion')
    self.consumible2  = ttk.Label(self.marco_productos, text='Super pocion')
    self.consumible3  = ttk.Label(self.marco_productos, text='Eter')
    self.consumible4  = ttk.Label(self.marco_productos, text='Elixir')
    self.pocion       = ttk.Spinbox(self.marco_productos, from_= 0, to= 99, wrap=True, textvariable=self.cantidades["pocion"], state='readonly', command=calcular)
    self.super_pocion = ttk.Spinbox(self.marco_productos, from_= 0, to= 99, wrap=True, textvariable=self.cantidades["super pocion"], state='readonly', command=calcular)
    self.eter         = ttk.Spinbox(self.marco_productos, from_= 0, to= 99, wrap=True, textvariable=self.cantidades["eter"], state='readonly', command=calcular)
    self.elixir       = ttk.Spinbox(self.marco_productos, from_= 0, to= 99, wrap=True, textvariable=self.cantidades["elixir"], state='readonly', command=calcular)
    
    self.etiq2                    = ttk.Label(self.marco_productos, text='Armas: ')
    self.arma1                    = ttk.Label(self.marco_productos, text='Teclado')
    self.arma2                    = ttk.Label(self.marco_productos, text='Teclado Gaming')
    self.arma3                    = ttk.Label(self.marco_productos, text='Teclado 60%')
    self.arma4                    = ttk.Label(self.marco_productos, text='Libro Coding')
    self.arma5                    = ttk.Label(self.marco_productos, text='Libro Coding avanzado')
    self.arma6                    = ttk.Label(self.marco_productos, text='Libro Algoritmica Divina')
    self.teclado                  = ttk.Spinbox(self.marco_productos, from_=0, to=1, textvariable=self.cantidades["teclado"], state='readonly', command=calcular)
    self.teclado_gaming           = ttk.Spinbox(self.marco_productos, from_=0, to=1, textvariable=self.cantidades["teclado gaming"], state='readonly', command=calcular)
    self.teclado_60               = ttk.Spinbox(self.marco_productos, from_=0, to=1, textvariable=self.cantidades["teclado 60"], state='readonly', command=calcular)
    self.libro_coding             = ttk.Spinbox(self.marco_productos, from_=0, to=1, textvariable=self.cantidades["libro coding"], state='readonly', command=calcular)
    self.libro_coding_avanzado    = ttk.Spinbox(self.marco_productos, from_=0, to=1, textvariable=self.cantidades["libro coding avanzado"], state='readonly', command=calcular)
    self.libro_algoritmica_divina = ttk.Spinbox(self.marco_productos, from_=0, to=1, textvariable=self.cantidades["libro algoritmica divina"], state='readonly', command=calcular)
    
    self.etiq3 = ttk.Label(self.marco_productos, text="Total: ")
    self.total = ttk.Label(self.marco_productos, textvariable=self.precio_total, borderwidth=5, anchor="e")
    
    self.cerrar = ttk.Button(self.tienda, text='cerrar', command=self.tienda.destroy)
    
    self.marco_imagen.grid(column=0, row=0)
    self.dependiente.grid(column=0, row=0)
    self.marco_productos.grid(column=0, row=1)
    self.etiq1.grid(column=0, row=2)          
    self.consumible1.grid(column=0, row=3)  
    self.consumible2.grid(column=0, row=4)  
    self.consumible3.grid(column=0, row=5)  
    self.consumible4.grid(column=0, row=6)  
    self.pocion.grid(column=1, row=3)          
    self.super_pocion.grid(column=1, row=4) 
    self.eter.grid(column=1, row=5)              
    self.elixir.grid(column=1, row=6)          
            
    self.etiq2.grid(column=0, row=11)        
    self.arma1.grid(column=0, row=12)        
    self.arma2.grid(column=0, row=13)        
    self.arma3.grid(column=0, row=14)        
    self.arma4.grid(column=0, row=15)        
    self.arma5.grid(column=0, row=16)        
    self.arma6.grid(column=0, row=17)        
    self.teclado.grid(column=1, row=12)                   
    self.teclado_gaming.grid(column=1, row=13)           
    self.teclado_60.grid(column=1, row=14)               
    self.libro_coding.grid(column=1, row=15)             
    self.libro_coding_avanzado.grid(column=1, row=16)    
    self.libro_algoritmica_divina.grid(column=1, row=17) 
    
    self.etiq3.grid(column=0, row=18)        
    self.total.grid(column=1, row=18)  
    
    self.cerrar.grid(column=0, row=19)
    
    self.tienda.transient(master=self.raiz)
    
    self.tienda.grab_set()
    
    self.raiz.wait_window(self.tienda)