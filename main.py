import tkinter as tk
from snake import Snake
from tkinter import messagebox


ventana=tk.Tk() #ventana principal
ventana.title('Snake') #nombre de la ventana
ventana.geometry('1000x700') #tamaño de la ventana anchoxalto
ventana.resizable(False, False) #Se permite que se ajuste el tamaño de la ventana


#se crearon dos contenedores
frameabajo=tk.Frame(ventana) #se ubican los botones A,S,D,W
framearriba=tk.Frame(ventana,relief="solid", borderwidth=1) #se va a ubicar la cuadricula, relief el el color del borde y borderwidth el tamaño del borde(simula los limites del juego)


frameabajo.pack(side='bottom') #se ubica abajo
framearriba.pack() #se ubica en el resto de la ventana(arriba)

labels= [[None for _ in range(13)] for _ in range(13)] 

#ciclo para que se creen las etiquetas
for i in range(13):
   for j in range(13):
      labels[i][j] = tk.Label(framearriba, borderwidth=1, width=4, height=2) #width y height es el tamaño por pixel en alto y ancho(queda mas o menos cuadrado)  relief='solid' para ver los bordes
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

def comprobar(lista):
   if isinstance(lista,bool):
      mostrar_advertencia('¡Te has chocado con tu cuerpo¡')
      #if lista=='cuerpo':
         #mostrar_advertencia('¡Te has chocado con tu cuerpo¡')
      #elif lista=='pared':
         #mostrar_advertencia('¡Te has chocado con la pared')

   else:
      tablero(lista)
      #if lista=='cuerpo':
       #  mostrar_advertencia('¡Te has chocado con tu propio cuerpo!')
      #elif lista=='pared':
       #  mostrar_advertencia('¡Te has chocado con la pared!')

def mover_arriba():
   if snake._direction!=(1,0):
      lista=snake.move((-1, 0)) #devuelve false o tupla(lista,posicion manzana)
      comprobar(lista)

   ##pintar(lista)


def mover_izquierda():
   if snake._direction!=(0,1):
      lista=snake.move((0,-1))
      comprobar(lista)


def mover_abajo():
   if snake._direction!=(-1,0):
      lista=snake.move((1, 0))
      comprobar(lista)
   

def mover_derecha():
   if snake._direction!=(0,-1):
      lista=snake.move((0, 1))
      comprobar(lista)


# Enlazar teclas con funciones de movimiento
ventana.bind('<Up>', lambda event: mover_arriba())
ventana.bind('<Left>', lambda event: mover_izquierda())
ventana.bind('<Down>', lambda event: mover_abajo())
ventana.bind('<Right>', lambda event: mover_derecha())
ventana.bind('w', lambda event: mover_arriba())
ventana.bind('a', lambda event: mover_izquierda())
ventana.bind('s', lambda event: mover_abajo())
ventana.bind('d', lambda event: mover_derecha())

def ventanainiciar():
   respuesta = messagebox.showwarning("Iniciar", "INICIAR JUEGO?",icon="question")
   if respuesta == 'ok':
     tablero(snake.move())
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

   if posicion_manzana != (-1,-1):
      labels[posicion_manzana[0]][posicion_manzana[1]].config(text='', bg='black')


def mostrar_advertencia(text):#se llama desde collision en snake y saca una advertenica al perder de reinciar juego o no
   respuesta = messagebox.showwarning("PERDISTE", f"{text}.\n¿Quieres reiniciar el juego?", type="yesno")
   if respuesta == 'yes':
      global snake
      snake = Snake()
      tablero(snake.move())
   else:
      ventana.destroy()

ventana.after(0, lambda: ventanainiciar())
ventana.mainloop()