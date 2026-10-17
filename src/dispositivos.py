# ==============================================================================
# Asignatura: Automatización de Infraestructura Digital I
# Práctica 3: Primer programa de Python para representar información de dispositivos
# Equipo: Juan Acevedo, Leslye Bello, Genesis Conde, Ehulises Araiza
# ==============================================================================

# ------------------------------------------------------------------------------
# PARTE 1, 2 Y 3: Representación individual con Variables y Diccionarios (Práctica 2)
# ------------------------------------------------------------------------------
# Datos recuperados de la Topología 2 de la Práctica 2:
# R1 (Router Cisco IOSv - IP: 10.1.1.1, Loopback: 1.1.1.1)
# R2 (Router Cisco IOSv - IP: 10.1.1.2, Loopback: 2.2.2.2)
# S1 (Switch Multicapa Cisco IOSvL2 - IP VLAN1: 10.1.1.3)

# ------------------------------------------------------------------------------
# PARTE 4 Y 5: Estructura de Datos (Lista de Diccionarios con Reto de Automatización)
# ------------------------------------------------------------------------------
dispositivos = [
    {
        "nombre": "R1",
        "tipo": "Router",
        "ip": "10.1.1.1",
        "loopback": "1.1.1.1",
        "interfaz": "GigabitEthernet0/0",
        "estado": "Fuera de servicio",
        "fabricante": "Cisco",          # Reto Parte 8: Dato extendido 1
        "protocolo": "OSPF"              # Reto Parte 8: Dato extendido 2
    },
    {
        "nombre": "R2",
        "tipo": "Router",
        "ip": "10.1.1.2",
        "loopback": "2.2.2.2",
        "interfaz": "GigabitEthernet0/0",
        "estado": "Activo",
        "fabricante": "Cisco",
        "protocolo": "OSPF"
    },
    {
        "nombre": "S1",
        "tipo": "Switch Multicapa",
        "ip": "10.1.1.3",
        "loopback": "N/A",
        "interfaz": "Vlan1",
        "estado": "Activo",
        "fabricante": "Cisco",
        "protocolo": "N/A"
    }
]

# ------------------------------------------------------------------------------
# PARTE 7 Y 8: Función para mostrar la información del dispositivo
# ------------------------------------------------------------------------------
def mostrar_dispositivo(dispositivo):
    """Muestra de manera organizada los detalles de un dispositivo de red."""
    print(f"Nombre:     {dispositivo['nombre']}")
    print(f"Tipo:       {dispositivo['tipo']}")
    print(f"IP:         {dispositivo['ip']}")
    print(f"Loopback:   {dispositivo['loopback']}")
    print(f"Interfaz:   {dispositivo['interfaz']}")
    print(f"Estado:     {dispositivo['estado']}")
    print(f"Fabricante: {dispositivo['fabricante']}")
    print(f"Protocolo:  {dispositivo['protocolo']}")
    
    # PARTE 6: Evaluación de estado (if/else)
    if dispositivo["estado"] == "Activo":
        print("Estatus:    El dispositivo está disponible.")
    else:
        print("Estatus:    El dispositivo requiere atención.")

# ------------------------------------------------------------------------------
# RETO FINAL: Función para buscar un dispositivo por su nombre
# ------------------------------------------------------------------------------
def buscar_dispositivo(nombre_buscado, lista_dispositivos):
    """Busca un dispositivo por nombre en la lista e imprime sus datos."""
    encontrado = False
    for dev in lista_dispositivos:
        # Se convierte a mayúsculas para evitar errores por minúsculas/mayúsculas
        if dev["nombre"].upper() == nombre_buscado.strip().upper():
            print("\n==========================================")
            print(f"   DISPOSITIVO ENCONTRADO: {dev['nombre']}")
            print("==========================================")
            mostrar_dispositivo(dev)
            encontrado = True
            break
            
    if not encontrado:
        print(f"\n[ERROR]: El dispositivo '{nombre_buscado}' no existe en la topología.")

# ------------------------------------------------------------------------------
# EJECUCIÓN DEL PROGRAMA
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    print("==================================================")
    print("   INVENTARIO DE DISPOSITIVOS DE RED (PRACTICA 3) ")
    print("==================================================\n")
    
    # Recorrer e imprimir todos los dispositivos de la lista
    for dev in dispositivos:
        mostrar_dispositivo(dev)
        print("-" * 40)

    # Prueba del Reto Final: Búsqueda interactiva de dispositivo
    print("\n--------------------------------------------------")
    busqueda = input("Ingrese el nombre del dispositivo a buscar (ej. R1, R2, S1): ")
    buscar_dispositivo(busqueda, dispositivos)