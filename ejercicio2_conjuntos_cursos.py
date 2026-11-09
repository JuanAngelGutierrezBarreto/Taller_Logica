curso_A = {
    "Ana", "Carlos", "Laura", "Pedro",
    "Sofia", "Andres", "Camila"
}

curso_B = {
    "Laura", "Pedro", "Daniel", "Sofia",
    "Mateo", "Valentina"
}

def mostrar_resultados(conjunto_A, conjunto_B):
    print("\nESTUDIANTES DEL CURSO A:")
    print(sorted(conjunto_A))

    print("\nESTUDIANTES DEL CURSO B:")
    print(sorted(conjunto_B))

    todos = conjunto_A | conjunto_B
    ambos = conjunto_A & conjunto_B
    solo_A = conjunto_A - conjunto_B
    solo_B = conjunto_B - conjunto_A
    exactamente_uno = conjunto_A ^ conjunto_B

    print("\nCANTIDAD DE ESTUDIANTES DIFERENTES:")
    print(len(todos))

    print("\nESTUDIANTES EN AMBOS CURSOS:")
    print(sorted(ambos))

    print("\nESTUDIANTES SOLAMENTE EN EL CURSO A:")
    print(sorted(solo_A))

    print("\nESTUDIANTES SOLAMENTE EN EL CURSO B:")
    print(sorted(solo_B))

    print("\nESTUDIANTES INSCRITOS EN EXACTAMENTE UN CURSO:")
    print(sorted(exactamente_uno))

    print("\n¿TODOS LOS ESTUDIANTES DEL CURSO A TAMBIÉN ESTÁN EN B?")
    print(conjunto_A.issubset(conjunto_B))

def agregar_estudiante(conjunto_A, conjunto_B):
    print("\nAGREGAR UN ESTUDIANTE")
    curso = input("¿A qué curso desea agregarlo? (A o B): ").upper()

    while curso != "A" and curso != "B":
        print("Opción no válida.")
        curso = input("Escriba A o B: ").upper()

    nombre = input("Ingrese el nombre del estudiante: ").strip()

    while nombre == "":
        print("El nombre no puede estar vacío.")
        nombre = input("Ingrese el nombre del estudiante: ").strip()

    if curso == "A":
        conjunto_A.add(nombre)
    else:
        conjunto_B.add(nombre)

    print("Estudiante agregado. Si ya estaba inscrito, el conjunto no lo duplica.")

mostrar_resultados(curso_A, curso_B)
agregar_estudiante(curso_A, curso_B)
print("\nRESULTADOS ACTUALIZADOS")
mostrar_resultados(curso_A, curso_B)
