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
        self.fila = fila

        # Almacena la columna en el grid.
        self.columna = columna

        # El siguiente nodo en la cola (inicialmente se establece como None).
        self.nextNode = None
