from linkedDequeue import LinkedDequeue
from node import PositionNode as Node
import random

class Snake:
    def __init__(self):
        self.__body = LinkedDequeue()
        self._direction = (-1, 0)
        self.__define_apple()
        self._count_apple = 0
        self.dont_move = False
        self.moves = 0

    def move(self, direction=None):
        #Comprobamos si la serpiente tiene permitido moverse
        if not self.dont_move:    
            #Si la funcion move viene con parametro vacio se asigna
            if direction == None:
                direction = self._direction
            else:
                #Si tiene un nuevo parametro direccion se asigna
                self._direction = direction

            # Comprobamos si es una direccion prohibida
            if direction != (-1 * self._direction[0], -1 * self._direction[1]):
                # Se obtiene el nodo cabeza de la serpiente y se le suma la direccion
                new_node = Node(*self.__body.peekleft()) + Node(*direction)
                #Se comprueba si la serpiente se comio una manzan
                eat = self.__eat_apple()
                #Se añade una nueva cabeza al cuerpo
                self.__body.appendleft(*new_node.position())
                #Se suma uno al contador de movimientos
                self.moves += 1
                #Comprobamos si la serpiente se comio una manzana para saber si eliminamos la ola
                if not eat:
                    self.__body.pop()
                else:
                    #Definimos la manzana como una posicion nula mientras se ejecutan los movimientos requeridos 
                    self._apple = (-1,-1)  
                    #Se define el nuevo numero de movimientos requeridos para que aparezca la manzana
                    self._count_apple = random.randint(1,10)-1
                    #Se guarda cuantos movimientos habia hasta el momento en el que se comio la ultima manzana
                    self.last_count = self.moves
                #En cada movimiento se resta uno al contador siempre que el contador no sea -1 ya que significa
                #que hay una manzana en el mapa que no ha sido comida
                self._count_apple -= 1 if self._count_apple != -1 else 0

                #Si el contador llega a cero se define una nueva manzana
                if self._count_apple == 0:
                    self.__define_apple()
                    #Se iguala el contador a -1 hasta que se coman la manzana que hay en el mapa
                    self._count_apple = -1
                #Si ocurre el bug y no se asigna una manzana luego de 10 movimientos se fuerza la aparicion
                if self._count_apple == -1  and self._apple == (-1,-1) and self.moves - self.last_count>10:
                    self.__define_apple()
                    self._count_apple = -1

            #Si no hay colisiones retornamos el cuerpo de la serpiente y la posicion de la manzan
            if self.__collision() == True:
                return (self.__body.get_elements(),self._apple)  
            #Retornamos cuerpo si la serpiente se ha chocado con su propio cuerpo
            if self.__collision() == "cuerpo":
                return "cuerpo"
            #Retornamos pared si la serpiente se salio del mapa
            if self.__collision() == "pared":
                return "pared"
        else:
            #Se retorna un valor que no cumple las condiciones para que el juego se detenga
            return [13,13]
        
    def __define_apple(self):
        #Definimos la nueva tupla manzana y obtenemos los elementos
        nueva_manzana = None
        posiciones = self.__body.get_elements()

        while True:
            #Generamos dos numeros aleatorios y los volvemos tupla
            x = random.randint(0,12)
            y = random.randint(0,12)
            nueva_manzana = (x,y)

            #Si la tupla no se encuentra en la lista de tuplas cerramos el ciclo
            if nueva_manzana not in posiciones:
                break

        #asignamos el nuevo valor de la manzana
        self._apple = nueva_manzana

    def __eat_apple(self, direction=None):
        #Si la direccion esta vacia se asigna la direccion interna
        if direction == None:
            direction = self._direction

        #Se obtiene el nodo cabeza
        nodo_cabeza = Node(*self.__body.peekleft())
        #Se crea un nodo con la direccion
        nodo_direccion = Node(*direction)
        #Se crea un nodo con la posicion de la manzana
        manzana = Node(*self._apple)
        #Se crea el nodo donde quedara la cabeza, sumando las posiciones de la direccion y la cabeza
        futuro_nodo_cabeza = nodo_cabeza+nodo_direccion

        #Se retorna si la futura cabeza es la posicion de la manzana
        return futuro_nodo_cabeza == manzana
        
    def __collision(self):
        # Se verifica que la cordenada de la cabeza no este fuera del tablero
        if not 0 <= self.__body.peekleft()[0] < 13 or not 0 <= self.__body.peekleft()[1] < 13:
            return "pared"

        # Se verifica que la coordenada de la cabeza no este sobre otra coordenada del cuerpo.
        if self.__body.peekleft() in self.__body.get_elements()[1:]:
            return "cuerpo"
        #Se retorna true si la cabeza de la serpiente no incumple ninguna norma
        return True    