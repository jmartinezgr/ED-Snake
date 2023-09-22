from node import PositionNode as Node

class LinkedList:
    def __init__(self):
        """
        Constructor de la clase LinkedList.
        Inicializa una lista doblemente enlazada vacía.
        """
        self._head = Node(6,6)
        self.head.nextNode = Node(7,6)
        self._tail = Node(8,6)
        self.head.nextNode.nextNode = self._tail
        self.head.nextNode.previousNode = self._head
        self._tail.previousNode = self.head.nextNode
        self._size = 3

    @property
    def head(self):
        """
        Obtiene el nodo principal de la lista.

        :return: El nodo principal.
        :rtype: Node
        """
        return self._head

    @property
    def tail(self):
        """
        Obtiene el nodo final de la lista.

        :return: El nodo final.
        :rtype: Node
        """
        return self._tail
    
    @property
    def size(self):
        """
        Obtiene el tamaño de la lista.

        :return El tamaño de la lista.
        :rtype: Int
        """
        return self._size

    def get_positions(self):
        """
        Obtiene una lista de tuplas que representan las posiciones de los nodos en la lista.

        :return: Lista de tuplas de posiciones.
        :rtype: list[tuple[int, int]]
        """
        positions = []
        current_node = self._head
        while current_node is not None:
            positions.append(current_node.position())
            current_node = current_node.nextNode
        return positions

    def insert_at(self, row, column ,index = -1):
        """
        Inserta un nodo en una posición específica de la lista.

        :param node: El nodo que se va a insertar.
        :type node: Node
        :param index: La posición en la que se va a insertar el nodo.
        :type index: int
        """
        
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
        """
        Elimina el nodo en una posición específica de la lista.

        :param index: La posición del nodo que se va a eliminar.
        :type index: int
        """
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


if __name__ == '__main__':
    lista = LinkedList()
    
    lista.insert_at(1, 2)
    lista.insert_at(3, 4)
    lista.insert_at(5, 6)    

    posiciones = lista.get_positions()

    print("Posiciones de los nodos en la lista:", posiciones)

    # Insertar un nuevo nodo en la posición 0
    nuevo_nodo = Node(7, 8)
    lista.insert_at(*nuevo_nodo.position())
    nuevo_nodo = Node(9,10)
    lista.insert_at(*nuevo_nodo.position())

    posiciones = lista.get_positions()

    print("Posiciones de los nodos después de la inserción:", posiciones)

    lista.remove_at()
    lista.remove_at()
    lista.remove_at()
    lista.remove_at(0)

    posiciones = lista.get_positions()

    print("Posiciones de los nodos después de la eliminacion:", posiciones)

    lista.insert_at(6,6,0)

    posiciones = lista.get_positions()

    print("Posiciones de los nodos después de la inserción:", posiciones)
    


