from node import PositionNode as Node

class LinkedList:
    def __init__(self):
        self._head = Node(6,6)
        self.head.nextNode = Node(7,6)
        self._tail = Node(8,6)
        self.head.nextNode.nextNode = self._tail
        self.head.nextNode.previousNode = self._head
        self._tail.previousNode = self.head.nextNode
        self._size = 3

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail
    
    @property
    def size(self):
        return self._size

    def get_positions(self):
        positions = []
        current_node = self._head
        #Se recorre la lista doblemente enlazada
        while current_node is not None:
            #Se adiciona las tuplas con los valores de los nodos a un arreglo de redimensionamiehnto dinamico
            positions.append(current_node.position())
            current_node = current_node.nextNode
        #Se retorna el arreglo creado
        return positions

    def insert_at(self, row, column ,index = -1):
        node = Node(row,column)
        
        if index <-1:
            raise ValueError("El índice debe ser mayor o igual a 0")
        
        if index == 0:
            # Insertar al principio
            if self._head is not None:
                node.nextNode = self._head
                self._head.previousNode = node
                self._head = node
                if self._tail is None:
                    self._tail = node
        elif index == self._size or index == -1:
            # Insertar al final
            if self._tail is not None:
                node.previousNode = self._tail
                self._tail.nextNode = node
                self._tail = node

        # Incrementar el tamaño de la lista
        self._size += 1

    def remove_at(self, index=-1):
        if index < -1:
            raise ValueError("El índice debe ser mayor o igual a 0")

        if index == 0:
            # Eliminar el primer nodo
            if self._head is not None:
                self._head = self._head.nextNode
                if self._head is not None:
                    self._head.previousNode = None
                else:
                    self._tail = None
        elif index == self._size - 1 or index == -1:
            # Eliminar el último nodo
            if self._tail is not None:
                self._tail = self._tail.previousNode
                if self._tail is not None:
                    self._tail.nextNode = None
                else:
                    self._head = None

        # Disminuir el tamaño de la lista
        self._size -= 1