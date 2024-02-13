def identificar_cuadrilatero(lados):
    if len(set(lados)) == 1:
        return "cuadrado"
    elif len(set(lados)) == 2:
        return "rectangulo"
    else:
        return "cualquier otro cuadrilatero"
lados = [float(input(f"Medida del lado {i+1}: ")) for i in range(4)]
tipo_cuadrilatero = identificar_cuadrilatero(lados)
print(f"Lo que ingresaste es un{tipo_cuadrilatero}.")
    