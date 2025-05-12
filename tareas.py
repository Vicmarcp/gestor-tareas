# Función agregar tarea
def agregar_tarea(lista, tarea):
    lista.append(tarea)
    return lista


# Función listar tarea
def listar_tareas(lista):
    for i, t in enumerate(lista, 1):
        print(f"{i}. {t}")


# Funnción eliminar tarea
def eliminar_tarea(lista, indice):
    if 0 <= indice < len(lista):
        lista.pop(indice)
        return lista
    else:
        print("Índice inválido")