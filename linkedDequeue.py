from linkedList import LinkedList
from node import PositionNode as Node

class LinkedDequeue:
    def __init__(self):
        self._list = LinkedList()

    def append(self,row,column):
        #Se inserta un elemento al final del dequeue
        self._list.insert_at(row,column)

    def appendleft(self,row,column):
        #Se inserta un elemento al inicio del dequeue
        self._list.insert_at(row,column,0)

    def pop(self):
        #Obtenemos el nodo a eliminar
        exNode = self._list.tail
        #Eliminamos el ultimo nodo
        self._list.remove_at()

        return exNode.position()

    def popleft(self):
        #Obtenemos el nodo a eliminar
        exNode = self._list.head
        #Eliminamos el primer nodo
        self._list.remove_at(0)

        return exNode.position()
    
    def peek(self):
        #Retornamos el nodo mas a la derecha
        return self._list.tail.position()
    
    def peekleft(self):
        #Retornamos el nodo mas a la izquierda
        return self._list.head.position()

    def get_elements(self):
        #Retornamos los elementos
        return self._list.get_positions()
