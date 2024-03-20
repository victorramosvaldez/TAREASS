def crear_espiral(n):
    espiral = [[None] * n for _ in range(n)]
    x, y = 0, 0
    dx, dy = 1, 0
    for num in range(1, n*n + 1):
        espiral[y][x] = num
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and espiral[ny][nx] == None:
            x, y = nx, ny
        else:
            dx, dy = -dy, dx
            x, y = x + dx, y + dy

    for fila in espiral:
        print(' '.join(str(num) for num in fila))


tamaño = int(input("ingresar numero: "))
crear_espiral(tamaño)