import tkinter as tk
from snake import Snake
from tkinter import messagebox
import time

ventana=tk.Tk() #ventana principal
ventana.title('Snake') #nombre de la ventana
ventana.geometry('1000x700') #tamaño de la ventana anchoxalto
ventana.resizable(False, False) #Se permite que se ajuste el tamaño de la ventana
ventana.focus_set()

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
manual_move = False
tiempo_inicial = time.time()

juego_iniciado = False  # Variable para rastrear si el juego ha comenzado
# Variable para rastrear si la advertencia ya se mostró
advertencia_mostrada = False

def comprobar(lista):
   if isinstance(lista,str):
      if lista=="cuerpo":
         mostrar_advertencia('¡Te has chocado con tu cuerpo!')
      if lista=="pared":
         mostrar_advertencia('¡Te has chocado con la pared!')
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
   global tiempo_inicial   
   if snake._direction!=(1,0):
      lista=snake.move((-1, 0)) #devuelve false o tupla(lista,posicion manzana)
      comprobar(lista)
      tiempo_inicial = time.time()

   ##pintar(lista)


def mover_izquierda():
   global tiempo_inicial
   if snake._direction!=(0,1):
      lista=snake.move((0,-1))
      comprobar(lista)
      tiempo_inicial = time.time()


def mover_abajo():
   global tiempo_inicial   
   if snake._direction!=(-1,0):
      lista=snake.move((1, 0))
      comprobar(lista)
      tiempo_inicial = time.time()
   

def mover_derecha():
   global tiempo_inicial   
   if snake._direction!=(0,-1):
      lista=snake.move((0, 1))
      comprobar(lista)
      tiempo_inicial = time.time()


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
   global juego_iniciado
   respuesta = messagebox.showwarning("Iniciar", "INICIAR JUEGO?", icon="question")
   if respuesta == 'ok':
      juego_iniciado = True
      global snake
      snake = Snake()
      tablero(snake.move())

      # Establecer el foco en la ventana principal después de iniciar el juego
      ventana.focus_set()

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


def mostrar_advertencia(text): # Se llama desde collision en snake y muestra una advertencia al perder o reiniciar el juego
   global advertencia_mostrada
   if not advertencia_mostrada:
      print("Mostrando advertencia")
      respuesta = messagebox.showwarning("PERDISTE", f"{text}.\n¿Quieres reiniciar el juego?", type="yesno")
      advertencia_mostrada = True
      if respuesta == 'yes':
         reiniciar_juego()
      else:
         ventana.destroy()

def verificar_movimiento():
   global tiempo_inicial, advertencia_mostrada
   if juego_iniciado and time.time()-tiempo_inicial >= 0.8 and not advertencia_mostrada:
      lista = snake.move()
      comprobar(lista) 
      tiempo_inicial = time.time()
   # Programa la próxima verificación después de 1000 milisegundos (1 segundo)
   ventana.after(800, verificar_movimiento)

def reiniciar_juego():
   global juego_iniciado, snake, advertencia_mostrada
   juego_iniciado = False
   snake = Snake()
   advertencia_mostrada = False
   tablero(snake.move())
   ventana.focus_set()
   verificar_movimiento()

# ... Tu código anterior ...

ventana.after(0, lambda: ventanainiciar())

# Inicia la primera verificación después de 1 segundo
ventana.after(800, verificar_movimiento)

ventana.focus_set()

ventana.mainloop()