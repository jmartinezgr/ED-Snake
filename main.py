import tkinter as tk
from snake import Snake


ventana=tk.Tk() #ventana principal
ventana.title('Snake') #nombre de la ventana
ventana.geometry('1000x700') #tamaño de la ventana anchoxalto
ventana.resizable(False, False) #Se permite que se ajuste el tamaño de la ventana


#se crearon dos contenedores
frameabajo=tk.Frame(ventana) #se ubican los botones A,S,D,W
framearriba=tk.Frame(ventana,relief="solid", borderwidth=1) #se va a ubicar la cuadricula, relief el el color del borde y borderwidth el tamaño del borde(simula los limites del juego)


frameabajo.pack(side='bottom') #se ubica abajo
framearriba.pack() #se ubica en el resto de la ventana(arriba)


A=[] #genera matriz de labels para facilitar el acceso y cambio de esta cambié: labels = [[None for _ in range(13)] for _ in range(13)]
for i in range(13):
  A.append(None)
labels=[A] 
for i in range(13):
  labels.append(A)

#ciclo para que se creen las etiquetas
for i in range(13):
    for j in range(13):
        labels[i][j] = tk.Label(framearriba, text=f"{i},{j}", borderwidth=1, width=4, height=2, relief="solid") #width y height es el tamaño por pixel en alto y ancho(queda mas o menos cuadrado)  relief='solid' para ver los bordes
        labels[i][j].grid(row=i, column=j) #posiciones


botonW=tk.Button(frameabajo,text='W',width=10, height=5,command = lambda: mover_arriba()) #width ancho, height alto, está en el frame de abajo
botonW.grid(row=0, column=1) #posicion de los botones dentro del frame
botonA=tk.Button(frameabajo,text='A',width=10, height=5,command = lambda: mover_izquierda())
botonA.grid(row=1, column=0)
botonS=tk.Button(frameabajo,text='S',width=10, height=5,command = lambda: mover_abajo())
botonS.grid(row=1, column=1)
botonD=tk.Button(frameabajo,text='D',width=12, height=5,command = lambda: mover_derecha())
botonD.grid(row=1, column=2)

def mover_arriba():
   list=Snake.move((-1, 0)) #devuelve false o tupla(lista,posicion manzana)
   if list is not False:
      pass

def mover_izquierda():
   list=Snake.move((-1, 0))
   if list is not False:
      pass


def mover_abajo():
   list=Snake.move((-1, 0))
   if list is not False:
      pass


def mover_derecha():
   list=Snake.move((-1, 0))
   if list is not False:
      pass


# Enlazar teclas con funciones de movimiento
ventana.bind('w', snake.move((-1, 0)))
ventana.bind('a', snake.move((0, -1)))
ventana.bind('s', snake.move((1, 0)))
ventana.bind('d', snake.move((0, 1)))

ventana.mainloop() #muestra7ejecuta la ventana principal y por ende el resto