# Start: Manejo de excepciones
## Sintaxis básica
# try:
#     # Introduce el código que puede fallar.
#     pass
# except TipoError1:
#     # Se ejecuta si ocurre TipoError1.
#     pass
# except (TipoError2, TipoError3):
#     # Se ejecuta si ocurre TipoError2 o el TipoError3.
#     pass
# else:
#     # Se ejecuta si no hubo ninguna excepción.
#     pass
# finally:
#     # Se ejecuta siempre al final (limpieza).
#     pass

## Ejemplo con ValueError
# Sin manejo de excepciones:
# while True:
#     numero = int(input("Ingresa un número entero: "))
#     print(f"Número ingresado: {numero}")
#     print("Intento de entrada finalizado.\n")
#     break

# Con manejo de excepciones:
# while True:
#     try:
#         numero = int(input("Ingresa un número entero: "))
#         print(f"Número ingresado: {numero}")
#         break
#     except ValueError:
#         print("Error: Debes ingresar un número entero. Intenta nuevamente.")
#     finally:
#         print("Intento de entrada finalizado.\n")

## Ejemplo con ValueError y ZeroDivisionError
# Sin manejo de excepciones:
# def division(a, b):
#     return a/b

# while True:
#     numero_1 = int(input("Ingresa un número entero: "))
#     numero_2 = int(input("Ingresa otro número entero: "))
#     resultado = division(a=numero_1, b=numero_2)
#     print(f"El resultado es: {resultado}")
#     print("Intento de entrada finalizado.\n")
#     break


# Con manejo de excepciones:
# def division(a, b):
#     return a/b

# while True:
#     try:
#         numero_1 = int(input("Ingresa un número entero: "))
#         numero_2 = int(input("Ingresa otro número entero: "))
#         resultado = division(a=numero_1, b=numero_2)
#         print(f"El resultado es: {resultado}")
#         break
#     except ValueError:
#         print("Error: Debes ingresar un número entero. Intenta nuevamente.")
#     except ZeroDivisionError:
#         print("Error: No puedes dividir entre cero.")
#     finally:
#         print("Intento de entrada finalizado.\n")

## Manejo de múltiples excepciones (captura del mensaje del error)
# try:
#     numero = int(input("Introduce un número: "))
#     resultado = 10 / numero
# except (ValueError, ZeroDivisionError) as error_var:
#     print(f"Error: {error_var}")

## Exception
# Ejemplo 1:
# try:
#     x = int("hola")  # Esto generará un ValueError
# except Exception as e:
#     print(f"Se produjo un error: {e}")

# Ejemplo 2:
# try:
#     resultado = 5/0  # Esto generará un ZeroDivisionError
# except Exception as e:
#     print(f"Se produjo un error: {e}")

# End: Manejo de excepciones

# Start: Lanzando excepciones
# Sintaxis básica: raise TipoDeError("Mensaje opcional")
# Sin manejo de excepciones:
# def verificar_edad(edad):
#     if edad < 0:
#         raise ValueError("La edad no puede ser negativa.")
#     print(f"Edad válida: {edad}")

# verificar_edad(-5) # Esto generará un ValueError


# Con manejo de excepciones:
# def verificar_edad(edad):
#     if edad < 0:
#         raise ValueError("La edad no puede ser negativa.")
#     print(f"Edad válida: {edad}")

# try:
#     verificar_edad(-5) # Esto generará un ValueError
# except ValueError as e:
#     print(f'Error: {e}')

## Bonus: Uso de any()
# texto = "python es Genial"
# print(any(char.isupper() for char in texto))

# End: Lanzando excepciones

# Start: Decoradores
# def requiere_permiso(func):
#     """Función para preguntar si un usuario tiene permiso."""

#     def wrapper(usuario, *args, **kwargs):
#         if usuario != "admin":
#             print("✖️  Acceso denegado: no tienes permisos.")
#             return None
#         return func(usuario, *args, **kwargs)

#     return wrapper


# @requiere_permiso
# def eliminar_datos(usuario):
#     """Función para simular la eliminación de datos."""
#     print(f"🗑️  Datos eliminados por {usuario}")


# eliminar_datos(usuario="invitado")
# eliminar_datos(usuario="admin")
# End: Decoradores


# Start: POO
## Start: Clases
### Ejemplo sintaxis
# class Perro:
#     """Clase para representar a un perro."""

#     pass

# mi_perro = Perro()
# print(type(mi_perro))


### Ejemplo constructor
# class Persona:
#     """Clase para representar a una persona."""

#     cerebro = 1  # Atributo de la clase.

#     def __init__(self, nombre, edad):
#         # Atributos de la instancia.
#         self.nombre = nombre
#         self.edad = edad


# p_1 = Persona(nombre="Ana", edad=30)
# print(p_1.nombre, p_1.edad)
# print(p_1.cerebro)
# print("-" * 40)
# p_2 = Persona("Pedro", 15)
# print(p_2.nombre, p_2.edad)
# print(p_2.cerebro)


### Clases y objetos
# class Coche:
#     """Clase para representar un coche."""

#     ruedas = 4

#     def __init__(self, marca, modelo, color=None):
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color

#     def detalles(self):
#         """Devuelve todos los detalles del coche."""
#         if not self.color:
#             return f"- Coche de {self.ruedas} ruedas: {self.marca} {self.modelo}"
#         return f"- Coche {self.color.lower()} de {self.ruedas} ruedas: {self.marca} {self.modelo}"


# mi_coche = Coche("Toyota", "Corolla")
# print(mi_coche.detalles())
# mi_coche_2 = Coche(color="ROJO", modelo="ONIX TURBO RS", marca="Chevrolet")
# print(mi_coche_2.detalles())
## End: Clases

# End: POO
