ventas = [
    [12, 15, 10, 18],
    [8, 14, 16, 12],
    [20, 18, 15, 22]
]

def mostrar_matriz(matriz):
    print("\nVENTAS REGISTRADAS (millones de pesos)")
    for i in range(len(matriz)):
        print("Vendedor", i + 1, end=": ")
        for j in range(len(matriz[i])):
            print("Semana", j + 1, "=", matriz[i][j], end="  ")
        print()

def analizar_ventas(matriz):
    totales_vendedores = []
    total_empresa = 0

    print("\n1. TOTAL DE VENTAS POR VENDEDOR")
    for i in range(len(matriz)):
        suma = 0
        for j in range(len(matriz[i])):
            suma += matriz[i][j]
        totales_vendedores.append(suma)
        total_empresa += suma
        print("Vendedor", i + 1, ":", suma, "millones")

    print("\n2. TOTAL DE VENTAS POR SEMANA")
    totales_semanas = []
    for j in range(len(matriz[0])):
        suma = 0
        for i in range(len(matriz)):
            suma += matriz[i][j]
        totales_semanas.append(suma)
        print("Semana", j + 1, ":", suma, "millones")

    mayor_vendedor = 0
    for i in range(1, len(totales_vendedores)):
        if totales_vendedores[i] > totales_vendedores[mayor_vendedor]:
            mayor_vendedor = i

    mayor_semana = 0
    for j in range(1, len(totales_semanas)):
        if totales_semanas[j] > totales_semanas[mayor_semana]:
            mayor_semana = j

    cantidad_datos = 0
    for fila in matriz:
        for valor in fila:
            cantidad_datos += 1

    promedio = total_empresa / cantidad_datos

    print("\n3. MAYOR TOTAL POR VENDEDOR")
    print("Vendedor", mayor_vendedor + 1, "con",
          totales_vendedores[mayor_vendedor], "millones")

    print("\n4. SEMANA CON MAYOR VOLUMEN DE VENTAS")
    print("Semana", mayor_semana + 1, "con",
          totales_semanas[mayor_semana], "millones")

    print("\n5. PROMEDIO GENERAL DE VENTAS")
    print(round(promedio, 2), "millones")

def modificar_venta(matriz):
    print("\nMODIFICAR UNA VENTA")
    vendedor = int(input("Ingrese el número de vendedor (1 a 3): "))
    while vendedor < 1 or vendedor > 3:
        print("Posición no válida.")
        vendedor = int(input("Ingrese el número de vendedor (1 a 3): "))

    semana = int(input("Ingrese el número de semana (1 a 4): "))
    while semana < 1 or semana > 4:
        print("Posición no válida.")
        semana = int(input("Ingrese el número de semana (1 a 4): "))

    nuevo_valor = float(input("Ingrese el nuevo valor de ventas: "))
    matriz[vendedor - 1][semana - 1] = nuevo_valor
    print("\nLa venta fue modificada correctamente.")

mostrar_matriz(ventas)
analizar_ventas(ventas)
modificar_venta(ventas)
print("\nMATRIZ Y RESULTADOS ACTUALIZADOS")
mostrar_matriz(ventas)
analizar_ventas(ventas)
