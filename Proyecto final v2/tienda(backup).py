from tkinter import *
from tkinter import ttk

class Tienda():
    def __init__(self) -> None:
        
        self.raiz = Tk()
        self.raiz.geometry("480x360")
        self.raiz.title("Tienda")
        
        self.marco_imagen = ttk.Frame(self.raiz)
        self.marco_productos = ttk.Frame(self.raiz)
        
        goron = PhotoImage(file="MediGoron.png")
        
        self.dependiente = ttk.Label(self.marco_imagen, image=goron)
        
        self.etiq1 = ttk.Label(self.marco_productos, text="Consumibles: ")
        self.consumible1 = ttk.Checkbutton(self.marco_productos, text='Pocion')
        self.consumible2 = ttk.Checkbutton(self.marco_productos, text='Super pocion')
        self.consumible3 = ttk.Checkbutton(self.marco_productos, text='Eter')
        self.consumible4 = ttk.Checkbutton(self.marco_productos, text='Elixir')
        self.pocion =       ttk.Spinbox(self.marco_productos, from_= 0, to= 99, wrap=True, state='readonly')
        self.super_pocion = ttk.Spinbox(self.marco_productos, from_= 0, to= 99, wrap=True, state='readonly')
        self.eter =         ttk.Spinbox(self.marco_productos, from_= 0, to= 99, wrap=True, state='readonly')
        self.elixir =       ttk.Spinbox(self.marco_productos, from_= 0, to= 99, wrap=True, state='readonly')
        
        self.etiq2 = ttk.Label(self.marco_productos, text="Armas: ")
        self.arma1 = ttk.Checkbutton(self.marco_productos, text='Teclado')
        self.arma2 = ttk.Checkbutton(self.marco_productos, text='Teclado Gaming')
        self.arma3 = ttk.Checkbutton(self.marco_productos, text='Teclado 60%')
        self.arma4 = ttk.Checkbutton(self.marco_productos, text='Libro Coding')
        self.arma5 = ttk.Checkbutton(self.marco_productos, text='Libro Coding avanzado')
        self.arma6 = ttk.Checkbutton(self.marco_productos, text='Libro Algoritmica Divina')
        self.teclado =                  ttk.Spinbox(self.marco_productos, from_=0, to=1, state='readonly')
        self.teclado_gaming =           ttk.Spinbox(self.marco_productos, from_=0, to=1, state='readonly')
        self.teclado_60 =               ttk.Spinbox(self.marco_productos, from_=0, to=1, state='readonly')
        self.libro_coding =             ttk.Spinbox(self.marco_productos, from_=0, to=1, state='readonly')
        self.libro_coding_avanzado =    ttk.Spinbox(self.marco_productos, from_=0, to=1, state='readonly')
        self.libro_algoritmica_divina = ttk.Spinbox(self.marco_productos, from_=0, to=1, state='readonly')
        
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
        
        self.raiz.mainloop()
        
def main():
    pantalla = Tienda()
    return

if __name__ == '__main__':
    main()