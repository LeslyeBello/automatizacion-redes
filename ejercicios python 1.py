producto = input("Nombre del producto: ")
precio = float(input("Precio unitario: "))
unidades = int(input("Número de unidades: "))
coste = precio * unidades
print(f"Producto: {producto}")
print(f"Precio unitario: {precio:09.2f}")
print(f"Unidades: {unidades:03d}")
print(f"Coste total: {coste:011.2f}")