# 5. Empaquetado Nominal (**kwargs)
def generar_perfil_usuario(**kwargs: str | int) -> str:
    """Recorre los datos clave-valor recibidos y construye una descripción del usuario."""
    lineas = [f"- {clave.capitalize()}: {valor}" for clave, valor in kwargs.items()]
    return "Perfil de usuario:\n" + "\n".join(lineas)

print("5)", generar_perfil_usuario(nombre="Lucía", edad=28, pais="Perú", profesion="Ingeniera"))