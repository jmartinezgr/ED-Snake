from node import PositionNode as Node

class LinkedList:
    def __init__(self):
        """
        Constructor de la clase LinkedList.
        Inicializa una lista doblemente enlazada vacía.
        """
        self._head = None
        self._current = None
        self._tail = None

    @property
    def head(self):
        """
        Obtiene el nodo principal de la lista.

        :return: El nodo principal.
        :rtype: Node
        """
        return self._head

    @property
    def current(self):
        """
        Obtiene el nodo actual de la lista.

        :return: El nodo actual.
        :rtype: Node
        """
        return self._current

    @property
    def tail(self):
        """
        Obtiene el nodo final de la lista.

        :return: El nodo final.
        :rtype: Node
        """
        return self._tail

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
            self._tail._nextNode = new_node
            self._tail = new_node

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
            current_node = current_node._nextNode
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

        current_node = self._head
        current_index = 0

        if index == 0:
            # Insertar al principio
            node._nextNode = self._head
            self._head._previousNode = node
            self._head = node
            if self._tail is None:
                self._tail = node
        else:
            while current_node is not None and current_index < index:
                current_node = current_node._nextNode
                current_index += 1

            if current_node is None and current_index < index:
                raise ValueError("El índice está fuera de rango")

            node._previousNode = current_node._previousNode
            node._nextNode = current_node
            if current_node._previousNode is not None:
                current_node._previousNode._nextNode = node
            current_node._previousNode = node

    def remove_at(self, index):
        """
        Elimina el nodo en una posición específica de la lista.

        :param index: La posición del nodo que se va a eliminar.
        :type index: int
        """
        if index < 0:
            raise ValueError("El índice debe ser mayor o igual a 0")

        current_node = self._head
        current_index = 0

        if index == 0:
            # Eliminar el primer nodo
            if self._head is not None:
                self._head = self._head._nextNode
                if self._head is not None:
                    self._head._previousNode = None
                else:
                    self._tail = None
        else:
            while current_node is not None and current_index < index:
                current_node = current_node._nextNode
                current_index += 1

            if current_node is None and current_index < index:
                raise ValueError("El índice está fuera de rango")

            if current_node._previousNode is not None:
                current_node._previousNode._nextNode = current_node._nextNode
            if current_node._nextNode is not None:
                current_node._nextNode._previousNode = current_node._previousNode

            if current_node == self._head:
                self._head = current_node._nextNode

            if current_node == self._tail:
                self._tail = current_node._previousNode

if __name__ == '__main__':
    lista = LinkedList()

    lista.append(1, 2)
    lista.append(3, 4)
    lista.append(5, 6)

    posiciones = lista.get_positions()

    print("Posiciones de los nodos en la lista:", posiciones)

    # Insertar un nuevo nodo en la posición 1
    nuevo_nodo = Node(7, 8)
    lista.insert_at(nuevo_nodo, 1)

    posiciones = lista.get_positions()

    print("Posiciones de los nodos después de la inserción:", posiciones)

    # Eliminar el nodo en la posición 1
    lista.remove_at(1)

    posiciones = lista.get_positions()

    print("Posiciones de los nodos después de la eliminación:", posiciones)
