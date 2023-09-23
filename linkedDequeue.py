from linkedList import LinkedList
from node import PositionNode as Node

class LinkedDequeue:
    def __init__(self):
        """
        Constructor de la clase LinkedQueue.
        Inicializa una cola vacía basada en una lista enlazada.
        """
        self._list = LinkedList()

    def append(self,row,column):
        """
        Agrega un elemento a la derecha del dequeue.

        :param row: La fila del nuevo elemento.
        :type row: int
        :param column: La columna del nuevo elemento.
        :type column: int
        """
        self._list.insert_at(row,column)

    def appendleft(self,row,column):
        """
        Agrega un elemento a la izquierda del dequeue.

        :param row: La fila del nuevo elemento.
        :type row: int
        :param column: La columna del nuevo elemento.
        :type column: int
        """
        self._list.insert_at(row,column,0)

    def pop(self):
        """
        Elimina y devuelve el elemento mas a la derecha del dequeue.

        :return: El elemento eliminado.
        :rtype: tuple[int, int]
        """
        #Obtenemos el nodo a eliminar
        exNode = self._list.tail
        #Eliminamos el ultimo nodo
        self._list.remove_at()

        return exNode.position()

    def popleft(self):
        """
        Elimina y devuelve el elemento mas a la izquierda del dequeue.

        :return: El elemento eliminado.
        :rtype: tuple[int, int]
        """
        #Obtenemos el nodo a eliminar
        exNode = self._list.head
        #Eliminamos el primer nodo
        self._list.remove_at(0)

        return exNode.position()
    
    def peek(self):
        """
        Devuelve el elemento mas a la derecha del dequeue.

        :return: El elemento eliminado.
        :rtype: tuple[int, int]
        """
        return self._list.tail.position()
    
    def peekleft(self):
        """
        Devuelve el elemento mas a la izquierda del dequeue.

        :return: El elemento eliminado.
        :rtype: tuple[int, int]
        """
        return self._list.head.position()

    def get_elements(self):
        """
        Obtiene una lista de tuplas que representan los elementos en el dequeue.

        :return: Lista de tuplas de elementos.
        :rtype: list[tuple[int, int]]
        """
        return self._list.get_positions()


if __name__ == '__main__':
    cola = LinkedDequeue()

    n1 = Node(1, 2)
    n2 = Node(3, 4)
    n3 = Node(5, 6)
    cola.append(*n1.position())
    cola.append(*n2.position())  
    cola.append(*n3.position())

    elementos = cola.get_elements()

    print("Elementos en la cola:", elementos)

    # Eliminar el elemento de la cola
    elemento_eliminado = cola.pop()

    elementos = cola.get_elements()

    print("Elementos en la cola después de eliminar uno:", elementos)