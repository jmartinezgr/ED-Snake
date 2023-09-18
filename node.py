class PositionNode:
    def __init__(self, fila, columna):
        """
        Constructor de la clase PositionNode.

        :param fila: La fila en la que se encuentra el nodo en el grid.
        :type fila: int
        :param columna: La columna en la que se encuentra el nodo en el grid.
        :type columna: int
        """
        # Almacena la fila en el grid.
        self._fila = fila

        # Almacena la columna en el grid.
        self._columna = columna

        # El siguiente nodo en la cola (inicialmente se establece como None).
        self._nextNode = None

    @property
    def fila(self):
        """
        Obtiene el valor de la fila en el grid.

        :return: El valor de la fila.
        :rtype: int
        """
        return self._fila

    @fila.setter
    def fila(self, valor):
        """
        Establece el valor de la fila en el grid.

        :param valor: El nuevo valor de la fila.
        :type valor: int
        """
        self._fila = valor

    @property
    def columna(self):
        """
        Obtiene el valor de la columna en el grid.

        :return: El valor de la columna.
        :rtype: int
        """
        return self._columna

    @columna.setter
    def columna(self, valor):
        """
        Establece el valor de la columna en el grid.

        :param valor: El nuevo valor de la columna.
        :type valor: int
        """
        self._columna = valor
