def num_paths(maze):
    if not maze or not maze[0]:
        return 0

    m, n = len(maze), len(maze[0])

    # Crear una matriz dp con las mismas dimensiones que el laberinto
    dp = [[0] * n for _ in range(m)]

    # Inicializar la posición de inicio
    dp[0][0] = 1 if maze[0][0] == 0 else 0

    # Llenar la primera fila
    for j in range(1, n):
        if maze[0][j] == 0:
            dp[0][j] = dp[0][j-1]

    # Llenar la primera columna
    for i in range(1, m):
        if maze[i][0] == 0:
            dp[i][0] = dp[i-1][0]

    # Llenar el resto de la matriz dp
    for i in range(1, m):
        for j in range(1, n):
            if maze[i][j] == 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    # La última celda contiene el número de maneras de llegar a la posición (m, n)
    return dp[-1][-1]

# Ejemplo de uso
maze = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0],
    [1, 1, 0, 0]
]

print(num_paths(maze))  # Salida esperada: 3
