class PositionNode:
    def __init__(self, row, column):
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
        return self._row

    @row.setter
    def row(self, value):
        self._row = value

    @property
    def column(self):
        return self._column

    @column.setter
    def column(self, value):
        self._column = value

    @property
    def nextNode(self):
        return self._nextNode
    
    @nextNode.setter
    def nextNode(self, node):
        self._nextNode = node

    @property
    def previousNode(self):
        return self._previousNode

    @previousNode.setter
    def previousNode(self, node):
        self._previousNode = node
        
    def position(self):
        return (self._row, self._column)
    
    def __add__ (self, other):
        return PositionNode(self._row + other._row, self._column + other._column)
    
    def __eq__(self,other):
        return self._row == other._row and self._column == other._column
