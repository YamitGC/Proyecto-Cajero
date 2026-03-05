from database.users import cuentas

def registrar_movimiento(usuario, tipo, monto):
    # Solo guardamos el texto del movimiento
    movimiento = f"{tipo}: ${monto:.2f}"
    # Buscamos la lista 'historial' dentro del diccionario del usuario
    cuentas[usuario]["historial"].append(movimiento)

def consultar_historial(usuario):
    print(f"\n--- HISTORIAL DE MOVIMIENTOS ---")
    print(f"Usuario: {usuario.upper()}")
    
    movimientos = cuentas[usuario].get("historial", [])
    
    if not movimientos:
        print("No hay movimientos registrados aún.")
    else:
        for i, m in enumerate(movimientos, 1):
            print(f"{i}. {m}")

def consultar_saldo(usuario):
    # Accedemos a la base de datos para obtener el saldo actual
    # Usamos .get() por seguridad, aunque ya sabemos que el usuario existe por el auth
    saldo = cuentas[usuario]["saldo"]
    
    print("\n" + "="*30)
    print(f"       ESTADO DE CUENTA")
    print("="*30)
    print(f"Cliente: {usuario.upper()}")
    print(f"Saldo disponible: ${saldo:.2f}")
    print("="*30)

def depositar_dinero(usuario):
    try:
        print(f"\n--- DEPÓSITO ---")
        monto = float(input("¿Cuánto deseas depositar?: "))

        # 1. Validar que no sea negativo o cero
        if monto <= 0:
            print("Error: El monto debe ser una cantidad positiva.")
        
        # 2. Validar un límite máximo por depósito (Ejemplo: 10,000)
        elif monto > 10000:
            print("Error: Por seguridad, no puedes depositar más de $10,000 por transacción.")
        
        else:
            # Si pasa las pruebas, procedemos
            cuentas[usuario]["saldo"] += monto
            registrar_movimiento(usuario, "DEPÓSITO", monto)
            
            print(f"✅ ¡Depósito exitoso!")
            print(f"Nuevo saldo: ${cuentas[usuario]['saldo']:.2f}")

    except ValueError:
        print("Error: Entrada inválida. Por favor, ingresa solo números (ej: 100.50).")

def retirar_dinero(usuario):
    try:
        monto = float(input("¿Cuánto deseas retirar?: "))
        saldo_actual = cuentas[usuario]["saldo"]
        
        if 0 < monto <= saldo_actual:
            cuentas[usuario]["saldo"] -= monto
            # REGISTRO EN EL HISTORIAL
            registrar_movimiento(usuario, "RETIRO", monto)
            print(f"Retiro exitoso. Saldo restante: ${cuentas[usuario]['saldo']:.2f}")
        elif monto > saldo_actual:
            print("Error: Fondos insuficientes.")
        else:
            print("Error: El monto debe ser mayor a 0.")
    except ValueError:
        print("Error: Entrada inválida.")