def imprimir_laberinto(laberinto, inicio, fin):
    print("Laberinto original:")
    for i in range(len(laberinto)):
        fila_texto = []
        for j in range(len(laberinto[0])):
            if (i, j) == inicio:
                fila_texto.append("I")
            elif (i, j) == fin:
                fila_texto.append("F")
            else:
                fila_texto.append(str(laberinto[i][j]))
        print(" ".join(fila_texto))
    print()


def imprimir_matriz_camino(matriz_camino):
    print("Matriz que indica cómo salir:")
    for fila in matriz_camino:
        print(" ".join(str(valor) for valor in fila))


def buscar_camino(laberinto, fila, columna, fin, energia, visitado, matriz_camino):
    if (fila, columna) == fin:
        matriz_camino[fila][columna] = 1
        return True

    visitado[fila][columna] = True
    matriz_camino[fila][columna] = 1

    movimientos = [(0, -1), (1, 0), (-1, 0), (0, 1)]

    for df, dc in movimientos:
        nf = fila + df
        nc = columna + dc

        if 0 <= nf < len(laberinto) and 0 <= nc < len(laberinto[0]) and not visitado[nf][nc]:
            if laberinto[nf][nc] == 99:
                continue

            costo = laberinto[nf][nc]
            nueva_energia = energia

            if costo > 0:
                nueva_energia -= costo
            elif costo < 0:
                nueva_energia += abs(costo)

            if nueva_energia < 0:
                continue

            if buscar_camino(laberinto, nf, nc, fin, nueva_energia, visitado, matriz_camino):
                return True

    matriz_camino[fila][columna] = 0
    visitado[fila][columna] = False
    return False


def resolver_laberinto():
    laberinto = [
        [1, 1, 1, 1, 99, 1, 1, 1, 0],
        [1, 99, 99, 1, 99, 1, 99, 1, 99],
        [1, 1, 99, 1, 1, 1, 99, 1, 99],
        [99, 1, 99, 1, 99, 99, 99, 1, 99],
        [1, 1, 99, -1, 1, 1, 1, 3, 99],
        [-2, 99, 99, 1, 99, 99, 99, 1, 1],
        [1, 99, 1, -1, 1, 1, 1, 1, 99],
        [1, 99, 99, 99, 99, 2, 99, 1, 99],
        [0, 1, 3, 1, 1, 1, 99, 1, 1],
    ]

    inicio = (0, 8)
    fin = (8, 0)
    energia_inicial = 18

    imprimir_laberinto(laberinto, inicio, fin)

    filas = len(laberinto)
    columnas = len(laberinto[0])
    visitado = [[False] * columnas for _ in range(filas)]
    matriz_camino = [[0] * columnas for _ in range(filas)]

    exito = buscar_camino(laberinto, inicio[0], inicio[1], fin, energia_inicial, visitado, matriz_camino)

    if exito:
        print("Se logró llegar a la salida con la energía disponible.")
    else:
        print("No se logró llegar a la salida con la energía disponible.")

    imprimir_matriz_camino(matriz_camino)


if __name__ == "__main__":
    resolver_laberinto()
