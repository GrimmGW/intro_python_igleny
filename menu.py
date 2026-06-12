
def mostrar_condicionales():
    print('\n--- Opcion 3: Condicionales --- \n')
    print('Vamos a comparar los valores')
    
    nota = input('Escribe una nota del 0 al 20: ')
    notaFloat = float(nota)

    if notaFloat >= 18:
        print('Excelenteee')
    elif notaFloat >= 14:
        print('Muy bien, notable')
    elif notaFloat <= 13:
        print('Mejorable...')
    elif notaFloat <= 0:
        print('Ingresa un valor entre 0 y 20')
    else:
        print('Invalido')

    print('\nTambien se pueden usar condicionales con bool')
    tieneEntrada = input('Tienes una entrada para el cine? (s/n): ')
    tieneEntrada = tieneEntrada.lower()

    if tieneEntrada == 's':
        print('\nAdelante, disfruta de la peli.\n')
    else: 
        print('\nDebes comprar una entrada primero.\n')


def mostrar_input():
    print('\n--- Opcion 2: Inputs --- \n')
    print('¿Cómo te llamas?')
    nombre = input('Escribe tu nombre: ')

    print('¡Un placer, ' + nombre + '!\n')
    print('Y... ¿Cuántos años tienes?')
    edad = input('Escribe tu edad: ')
    print('Entonces... te llamas ' + nombre + ' y tienes ' + edad + ' años.')


def mostrar_menu():
    print('=' * 50)
    print('                 MENU DE OPCIONES')
    print('=' * 50)
    print(' 1. Variables')
    print(' 2. Input')
    print(' 3. Condicionales')
    print(' 4. Bucle')
    print(' 5. For i in range')
    print(' 0. Salir del programa')
    print(' ')


def main():
    while True:
        mostrar_menu()
        opcion = input('Elige una opcion: ')

        #Estructura de control: aqui vamos a revisar las opciones
        if opcion == '1':
            print('Mostrar Variables')
        elif opcion == '2':
            mostrar_input()
        elif opcion == '3':
            mostrar_condicionales()
        elif opcion == '4':
            print('Mostrar Bucles')
        elif opcion == '5':
            print('Mostrar for i in range')
        elif opcion == '0':
            print('\n Hasta luego!!!')
            break
        else:
            print()
            print('Opcion no valida, debes escribir un numero del 1 al 5.')
        
        input('Oprime ENTER para continuar.')
        print('Regresando al menu...')

main()