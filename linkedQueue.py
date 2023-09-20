from linkedList import LinkedList
from node import PositionNode

class LinkedQueue:
    def __init__(self):
        """
        Constructor de la clase LinkedQueue.
        Inicializa una cola vacía basada en una lista enlazada.
        """
        self._list = LinkedList()

    def is_empty(self):
        """
        Verifica si la cola está vacía.

        :return: True si la cola está vacía, False en caso contrario.
        :rtype: bool
        """
        return self._list.empty()

    def enqueue(self, row, column):
        """
        Agrega un nuevo elemento a la cola.

        :param row: La fila del nuevo elemento.
        :type row: int
        :param column: La columna del nuevo elemento.
        :type column: int
        """
        self._list.append(row, column)

    def dequeue(self):
        """
        Elimina y devuelve el elemento de la cola.

        :return: El elemento eliminado.
        :rtype: tuple[int, int]
        """
        if self.is_empty():
            raise IndexError("La cola está vacía")

        # Obtenemos el primer elemento de la cola
        first_element = self._list.get_positions()[0]

        # Eliminamos el primer elemento de la cola
        self._list.remove_at(0)

        return first_element

    def get_elements(self):
        """
        Obtiene una lista de tuplas que representan los elementos en la cola.

        :return: Lista de tuplas de elementos.
        :rtype: list[tuple[int, int]]
        """
        return self._list.get_positions()
    
    def move(self,direction):
        if self.is_empty():
            raise IndexError("La cola esta vacia")
        
        #Obtenemos la cabeza actual de la cola
        current_head = PositionNode(*self._list.head.position())

        new_head = current_head + direction

        

if __name__ == '__main__':
    cola = LinkedQueue()

    cola.enqueue(1, 2)
    cola.enqueue(3, 4)  
    cola.enqueue(5, 6)

    elementos = cola.get_elements()

    print("Elementos en la cola:", elementos)

    # Eliminar el elemento de la cola
    elemento_eliminado = cola.dequeue()

    elementos = cola.get_elements()

    print("Elementos en la cola después de eliminar uno:", elementos)

    [(1,1),(1,2),(1,3)]
    [(2,1),(1,1),(1,2)]
    (1,0)(0,1)(-1,0)(0,-1)
