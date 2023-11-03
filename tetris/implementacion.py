class Tetromino:
    def __init__(self, forma):
        self.forma = forma
        self.rotacion = 0

    def rotar(self):
        # Obtener las dimensiones de la forma del tetromino
        filas = len(self.forma)
        columnas = len(self.forma[0])

        # Crear una nueva matriz vacía con las dimensiones rotadas
        nueva_forma = [[' ' for _ in range(filas)] for _ in range(columnas)]

        # Realizar la rotación en sentido horario
        for i in range(filas):
            for j in range(columnas):
                nueva_forma[j][filas - 1 - i] = self.forma[i][j]

        # Actualizar la forma del tetromino con la nueva forma rotada
        self.forma = nueva_forma

    def formas(self, nueva):
        return self.forma == nueva.forma and self.rotacion == nueva.rotacion

    def mostrar_tetromino(self):
        for fila in self.forma:
            for columna in fila:
                if columna == '@':
                    print('@', end=' ')
                else:
                    print('.', end=' ')
            print()

    def igual(self, otro):
        # Comprueba si dos tetrominós son iguales en su rotación actual
        return self.formas(otro) and self.rotacion == otro.rotacion

    def semejante(self, otro):
        # Comprueba si dos tetrominós son semejantes en al menos una de sus rotaciones
        for _ in range(4):
            if self.igual(otro):
                return True
            otro.rotar()
        return False

    def guardar_estado_en_archivo(self, nombre_archivo):
        # Guardar el estado actual del tetrominó en un archivo
        with open(nombre_archivo, 'w') as archivo:
            for fila in self.forma:
                for columna in fila:
                    archivo.write(columna)
                archivo.write('\n')


tI = Tetromino([
    ['.', '.', '@', '.'],
    ['.', '.', '@', '.'],
    ['.', '.', '@', '.'],
    ['.', '.', '@', '.']])

tO = Tetromino([
    ['.', '.', '.', '.'],
    ['.', '@', '@', '.'],
    ['.', '@', '@', '.'],
    ['.', '.', '.', '.'], ])

tT = Tetromino([
    ['.', '.', '.', '.'],
    ['.', '@', '@', '@'],
    ['.', '.', '@', '.'],
    ['.', '.', '.', '.']])

tS = Tetromino([
    ['.', '.', '.', '.'],
    ['.', '.', '@', '@'],
    ['.', '@', '@', '.'],
    ['.', '.', '.', '.'], ])

tZ = Tetromino([
    ['.', '.', '.', '.'],
    ['.', '@', '@', '.'],
    ['.', '.', '@', '@'],
    ['.', '.', '.', '.'], ])

tJ = Tetromino([
    ['.', '.', '@', '.'],
    ['.', '.', '@', '.'],
    ['.', '@', '@', '.'],
    ['.', '.', '.', '.'], ])

tL = Tetromino([
    ['.', '@', '.', '.'],
    ['.', '@', '.', '.'],
    ['.', '@', '@', '.'],
    ['.', '.', '.', '.'], ])

# Pide al usuario la letra del tetromino y la cantidad de rotaciones
letra = input("Elije una letra de Tetromino (I, O, T, S, Z, J, L): ").upper()
rotaciones = int(input("¿Cuántas veces deseas rotarla (1-4)? "))

# Diccionario para mapear la letra ingresada con el objeto Tetromino correspondiente
tetrominos = {
    'I': tI,
    'O': tO,
    'T': tT,
    'S': tS,
    'Z': tZ,
    'J': tJ,
    'L': tL,
}

if letra in tetrominos:
    tetromino = tetrominos[letra]

    if rotaciones < 1 or rotaciones > 4:
        print("El número de rotaciones debe estar entre 1 y 4.")
    else:
        print(f"Tetromino {letra} en su forma inicial:")
        tetromino.mostrar_tetromino()

        igualdad_en_rotacion_actual = False
        semejanza_en_alguna_rotacion = False

        for i in range(rotaciones):
            tetromino.rotar()
            print(f"Rotación {i + 1}:")
            tetromino.mostrar_tetromino()

            # Comprobar igualdad en la rotación actual
            if i == 0 and tetromino.igual(tetrominos[letra]):
                igualdad_en_rotacion_actual = True

            # Comprobar semejanza en la rotación actual o cualquier rotación anterior
            if tetromino.semejante(tetrominos[letra]):
                semejanza_en_alguna_rotacion = True

        # Aquí es donde se muestra si son iguales o semejantes
        if igualdad_en_rotacion_actual:
            print("Los tetrominós son iguales en la rotación actual.")
        else:
            print("Los tetrominós no son iguales en la rotación actual.")

        if semejanza_en_alguna_rotacion:
            print("Los tetrominós son semejantes en al menos una de sus rotaciones.")
        else:
            print("Los tetrominós no son semejantes en ninguna de sus rotaciones.")

        nombre_archivo = f"{letra}_estado.txt"
        tetromino.guardar_estado_en_archivo(nombre_archivo)
        print(f"El estado del tetromino se ha guardado en el archivo {nombre_archivo}")
else:
    print(f"La letra {letra} no es válida. Debes elegir entre I, O, T, S, Z, J, o L.")