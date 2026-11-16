#1. Funciones Básicas Crea una función llamada calcular_area_rectangulo que reciba la
#base y la altura de un rectángulo (números enteros o flotantes)
#y retorne su área calculada. Pruébala llamándola con dos valores distintos e imprime el resultado. 
# 1. Funciones Básicas
def calcular_area_rectangulo(base, altura):
    """Calcula el área de un rectángulo."""
    return base * altura

print("1) Área 5x3 =", calcular_area_rectangulo(5, 3))
print("   Área 7.5x2.5 =", calcular_area_rectangulo(7.5, 2.5))