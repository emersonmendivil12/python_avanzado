# crear un programa que me permita desarrollar las 4 operaciones basica 
# (suma, resta, division, multiplicacion)

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def mi_print(mensaje):
    texto = f"""

{mensaje}

"""
    print(texto)

mi_print(f"Suma: 45 + 70 = {sumar(45, 70)}")
mi_print(f"Resta: 70 - 45 = {restar(70, 45)}")
mi_print(f"Multiplicacion: 45 * 70 = {multiplicar(45, 70)}")
mi_print(f"Division: 70 / 45 = {dividir(70, 45)}")