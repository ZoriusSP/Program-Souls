from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import json, os
from Tienda import abrir_tienda

#función encargada de redimensionar las imagenes de los bosses y el prota
def redimensionar_imagenes(imagen, x, y):
    #se debe pasar al método resize tuplas
    return imagen.resize((x, y))

class PantallaPrincipal():
    def __init__(self) -> None:
        
        #creación del mapa principal
        self.raiz = Tk()
        self.raiz.geometry("720x480")
        self.raiz.title("Mapa Principal")
        self.raiz.resizable(0,0)
        
        #Fondo
        self.imagen_fondo = PhotoImage(file="escenario.png")
        self.fondo = ttk.Label(self.raiz, image=self.imagen_fondo)
        self.fondo.place(x = 0, y = 0)
        
        #dimensiones fijas del prota independientemente de las dimensiones de la imagen ubicada en el json del personaje
        self.x_prota = 30
        self.y_prota = 30
        
        #limitación para que el prota no se mueve más allá de las dimensiones de la ventana
        self.x_max_prota = 720 - self.x_prota
        self.y_max_prota = 480 - self.y_prota

        #proceso de redimensión de la imagen y asignación de esta al label del prota
        self.prota = Image.open("link.gif")
        self.prota_redimensionado = redimensionar_imagenes(self.prota, self.x_prota, self.y_prota)
        self.prota_final = ImageTk.PhotoImage(self.prota_redimensionado)
        self.machango = ttk.Label(self.raiz, image=self.prota_final)
        self.machango.place(x = 320, y = 210)
        
        #se establece el foco en el prota para que su ubicación pueda ser modificada más adelante
        self.machango.focus_set()
        
        #enlazamos los eventos del teclado a la función que hará el movimiento
        self.machango.bind("<Key>", self.movimiento)
        
        self.comprar = ttk.Button(self.raiz, text='Comprar', command=self.abrir_tienda, width=10)
        
        #ocultamos el boton
        self.comprar.place_forget()
        
        self.raiz.mainloop()
        
    def movimiento(self, evento):
        
        #obtenemos las coordenadas x e y del prota para poder ser modificadas 
        coordenadas = self.machango.winfo_geometry()
        coordenadas = coordenadas.split("+")
        coord_x = int(coordenadas[1])
        coord_y = int(coordenadas[2])
        
        #modificamos las coordenadas en función de la tecla que se haya pulsado
        if evento.keysym == "w" or evento.keysym == "Up":
            coord_y -= 5
            if coord_y <= 0:
                coord_y += 5
            
            elif (coord_x >= 580) and (coord_y <= 80):
                coord_y += 5
                
            elif (605 <= coord_x <=665) and (100 <= coord_y <=165):
                coord_y += 5
                
            self.machango.place(x = coord_x, y = coord_y)
            
            print(coord_x, coord_y)
        elif evento.keysym == "s" or evento.keysym == "Down":
            coord_y += 5
            if coord_y >= self.y_max_prota:
                coord_y -= 5
                
            elif (605 <= coord_x <=665) and (100 <= coord_y <=165):
                coord_y -= 5
                
            self.machango.place(x = coord_x, y = coord_y)
            
            print(coord_x, coord_y)
        elif evento.keysym == "d" or evento.keysym == "Right":
            coord_x += 5
            if coord_x >= self.x_max_prota:
                coord_x -= 5
            
            elif (coord_x >= 580) and (coord_y <= 80):
                coord_x -= 5
                
            elif (605 <= coord_x <=665) and (100 <= coord_y <=165):
                coord_x -= 5
                
            self.machango.place(x = coord_x, y = coord_y)
            
            print(coord_x, coord_y)
        elif evento.keysym == "a" or evento.keysym == "Left":
            coord_x -= 5
            if coord_x <= 0:
                coord_x += 5
            elif (605 <= coord_x <=665) and (100 <= coord_y <=165):
                coord_x += 5
            
            
            self.machango.place(x = coord_x, y = coord_y)
            
            print(coord_x, coord_y)
            
            
        if (coord_x >= 560) and (60 <= coord_y <= 200):
            self.comprar.place(x= 600, y = 58)
        
        #-------------reemplazar por boton de combate-------------
        elif (coord_x == 85) and (coord_y == 135):
            self.comprar.place(x= 600, y = 58)
         
    #--------------comentar que hace-----------
    def abrir_tienda(self):
        abrir_tienda(self)
        self.machango.focus_set()
                   
def main():
    pantalla = PantallaPrincipal()
    return 0

if __name__ == '__main__':
    main()
    
    
    
    
    
    
#85x135
#