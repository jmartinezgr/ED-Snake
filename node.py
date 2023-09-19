class PositionNode:
    def __init__(self, row, column):
        """
        Constructor de la clase PositionNode.

        :param row: La fila en la que se encuentra el nodo en la cuadrícula.
        :type row: int
        :param column: La columna en la que se encuentra el nodo en la cuadrícula.
        :type column: int
        """
        # Almacena la fila en la cuadrícula.
        self._row = row

        # Almacena la columna en la cuadrícula.
        self._column = column

        # El siguiente nodo en la cola (inicialmente se establece como None).
        self._nextNode = None

        # El nodo anterior en la cola (inicialmente se establece como None).
        self._previousNode = None

    @property
    def row(self):
        """
        Obtiene el valor de la fila en la cuadrícula.

        :return: El valor de la fila.
        :rtype: int
        """
        return self._row

    @row.setter
    def row(self, value):
        """
        Establece el valor de la fila en la cuadrícula.

        :param value: El nuevo valor de la fila.
        :type value: int
        """
        self._row = value

    @property
    def column(self):
        """
        Obtiene el valor de la columna en la cuadrícula.

        :return: El valor de la columna.
        :rtype: int
        """
        return self._column

    @column.setter
    def column(self, value):
        """
        Establece el valor de la columna en la cuadrícula.

        :param value: El nuevo valor de la columna.
        :type value: int
        """
        self._column = value

    @property
    def previousNode(self):
        """
        Obtiene el nodo anterior en la cola.

        :return: El nodo anterior.
        :rtype: PositionNode
        """
        return self._previousNode

    @previousNode.setter
    def previousNode(self, node):
        """
        Establece el nodo anterior en la cola.

        :param node: El nuevo nodo anterior.
        :type node: PositionNode
        """
        self._previousNode = node

        
    def position(self):
        """
        Obtiene la posición como una tupla (fila, columna) en la cuadrícula.

        :return: La posición como una tupla.
        :rtype: tuple[int, int]
        """
        return (self._row, self._column)
    
if __name__ == '__main__':
    # Crear nodos de prueba
    nodo1 = PositionNode(1, 2)
    nodo2 = PositionNode(3, 4)

    # Establecer el nodo anterior para nodo2
    nodo2.previousNode = nodo1

    # Imprimir las posiciones de los nodos
    print("Posición de nodo1:", nodo1.position())
    print("Posición de nodo2:", nodo2.position())

    # Imprimir el nodo anterior de nodo2
    if nodo2.previousNode:
        print("Posición del nodo anterior de nodo2:", nodo2.previousNode.position())
    else:
        print("Nodo anterior de nodo2 no está establecido.")
