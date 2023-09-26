from linkedDequeue import LinkedDequeue
from node import PositionNode as Node
#import main
import random

class Snake:
    def __init__(self):
        """
        Constructor de la clase Snake.
        Inicializa un objeto de tipo Snake que almacena las posiciones del
        cuerpo de la serpiente.
        """
        self.__body = LinkedDequeue()
        self._direction = (-1, 0)
        self.__define_apple()

    def move(self, direction=None):
        """
        Mueve el cuerpo de la serpiente en una direccion dada

        :param direction: Tupla que contiene la direccion que va a tomar la cabeza
        :type node: Tuple[int, int]
        :return: Lista con las posiciones modificadas
        :rtype: list[tuple[int, int]]
        """
        if direction == None:
            direction = self._direction
        else:
            self._direction = direction

        # Comprobamos si es una direccion prohibida
        if direction != (-1 * self._direction[0], -1 * self._direction[1]):
            # Se obtiene el nodo cabeza de la serpiente y se le suma la direccion
            new_node = Node(*self.__body.peekleft()) + Node(*direction)
            # Se adiciona la nueva cabeza al cuerpo
            
            eat = self.__eat_apple()
            
            self.__body.appendleft(*new_node.position())
            if not eat:
                self.__body.pop()
            else:
                self.__define_apple()

        return (self.__body.get_elements(),self._apple) if self.__collision() else False

    def __define_apple(self):
        """
        Asigna de manera aleatoria una posicion a la manzana, esta posicion
        no puede estar sobre el cuerpo de la serpiente

        :param: None
        :rtype: None
        """
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
        """
        Verifica si en el siguiente movimiento la cabeza de la serpiente pasara por la manzana
        
        :param direction: Tupla que contiene la direccion que va a tomar la cabeza
        :type node: Tuple[int, int]
        :return: Retorna si en el proximo movimiento se comera la manzana
        :rtype: boolean
        """
        if direction == None:
            direction = self._direction

        nodo_cabeza = Node(*self.__body.peekleft())
        nodo_direccion = Node(*direction)
        manzana = Node(*self._apple)
        futuro_nodo_cabeza = nodo_cabeza+nodo_direccion

        return futuro_nodo_cabeza == manzana
        
    def __collision(self):
        """
        Retorna si la cabeza de la serpiente esta fuera del tablero o chochandose con su cuerpo

        :return: Retorna False si se cumple alguna condicion, indicando que el juego termino
        :rtype: boolean
        """
        # Se verifica que la cordenada de la cabeza no este fuera del tablero
        if not 0 <= self.__body.peekleft()[0] < 13 or not 0 <= self.__body.peekleft()[1] < 13:
            #main.mostrar_advertencia('¡Has chocado con la pared!') #ejecuta la advertencia
            return False

        # Se verifica que la coordenada de la cabeza no este sobre otra coordenada del cuerpo.
        #print(self.__body.get_elements())
        if self.__body.peekleft() in self.__body.get_elements()[1:]:
            #main.mostrar_advertencia('¡Has chocado con tu cuerpo!')
            return False

        return True

    
if __name__ == "__main__":
    snake = Snake()
    print(snake.move((1,0)))
    while True:
        a,b = list(map(int,input().split()))
        posiciones = snake.move((a,b))
        print(posiciones if posiciones else "Termino el juego")        