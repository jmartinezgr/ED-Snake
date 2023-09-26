import tkinter as tk
from snake import Snake
from tkinter import messagebox
import linkedDequeue


ventana=tk.Tk() #ventana principal
ventana.title('Snake') #nombre de la ventana
ventana.geometry('1000x700') #tamaño de la ventana anchoxalto
ventana.resizable(False, False) #Se permite que se ajuste el tamaño de la ventana


#se crearon dos contenedores
frameabajo=tk.Frame(ventana) #se ubican los botones A,S,D,W
framearriba=tk.Frame(ventana,relief="solid", borderwidth=1) #se va a ubicar la cuadricula, relief el el color del borde y borderwidth el tamaño del borde(simula los limites del juego)


frameabajo.pack(side='bottom') #se ubica abajo
framearriba.pack() #se ubica en el resto de la ventana(arriba)

"""
A=[] #genera matriz de labels para facilitar el acceso y cambio de esta cambié: labels = [[None for _ in range(13)] for _ in range(13)]
for i in range(13):
   A.append(None)
   """

labels= [[None for _ in range(13)] for _ in range(13)] 

"""
for i in range(13):
   labels.append(A)
"""

#ciclo para que se creen las etiquetas
for i in range(13):
   for j in range(13):
      labels[i][j] = tk.Label(framearriba, borderwidth=1, width=4, height=2, relief="solid") #width y height es el tamaño por pixel en alto y ancho(queda mas o menos cuadrado)  relief='solid' para ver los bordes
      labels[i][j].grid(row=i, column=j) #posiciones


botonW=tk.Button(frameabajo,text='W',width=10, height=5,command = lambda: mover_arriba()) #width ancho, height alto, está en el frame de abajo
botonW.grid(row=0, column=1) #posicion de los botones dentro del frame
botonA=tk.Button(frameabajo,text='A',width=10, height=5,command = lambda: mover_izquierda())
botonA.grid(row=1, column=0)
botonS=tk.Button(frameabajo,text='S',width=10, height=5,command = lambda: mover_abajo())
botonS.grid(row=1, column=1)
botonD=tk.Button(frameabajo,text='D',width=12, height=5,command = lambda: mover_derecha())
botonD.grid(row=1, column=2)

snake=Snake()

def mover_arriba():
   lista=snake.move((-1, 0)) #devuelve false o tupla(lista,posicion manzana)
   if lista is not False:
      tablero(lista)
      #ventana.after(200,snake.move())
   else:
      mostrar_advertencia('¡Te has chocado con tu propio cuerpo!')
   ##pintar(lista)


def mover_izquierda():
   lista=snake.move((0,-1))
   if lista is not False:
      tablero(lista)
      #ventana.after(200,snake.move())
   else:
      mostrar_advertencia('¡Te has chocado con tu propio cuerpo!')
   


def mover_abajo():
   lista=snake.move((1, 0))
   if lista is not False:
      tablero(lista)
      #ventana.after(200,snake.move())
   else:
      mostrar_advertencia('¡Te has chocado con tu propio cuerpo!')
   

def mover_derecha():
   lista=snake.move((0, 1))
   if lista is not False:
      tablero(lista)
      #ventana.after(200,snake.move())
   else:
      mostrar_advertencia('¡Te has chocado con tu propio cuerpo!')
   


# Enlazar teclas con funciones de movimiento
ventana.bind('<W>', mover_arriba)
ventana.bind('<A>', mover_izquierda)
ventana.bind('<S>', mover_abajo)
ventana.bind('<D>', mover_derecha)

def ventanainiciar():
   respuesta = messagebox.showwarning("Iniciar", "INICIAR JUEGO?",icon="question")
   if respuesta == 'ok':
     tablero(snake.move())
     #mover_serpiente() #comando para que inicie a moverse cuando no hay movimeintos.
     pass

def tablero(tupla):
    
   for i in range(13):
      for j in range(13):
         labels[i][j].config(bg='white')

   if tupla!=False:
      posiciones, posicion_manzana = tupla[0],tupla[1]
      for i,j in posiciones:
         tupla=(i,j)
         if tupla==posiciones[0]:
            labels[i][j].config(text='', bg='dark gray')
         else:
            labels[i][j].config(text='', bg='light gray')

   labels[posicion_manzana[0]][posicion_manzana[1]].config(text='', bg='black')

def reiniciar():
   snake = Snake()

def mostrar_advertencia(text):#se llama desde collision en snake y saca una advertenica al perder de reinciar juego o no
    respuesta = messagebox.showwarning("PERDISTE", f"{text}.\n¿Quieres reiniciar el juego?", type="yesno")
    if respuesta == 'yes':
        ventanainiciar()
    else:
        ventana.destroy()

ventana.after(0, lambda: ventanainiciar())
ventana.mainloop()