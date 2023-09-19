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

    def position(self):
        """
        Obtiene la posición como una tupla (fila, columna) en la cuadrícula.

        :return: La posición como una tupla.
        :rtype: tuple[int, int]
        """
        return (self._row, self._column)
