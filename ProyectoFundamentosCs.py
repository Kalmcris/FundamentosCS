import sys

def principal():
    while True:
        try:
            linea1 = input().strip()
        except EOFError:
            break 
            
        # Condición de salida del programa
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
        
        lineas_automata = [linea1, linea2, linea3, linea4, linea5, linea6]
        
        
        procesar_automata(lineas_automata)


def procesar_automata(lineas):
    """
    Recibe exactamente 6 líneas y se encarga de validarlas.
    Si todo está correcto, procederá a la computación.
    Si hay error, imprimirá "Error encontrado en [X]".
    """
    pass


if __name__ == "__main__":
    principal()