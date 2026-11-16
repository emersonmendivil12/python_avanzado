# 10. Programación Funcional (filter())
palabras: list[str] = ["sol", "computadora", "luz", "programacion", "ia", "python"]
palabras_largas: list[str] = list(filter(lambda palabra: len(palabra) > 4, palabras))

print("10)", palabras_largas)