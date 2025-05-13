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
