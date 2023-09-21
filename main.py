import tkinter as tk

ventana=tk.Tk() #ventana principal
ventana.title('Snake') #nombre de la ventana
ventana.geometry('1000x800') #tamaño de la ventana anchoxalto
ventana.resizable(False,False) #no permite que se ajuste el tamaño de la ventana


#se crearon dos contenedores
frameabajo=tk.Frame(ventana) #se ubican los botones A,S,D,W
framearriba=tk.Frame(ventana,relief="solid", borderwidth=1) #se va a ubicar la cuadricula, relief el el color del borde y borderwidth el tamaño del borde(simula los limites del juego)


frameabajo.pack(side='bottom') #se ubica abajo
framearriba.pack(expand=True) #se ubica en el resto de la ventana(arriba)


labels = [[None for _ in range(13)] for _ in range(13)]

#ciclo para que se creen las etiquetas
for i in range(13):
    for j in range(13):
        labels[i][j] = tk.Label(framearriba, text=f"{i},{j}", borderwidth=1, width=4, height=2, relief="solid") #width y height es el tamaño por pixel en alto y ancho(queda mas o menos cuadrado)  relief='raised' para ver los bordes
        labels[i][j].grid(row=i, column=j) #posiciones


botonW=tk.Button(frameabajo,text='W',width=6, height=3,command = lambda: mover_arriba()) #width ancho, height alto, está en el frame de abajo
botonW.grid(row=0, column=1) #posicion de los botones dentro del frame
botonA=tk.Button(frameabajo,text='A',width=6, height=3,command = lambda: mover_izquierda())
botonA.grid(row=1, column=0)
botonS=tk.Button(frameabajo,text='S',width=6, height=3,command = lambda: mover_abajo())
botonS.grid(row=1, column=1)
botonD=tk.Button(frameabajo,text='D',width=6, height=3,command = lambda: mover_derecha())
botonD.grid(row=1, column=2)

def mover_arriba():
    pass

def mover_izquierda():
    pass

def mover_abajo():
    pass

def mover_derecha():
    pass


ventana.mainloop() #muestra7ejecuta la ventana principal y por ende el resto