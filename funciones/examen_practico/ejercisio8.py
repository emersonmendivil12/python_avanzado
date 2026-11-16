# 8. Closure (Clausura)
def crear_validador_limite(limite_maximo: int):
    """Retorna una función validadora que recuerda el límite máximo configurado."""
    def validar(numero: int | float) -> bool:
        return numero <= limite_maximo
    return validar

validador_100 = crear_validador_limite(100)
print("8a) ¿85 cumple el límite 100?:", validador_100(85))
print("8b) ¿120 cumple el límite 100?:", validador_100(120))