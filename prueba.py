from linkedList import LinkedList

lista = LinkedList()

print(lista.get_positions())

lista.insert_at(6,7,0)
#lista.insert_at(7,6)
print(lista.get_positions())

lista.remove_at(lista.size-1)
print(lista.get_positions())