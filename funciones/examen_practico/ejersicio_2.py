# 2. Parámetros Nominales y por Defecto
def calcular_precio_final(precio, impuesto=0.18, descuento=0.0):
    """Calcula el precio final aplicando impuesto y descuento."""
    precio_con_descuento = precio * (1 - descuento)
    return precio_con_descuento * (1 + impuesto)

# Argumento nominal: solo se pasa descuento, el impuesto usa su valor por defecto
print("2) Precio final (100, descuento 5%):", calcular_precio_final(100, descuento=0.05))