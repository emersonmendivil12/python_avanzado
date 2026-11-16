# 4. Empaquetado Posicional (*args)
def unir_frases(*args: str) -> str:
    """Une una cantidad variable de cadenas en una sola oración."""
    return " ".join(args)

print("4)", unir_frases("Python", "es", "un", "lenguaje", "poderoso"))