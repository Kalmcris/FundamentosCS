#Trabajo Práctico 1 - Fundamentos de la Computación
#Integrantes: Martin Salamanca, Joaquín González, Pablo Rojas, Cristian Osses

def obtener_clausura_epsilon(estados, transiciones):
    """
    Calcula todos los estados a los que se puede llegar consumiendo
    únicamente la palabra vacía ('#').
    """
    clausura = set(estados)
    pila = list(estados)

    while pila:
        actual = pila.pop()
        # Si el estado tiene transiciones y existe una con '#'
        if actual in transiciones and "#" in transiciones[actual]:
            for estado_destino in transiciones[actual]["#"]:
                if estado_destino not in clausura:
                    clausura.add(estado_destino)
                    pila.append(estado_destino)
    return clausura


def procesar_automata(lineas):
    l_estados, l_alfabeto, l_inicial, l_finales, l_transiciones, l_palabra = lineas
    caracteres_prohibidos = ["#", "'", '"', ","]

    # Línea 1: Estados
    for char in caracteres_prohibidos:
        if char in l_estados:
            print("Error encontrado en 1")
            return
    estados = l_estados.split()

    # Línea 2: Alfabeto
    for char in caracteres_prohibidos:
        if char in l_alfabeto:
            print("Error encontrado en 2")
            return
    alfabeto = l_alfabeto.split()

    # Línea 3: Estado inicial
    estado_inicial = l_inicial.strip()
    if estado_inicial not in estados:
        print("Error encontrado en 3")
        return

    # Línea 4: Estados finales
    estados_finales = l_finales.split()
    for estado in estados_finales:
        if estado not in estados:
            print("Error encontrado en 4")
            return

    # Línea 5: Transiciones
    transiciones = {}
    transiciones_crudas = l_transiciones.split()

    for t in transiciones_crudas:
        # Validar formato (A,0,B)
        if not (t.startswith("(") and t.endswith(")")):
            print("Error encontrado en 5")
            return

        contenido = t[1:-1].split(",")
        if len(contenido) != 3:
            print("Error encontrado en 5")
            return

        origen, simbolo, destino = contenido

        if origen not in estados or destino not in estados:
            print("Error encontrado en 5")
            return
        if simbolo != "#" and simbolo not in alfabeto:
            print("Error encontrado en 5")
            return

        # Guardar en diccionario
        if origen not in transiciones:
            transiciones[origen] = {}
        if simbolo not in transiciones[origen]:
            transiciones[origen][simbolo] = []
        transiciones[origen][simbolo].append(destino)

    # Línea 6: Palabra a procesar
    palabra = l_palabra.strip()
    if palabra == "#":
        palabra = ""  
    else:
        for char in palabra:
            if char not in alfabeto and char != "#":
                print("Error encontrado en 6")
                return

    estados_actuales = obtener_clausura_epsilon({estado_inicial}, transiciones)

    for i in range(len(palabra) + 1):
        mitad_izq = palabra[:i]
        mitad_der = palabra[i:]
        estados_str = "".join(sorted(list(estados_actuales)))

        print(f"{mitad_izq}_{mitad_der} {estados_str}".strip())

        # Si llega al final de la palabra, rompe el ciclo
        if i == len(palabra):
            break

        char = palabra[i]
        siguientes_estados = set()

        for estado in estados_actuales:
            if estado in transiciones and char in transiciones[estado]:
                for dest in transiciones[estado][char]:
                    siguientes_estados.add(dest)

        estados_actuales = obtener_clausura_epsilon(siguientes_estados, transiciones)

    # Finalmente, verificamos si alguno de los estados actuales es un estado final
    if estados_actuales.intersection(set(estados_finales)):
        print("Aceptado")
    else:
        print("Rechazado")


def principal():
    while True:
        try:
            linea1 = input().strip()
        except EOFError:
            break

        if linea1 == "FIN":
            break

        try:
            linea2 = input().strip()
            linea3 = input().strip()
            linea4 = input().strip()
            linea5 = input().strip()
            linea6 = input().strip()
        except EOFError:
            break

        procesar_automata([linea1, linea2, linea3, linea4, linea5, linea6])


if __name__ == "__main__":
    principal()

