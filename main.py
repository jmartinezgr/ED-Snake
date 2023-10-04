import tkinter as tk
from snake import Snake
from tkinter import messagebox
import time

ventana=tk.Tk() #ventana principal
ventana.title('Snake') #nombre de la ventana
ventana.geometry('1000x700') #tamaño de la ventana anchoxalto
ventana.resizable(False, False)

#se crearon dos contenedores
frameabajo=tk.Frame(ventana) #se ubican los botones A,S,D,W
framearriba=tk.Frame(ventana,relief="solid", borderwidth=1) #se va a ubicar la cuadricula, relief el el color del borde y borderwidth el tamaño del borde(simula los limites del juego)
frameabajo.pack(side='bottom') #se ubica abajo
framearriba.pack() #se ubica en el resto de la ventana(arriba)

#Creamos una matriz vacia con las posiciones del grid 
labels= [[None for _ in range(13)] for _ in range(13)] 

#ciclo para que se creen las etiquetas
for i in range(13):
   for j in range(13):
      labels[i][j] = tk.Label(framearriba, borderwidth=1, width=4, height=2) #width y height es el tamaño por pixel en alto y ancho(queda mas o menos cuadrado)  relief='solid' para ver los bordes
      labels[i][j].grid(row=i, column=j) #posiciones

#Creamos los botones necesarios para el movimiento
botonW=tk.Button(frameabajo,text='W',width=10, height=5,command = lambda: mover_arriba()) #width ancho, height alto, está en el frame de abajo
botonW.grid(row=0, column=1) #posicion de los botones dentro del frame
botonA=tk.Button(frameabajo,text='A',width=10, height=5,command = lambda: mover_izquierda())
botonA.grid(row=1, column=0)
botonS=tk.Button(frameabajo,text='S',width=10, height=5,command = lambda: mover_abajo())
botonS.grid(row=1, column=1)
botonD=tk.Button(frameabajo,text='D',width=12, height=5,command = lambda: mover_derecha())
botonD.grid(row=1, column=2)

#Inicilizamos un objeto de tipo snake
snake=Snake()
#Tomamos el tiempo inicial del juego
tiempo_inicial = time.time()
# Variable para rastrear si el juego ha comenzado
juego_iniciado = False  

def ventanainiciar():
   #Se accede a la variable global juego iniciado   
   global juego_iniciado
   respuesta = messagebox.showwarning("Iniciar", "INICIAR JUEGO?", icon="question")
   if respuesta == 'ok':
      juego_iniciado = True

def mover_arriba():
   #Se accede a la variable global tiempo inicial
   global tiempo_inicial   
   if snake._direction!=(1,0):
      lista=snake.move((-1, 0)) #devuelve false o tupla(lista,posicion manzana)
      comprobar(lista)
#Si se realizo un movimiento manual se reinicia el tiempo, tomando el tiempo del ultimo movimiento hecho a mano
      tiempo_inicial = time.time()

def mover_izquierda():
   #Se accede a la variable global tiempo inicial   
   global tiempo_inicial
   if snake._direction!=(0,1):
      lista=snake.move((0,-1))
      comprobar(lista)
      #Si se realizo un movimiento manual se reinicia el tiempo, tomando el tiempo del ultimo movimiento hecho a mano
      tiempo_inicial = time.time()

def mover_abajo():
   #Se accede a la variable global tiempo inicial
   global tiempo_inicial   
   if snake._direction!=(-1,0):
      lista=snake.move((1, 0))
      comprobar(lista)
      #Si se realizo un movimiento manual se reinicia el tiempo, tomando el tiempo del ultimo movimiento hecho a mano      
      tiempo_inicial = time.time()
   
def mover_derecha():
   #Se accede a la variable global tiempo inicial   
   global tiempo_inicial   
   if snake._direction!=(0,-1):
      lista=snake.move((0, 1))
      comprobar(lista)
      #Si se realizo un movimiento manual se reinicia el tiempo, tomando el tiempo del ultimo movimiento hecho a mano      
      tiempo_inicial = time.time()

def comprobar(lista):
   #Comprobamos si el elemento retornado por snake.move() retorna un string
   if isinstance(lista,str):
      #Si el string es cuerpo significa que perdio por chocarse con el cuerpo
      if lista=="cuerpo":
         #Se establece el atributo dont_move como True para que la serpiente no acepte llamados despues de perder
         snake.dont_move = True         
         mostrar_advertencia('¡Te has chocado con tu cuerpo!')
      #Si el string es cuerpo significa que perdio por chocarse con los limites del mapa
      if lista=="pared":
         #Se establece el atributo dont_move como True para que la serpiente no acepte llamados despues de perder
         snake.dont_move = True
         mostrar_advertencia('¡Te has chocado con la pared!')
   elif isinstance(lista[0],list) and isinstance(lista[1],tuple):
      #Si se devuelve la lista con el cuerpo de la serpiente y la posicion de la manzana se pintan en el mapa
      tablero(lista)

def tablero(tupla):
   #Se pintan todas las columnas de blanco
   for i in range(13):
      for j in range(13):
         labels[i][j].config(bg='white')
   #Comprobamos si la respuesta de la funcion move no es falsa
   if tupla!=False:
      #Recorremos las posiciones devueltas y pintamos el grid
      posiciones, posicion_manzana = tupla[0],tupla[1]
      for i,j in posiciones:
         tupla=(i,j)
         if tupla==posiciones[0]:
            labels[i][j].config(text='', bg='dark gray')
         else:
            labels[i][j].config(text='', bg='light gray')

   #Si la manzana existe se pinta de negro
   if posicion_manzana != (-1,-1):
      labels[posicion_manzana[0]][posicion_manzana[1]].config(text='', bg='black')

def mostrar_advertencia(text): # Se llama desde collision en snake y muestra una advertencia al perder o reiniciar el juego
   respuesta = messagebox.showwarning("PERDISTE", f"{text}. Has conseguido realizar {snake.moves} movimientos")     
   if respuesta == 'ok':
      ventana.destroy()
   else:
      ventana.destroy()

def verificar_movimiento():
   #Se accede a la variable global tiempo inicial   
   global tiempo_inicial
   #La variable tiempo inicial sirve para saber cual fue el ultimo registro de un movimiento manual
   if juego_iniciado and time.time()-tiempo_inicial >= 0.8 :
      #Si dicho movimiento fue hace mas de 0.8 segundos el juego hace un movimiento automatico siguiendo la direccion actual del cuerpo
      lista = snake.move()
      comprobar(lista) 
      #Se reinicia el valor de tiempo inicial, ya que se realizo un movimiento
      tiempo_inicial = time.time()
   # Programa la próxima verificación después de 800 milisegundos (0.8 segundos)
   ventana.after(800, verificar_movimiento) 

#Recien se inicia la ventana se llama a la funcion iniciar ventana
ventana.after(0, lambda: ventanainiciar())

#Luego de 800 milisegundos se verifica por primera vez si no han habido movimientos
ventana.after(800, verificar_movimiento)

ventana.mainloop()