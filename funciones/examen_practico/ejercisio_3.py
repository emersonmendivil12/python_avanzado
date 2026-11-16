# 3. Type-hints (anotaciones estrictas)
def obtener_promedio(numeros: list[int]) -> float:
    """Retorna el promedio de una lista de enteros como float.

    Parámetros:
        numeros (list[int]): lista de números enteros, no vacía.

    Restricciones:
        La lista no debe estar vacía; si lo está, se lanza ValueError.

    Retorna:
        float: el promedio de los valores de la lista.
    """
    if not numeros:
        raise ValueError("La lista no debe estar vacía.")
    return float(sum(numeros) / len(numeros))

print("3) Promedio [4, 8, 15, 16]:", obtener_promedio([4, 8, 15, 16]))