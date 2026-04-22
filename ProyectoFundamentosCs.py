import sys

def principal():
    # Bucle infinito hasta encontrar la condición de quiebre
    while True:
        try:
            # Leemos la primera línea del bloque
            linea1 = input().strip()
        except EOFError:
            # Si se acaba el archivo de entrada repentinamente
            break 
            
        # Condición de salida del programa
        if linea1 == "FIN":
            break
            
        # Si no es FIN, leemos las otras 5 líneas correspondientes a este autómata
        try:
            linea2 = input().strip()
            linea3 = input().strip()
            linea4 = input().strip()
            linea5 = input().strip()
            linea6 = input().strip()
        except EOFError:
            break

        # Empaquetamos las líneas en una lista para pasarlas a la función validadora
        lineas_automata = [linea1, linea2, linea3, linea4, linea5, linea6]
        
        # Llamamos a la función que procesará este bloque en particular
        procesar_automata(lineas_automata)


def procesar_automata(lineas):
    """
    Recibe exactamente 6 líneas y se encarga de validarlas.
    Si todo está correcto, procederá a la computación.
    Si hay error, imprimirá "Error encontrado en [X]".
    """
    # Aquí irá toda nuestra lógica de validación (Fase 2)
    pass


if __name__ == "__main__":
    principal()