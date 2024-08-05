"""
Programa para verificar la longitud de una palabra y encontrar el cuadrante de un punto
Autor: Manuel BG
"""

# Función para verificar si la longitud de una palabra está dentro del rango permitido


def verificar_longitud_palabra(palabra):
    longitud = len(palabra)  # Calculamos la longitud de la palabra ingresada
    if 4 <= longitud <= 8:
        # Si la longitud está entre 4 y 8 caracteres, está bien
        print("La palabra es correcta.")
    elif longitud < 4:
        # Si la longitud es menor a 4, faltan letras
        print(f"Hacen falta letras. Solo tiene {longitud} letras.")
    else:
        # Si la longitud es mayor a 8, hay letras de más
        print(f"Sobran letras. Tiene {longitud} letras.")


# Función para encontrar el cuadrante en el plano cartesiano basado en coordenadas (x, y)
def encontrar_cuadrante(x, y):
    if x == 0 or y == 0:
        # Las coordenadas no pueden ser cero para determinar un cuadrante válido
        print("Las coordenadas no pueden ser cero.")
    elif x > 0 and y > 0:
        # Coordenadas en el primer cuadrante (x positivo, y positivo)
        print("El punto se encuentra en el cuadrante I")
    elif x < 0 and y > 0:
        # Coordenadas en el segundo cuadrante (x negativo, y positivo)
        print("El punto se encuentra en el cuadrante II")
    elif x < 0 and y < 0:
        # Coordenadas en el tercer cuadrante (x negativo, y negativo)
        print("El punto se encuentra en el cuadrante III")
    elif x > 0 and y < 0:
        # Coordenadas en el cuarto cuadrante (x positivo, y negativo)
        print("El punto se encuentra en el cuadrante IV")


# Ejemplo de uso para el primer programa: verificar la longitud de una palabra
print("Ejercicio 1: Longitud de una palabra")
# Pedimos al usuario que ingrese una palabra
palabra_ingresada = input("Ingresa una palabra: ")
# Llamamos a la función para verificar la longitud
verificar_longitud_palabra(palabra_ingresada)


# Ejemplo de uso para el segundo programa: encontrar el cuadrante de un punto
print("\nEjercicio 2: Encuentra el cuadrante")
# Pedimos al usuario que ingrese la coordenada X
x = int(input("Ingrese X: "))
# Pedimos al usuario que ingrese la coordenada Y
y = int(input("Ingrese Y: "))
# Llamamos a la función para determinar el cuadrante
encontrar_cuadrante(x, y)
