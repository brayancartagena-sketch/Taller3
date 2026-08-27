print("CALCULADORA BASICA")
print("---------------------------")
print("Seleccione la operación que desea realizar:")
print("0. Salir")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Porcentaje")

while True:
    try:
        opcion = int(input("Ingrese el número de la operación (0-5): "))
        if opcion not in [0, 1, 2, 3, 4, 5]:
            print("Opción inválida. Por favor, seleccione una opción del 0 al 5.")
            continue
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número del 0 al 5.")

    match opcion:
        case 0:
            print("Saliendo de la calculadora.")
            break
        case 1:
            from Suma import suma
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            resultado = suma(a, b)
            print(f"El resultado de la suma es: {resultado}")
        case 2:
            from Resta import resta
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            resultado = resta(a, b)
            print(f"El resultado de la resta es: {resultado}")
        case 3:
            from Multiplicacion import multiplicacion
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            resultado = multiplicacion(a, b)
            print(f"El resultado de la multiplicación es: {resultado}")
        case 4:
            from Division import division
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            try:
                resultado = division(a, b)
                print(f"El resultado de la división es: {resultado}")
            except ValueError as e:
                print(e)
        case 5:
            from Porcentaje import porcentaje
            a = float(input("Ingrese el número: "))
            b = float(input("Ingrese el porcentaje: "))
            resultado = porcentaje(a, b)
            print(f"El {b}% de {a} es: {resultado}")



        

