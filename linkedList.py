from node import PositionNode as Node

class LinkedList:
    def __init__(self):
        """
        Constructor de la clase LinkedList.
        Inicializa una lista doblemente enlazada vacía.
        """
        self._head = None
        self._tail = None
        self._size = 0

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

    def empty(self):
        """
        Verifica si la lista está vacía.

        :return: True si la lista está vacía, False en caso contrario.
        :rtype: bool
        """
        return self._head is None

    def append(self, row, column):
        """
        Agrega un nuevo nodo al final de la lista.

        :param row: La fila del nuevo nodo.
        :type row: int
        :param column: La columna del nuevo nodo.
        :type column: int
        """
        new_node = Node(row, column)

        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.previousNode = self._tail
            self._tail.nextNode = new_node
            self._tail = new_node

        #Se aumenta el tamaño de la lista
        self._size += 1

    def pop(self):
        if self.head is None:
            raise IndexError("No se puede eliminar un elemento de una lista vacia")
        else:
            if self._tail is not None:
                if self._tail == self._head:
                    self._tail = None
                    self._head = None
                else:
                    self._tail = self._tail.previousNode
                    self._tail.nextNode = None
        self._size -= 1

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

    def insert_at(self, node, index):
        """
        Inserta un nodo en una posición específica de la lista.

        :param node: El nodo que se va a insertar.
        :type node: Node
        :param index: La posición en la que se va a insertar el nodo.
        :type index: int
        """
        if index < 0:
            raise ValueError("El índice debe ser mayor o igual a 0")
        
        if index == 0:
            # Insertar al principio
            if self._head is not None:
                node.nextNode = self._head
                self._head.previousNode = node
                self._head = node
                if self._tail is None:
                    self._tail = node
            else:
                # Si la lista está vacía, simplemente definimos el nodo como cabeza y cola
                self._head = node
                self._tail = node
        elif index == self._size:
            # Insertar al final
            if self._tail is not None:
                node.previousNode = self._tail
                self._tail.nextNode = node
                self._tail = node
            else:
                # Si la lista está vacía, simplemente definimos el nodo como cabeza y cola
                self._head = node
                self._tail = node
        else:
            # Insertar en una posición diferente
            current_node = self._head
            current_index = 0

            while current_node is not None and current_index < index:
                current_node = current_node.nextNode
                current_index += 1

            if current_node is None and current_index < index:
                raise ValueError("El índice está fuera de rango")

            node.previousNode = current_node.previousNode
            node.nextNode = current_node
            if current_node.previousNode is not None:
                current_node.previousNode.nextNode = node
            current_node.previousNode = node

        # Incrementar el tamaño de la lista
        self._size += 1

    def remove_at(self, index):
        """
        Elimina el nodo en una posición específica de la lista.

        :param index: La posición del nodo que se va a eliminar.
        :type index: int
        """
        if index < 0:
            raise ValueError("El índice debe ser mayor o igual a 0")

        if index == 0:
            # Eliminar el primer nodo
            if self._head is not None:
                self._head = self._head.nextNode
                if self._head is not None:
                    self._head.previousNode = None
                else:
                    self._tail = None
        elif index == self._size - 1:
            # Eliminar el último nodo
            if self._tail is not None:
                self._tail = self._tail.previousNode
                if self._tail is not None:
                    self._tail.nextNode = None
                else:
                    self._head = None
        else:
            # Eliminar en una posición diferente
            current_node = self._head
            current_index = 0

            while current_node is not None and current_index < index:
                current_node = current_node.nextNode
                current_index += 1

            if current_node is None and current_index < index:
                raise ValueError("El índice está fuera de rango")

            if current_node.previousNode is not None:
                current_node.previousNode.nextNode = current_node.nextNode
            if current_node.nextNode is not None:
                current_node.nextNode.previousNode = current_node.previousNode

            if current_node == self._head:
                self._head = current_node.nextNode

            if current_node == self._tail:
                self._tail = current_node.previousNode

        # Disminuir el tamaño de la lista
        self._size -= 1


if __name__ == '__main__':
    lista = LinkedList()

    lista.append(1, 2)
    lista.append(3, 4)
    lista.append(5, 6)    

    posiciones = lista.get_positions()

    print("Posiciones de los nodos en la lista:", posiciones)

    # Insertar un nuevo nodo en la posición 0
    nuevo_nodo = Node(7, 8)
    lista.insert_at(nuevo_nodo, 0)
    nuevo_nodo = Node(9,10)
    lista.insert_at(nuevo_nodo,2)

    posiciones = lista.get_positions()

    print("Posiciones de los nodos después de la inserción:", posiciones)

    # Eliminar el nodo en la posición 1
    lista.remove_at(0)
    lista.remove_at(lista.size-1)

    posiciones = lista.get_positions()

    print("Posiciones de los nodos después de la eliminación:", posiciones)

    lista.pop()
    posiciones = lista.get_positions()

    print("Posiciones de los nodos después de la eliminación:", posiciones)
