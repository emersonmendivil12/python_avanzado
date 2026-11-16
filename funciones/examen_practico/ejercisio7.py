# 7. Documentación (docstring)
def calcular_potencia(base: float, exponente: float) -> float:
    """
    Calcula el resultado de elevar una base a un exponente dado.

    Parámetros:
        base (float): El número base que se desea elevar.
        exponente (float): El exponente al que se elevará la base.

    Restricciones:
        - El exponente no debe ser negativo (exponente >= 0).
        - Ambos parámetros deben ser valores numéricos válidos.

    Retorna:
        float: El resultado de la operación base ** exponente como número de punto flotante.
    """
    if exponente < 0:
        raise ValueError("El exponente no debe ser negativo.")
    return float(base ** exponente)

print("7)", calcular_potencia(3.0, 4.0))