def main():

    #Array de 1D: Una lista simple.
    numeritos = [1, 2, 3, 4, 5]
    print('Array 1D: ', numeritos)
    print('Primer valor', numeritos[0])

    #Matriz 2D: Lista anidada.
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print('Matriz 2D: ', matrix)
    # Acceder por filas y columnas
    print('Elemento[1][2]: ', matrix[1][2])

    #Generando matriz con ciclo for
    generarMatriz = [[fila * 5 + col for col in range(5)] for fila in range(5)]
    print(generarMatriz)

    print('Recorrido')
    for fila in matrix:
        for valor in fila:
            print(valor)
            
main()