# 🏧 Sistema de Cajero Automático en Python

> Proyecto que simula el funcionamiento básico de un **cajero
> automático (ATM)** usando Python.\
> Incluye autenticación de usuario, gestión de saldo, depósitos, retiros
> y registro de movimientos.

------------------------------------------------------------------------

## 📌 Descripción del proyecto

Este proyecto implementa un **sistema de cajero automático en consola**
que permite a los usuarios autenticarse mediante usuario y PIN, y
posteriormente realizar diferentes operaciones bancarias.

Entre las funcionalidades principales se incluyen:

-   Autenticación de usuario
-   Consulta de saldo
-   Depósitos
-   Retiros
-   Historial de transacciones
-   Interfaz de menú interactiva
-   Simulación de carga con barra de progreso

El sistema está organizado en **módulos**, siguiendo buenas prácticas de
programación para mantener el código limpio y escalable.

------------------------------------------------------------------------

# 📂 Estructura del proyecto

    project/
    │
    ├── main.py
    │
    ├── database/
    │   └── users.py
    │
    ├── app/
    │   ├── auth.py
    │   ├── menu.py
    │   ├── logica_atm.py
    │   ├── progress_bar.py
    │   └── clean_screen.py
    │
    └── README.md

### Descripción de los archivos

  Archivo             Descripción
  ------------------- ------------------------------------
  `main.py`           Punto de entrada del programa
  `users.py`          Base de datos simulada de usuarios
  `auth.py`           Sistema de autenticación
  `menu.py`           Menú principal del cajero
  `logica_atm.py`     Lógica de operaciones bancarias
  `progress_bar.py`   Simulación de barra de carga
  `clean_screen.py`   Limpieza de pantalla en consola

------------------------------------------------------------------------

# ⚙️ Funcionamiento del sistema

## 1. Inicio del programa

El programa comienza ejecutando `main.py`, que:

1.  Carga la base de datos de usuarios.
2.  Ejecuta el sistema de autenticación.
3.  Si el usuario se autentica correctamente, muestra el menú principal.

``` python
def iniciar_programa():
    print("=== BIENVENIDO AL CAJERO AUTOMÁTICO V2 ===")
    
    usuario_autenticado = auth(cuentas) 
    
    if usuario_autenticado:
        menu(usuario_autenticado)
    else:
        print("Acceso denegado. Saliendo...")
```

------------------------------------------------------------------------

# 🔐 Sistema de autenticación

El módulo `auth.py` permite validar usuarios mediante:

-   Nombre de usuario
-   PIN

Características:

-   Máximo **3 intentos de usuario**
-   Máximo **3 intentos de PIN**
-   Bloqueo automático si se exceden los intentos

Ejemplo de validación:

``` python
if pin_ingresado == pin_db:
    print("Acceso concedido")
    return usuario
```

------------------------------------------------------------------------

# 📊 Base de datos de usuarios

El sistema usa una **base de datos simulada en memoria** en `users.py`.

Cada usuario contiene:

-   PIN
-   Saldo
-   Historial de transacciones

Ejemplo:

``` python
cuentas = {
    "Luis": {
        "pin": "0000",
        "saldo": 1500.0,
        "historial": []
    }
}
```

------------------------------------------------------------------------

# 🧠 Lógica del cajero automático

El módulo `logica_atm.py` contiene las operaciones principales del
sistema.

## Consultar saldo

Permite ver el saldo disponible del usuario.

``` python
consultar_saldo(usuario)
```

Salida:

    ESTADO DE CUENTA
    Cliente: LUIS
    Saldo disponible: $1000.0

------------------------------------------------------------------------

## Depositar dinero

Permite ingresar dinero a la cuenta.

Validaciones:

-   El monto debe ser mayor a **0**
-   No puede superar **\$10,000 por transacción**

``` python
cuentas[usuario]["saldo"] += monto
```

También se registra en el historial.

------------------------------------------------------------------------

## Retirar dinero

Permite retirar dinero de la cuenta.

Validaciones:

-   El monto debe ser mayor a **0**
-   No puede exceder el saldo disponible

``` python
cuentas[usuario]["saldo"] -= monto
```

------------------------------------------------------------------------

## Historial de movimientos

Cada operación se guarda automáticamente en el historial del usuario.

Ejemplo de registro:

``` python
movimiento = f"{tipo}: ${monto:.2f}"
cuentas[usuario]["historial"].append(movimiento)
```

Ejemplo de salida:

    1. DEPÓSITO: $500.00
    2. RETIRO: $200.00

------------------------------------------------------------------------

# 📋 Menú interactivo

El archivo `menu.py` controla la navegación del usuario dentro del
cajero.

Opciones disponibles:

    1. Consultar saldo
    2. Depositar dinero
    3. Retirar dinero
    4. Historial
    5. Salir

Ejemplo:

``` python
opcion = int(input("Ingresa la opcion (1-5): "))
```

------------------------------------------------------------------------

# ⏳ Barra de progreso

El módulo `progress_bar.py` simula el procesamiento de operaciones con
una barra de progreso.

``` python
progress_bar()
```

Ejemplo visual:

    [██████----] 60%

Esto mejora la **experiencia del usuario** simulando el funcionamiento
de un cajero real.

------------------------------------------------------------------------

# 🧹 Limpieza de pantalla

El archivo `clean_screen.py` permite limpiar la terminal para mejorar la
presentación del menú.

``` python
os.system('clear')
```

------------------------------------------------------------------------

# 🛡️ Validaciones del sistema

El sistema incluye múltiples validaciones:

-   Control de errores en entradas numéricas
-   Validación de montos
-   Verificación de saldo suficiente
-   Control de intentos de autenticación

Ejemplo:

``` python
except ValueError:
    print("Error: Entrada inválida.")
```

------------------------------------------------------------------------

# 🚀 Cómo ejecutar el proyecto

## 1️⃣ Requisitos

-   Python 3.8 o superior

Verificar instalación:

``` bash
python --version
```

------------------------------------------------------------------------

## 2️⃣ Ejecutar el programa

Ubícate en la carpeta del proyecto y ejecuta:

``` bash
python main.py
```

------------------------------------------------------------------------

# 🧪 Usuarios de prueba

Puedes iniciar sesión con cualquiera de los usuarios definidos en
`users.py`.

 | Usuarios  |  PIN |
 |-----------|------------|
 | Luis      |  0000      |
 | Lucy      |  1111      |
 | Elon      |  5555      |
 | Maria     |  8888      |

------------------------------------------------------------------------



# 👨‍💻 Autor

Proyecto desarrollado con fines educativos para practicar:

-   Python
-   Programación modular
-   Manejo de estructuras de datos
-   Simulación de sistemas reales
