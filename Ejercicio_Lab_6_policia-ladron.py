def policiaLadron(arr, n, k):
    i = 0
    l = 0
    r = 0
    res = 0
    ladrones = []
    policias = []

    # Almacenar índices en listas
    while i < n:
        if arr[i] == 'P':
            policias.append(i)
        elif arr[i] == 'T':
            ladrones.append(i)
        i += 1

    # Rastrear los índices actuales más bajos de ladrones: ladrones[l], policías: policias[r]
    while l < len(ladrones) and r < len(policias):

        # Puede ser atrapado
        if (abs(ladrones[l] - policias[r]) <= k):
            res += 1
            l += 1
            r += 1

        # Incrementar el índice mínimo
        elif ladrones[l] < policias[r]:
            l += 1
        else:
            r += 1

    return res


# Programa principal
if __name__ == '__main__':
    arr1 = ['P', 'T', 'T', 'P', 'T']
    k = 2
    n = len(arr1)
    print(("Máximo de ladrones atrapados: {}".
        format(policiaLadron(arr1, n, k))))

    arr2 = ['T', 'T', 'P', 'P', 'T', 'P']
    k = 2
    n = len(arr2)
    print(("Máximo de ladrones atrapados: {}".
        format(policiaLadron(arr2, n, k))))

    arr3 = ['P', 'T', 'P', 'T', 'T', 'P']
    k = 3
    n = len(arr3)
    print(("Máximo de ladrones atrapados: {}".
        format(policiaLadron(arr3, n, k))))