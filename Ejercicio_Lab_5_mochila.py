def mochila_fraccionaria(items, capacidad):
    # Calcular ratio (beneficio / peso) para cada elemento
    for item in items:
        item.append(item[0] / item[1])

    # Ordenar elementos por ratio de forma decreciente
    items.sort(key=lambda x: x[2], reverse=True)

    # Inicializar resultado y peso total
    resultado = 0
    peso_total = capacidad

    # Iterar sobre los elementos ordenados
    for item in items:
        # Si el peso del elemento es menor que el peso disponible
        if item[1] <= peso_total:
            resultado += item[0]  # Agregar valor del articulo a resultado
            peso_total -= item[1]  # Restar peso del elemento de peso total
        else:
            # Calcular fraccion del articulo a agregar
            fraccion = peso_total / item[1]
            resultado += item[0] * fraccion  # Agregar fraccion del valor del articulo
            peso_total = 0  # La mochila esta llena, salir del bucle
            break

    return resultado

# Ejemplo de uso
items = [[60, 10], [100, 20], [120, 30],[140, 20]]  # Formato de los elementos: [beneficio, peso]
capacidad = 80
resultado = mochila_fraccionaria(items, capacidad)
print("El beneficio maximo obtenido es:", resultado)
