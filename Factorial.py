from os import system

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def es_primo(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

def numeros_primos_en_rango(inicio, fin):
    lista_primos = []
    for num in range(inicio, fin + 1):
        if es_primo(num):
            lista_primos.append(num)
    return lista_primos

while True:
    print("Seleccione una opción:")
    print("1. Cálculo de factorial")
    print("2. Números primos en un rango")
    print("3. Salir")
    opcion = input("Ingrese el número de la opción que desea ejecutar: ")

    if opcion == "1":
        system("cls")
        num = int(input("Ingrese un número para calcular su factorial: "))
        print("El factorial de", num, "es", factorial(num))
    elif opcion == "2":
        system("cls")
        inicio = int(input("Ingrese el inicio del rango: "))
        fin = int(input("Ingrese el fin del rango: "))
        print("Los números primos en el rango", inicio, "-", fin, "son:", numeros_primos_en_rango(inicio, fin))
    elif opcion == "3":
        system("cls")
        print("Saliendo del programa...")
        break
    else:
        system("cls")
        print("Opción inválida. Por favor, ingrese una opción válida.")