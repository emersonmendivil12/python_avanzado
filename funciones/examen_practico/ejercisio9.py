# 9. Programación Funcional (map())
precios: list[float] = [10.5, 20.0, 50.0, 5.99]
precios_incrementados: list[float] = list(map(lambda p: round(p * 1.10, 2), precios))

print("9)", precios_incrementados)