import random
import math

# Start: Sintaxis
# if True:
#     print("Hola mundo")
# End: Sintaxis

# Start: Variables, constantes y tipos de datos
# Variables
# x = 10  # Guarda el número entero 10 en la variable X.
# tasa_interes = 3.14
# usuario_actual = "Ana"
# usuario_activo = True

# Constantes
# MAX_INTENTOS_JUGADOR = 3 # ESTE VALOR NO DEBE CAMBIAR NUNCA

# Print (stdout)
# nombre = "Ana"
# otro_nombre = "Pedro"
# print("¡Hola, " + nombre + "!") # Imprime: ¡Hola, Ana!
# print("¡Hola,", nombre + "!") # Imprime: ¡Hola, Ana!
# print(f"¡Hola, {nombre} y {otro_nombre}!") # Imprime: ¡Hola, Ana y Pedro!

# Tipos de datos básicos
# int: números enteros (-2, 0, 5)
# float: números decimales (3.14, -0.5)
# str: texto entre comillas ("hola", 'hola')
# bool: verdadero o falso (True, False)
# print(type(x))
# print(type(tasa_interes))
# print(type(usuario_actual))
# print(type(usuario_activo))

# Tipado dinámico
# numero = 10  # Python infiere que 'numero' es un entero.
# print(type(numero))
# nombre = "Juan"  # Aquí infiere que 'nombre' es una cadena.
# print(type(nombre))

# Declaración y asignación de variables
# mensaje = ""
# End: Variables, constantes y tipos de datos

# Start: Operadores aritméticos
# Operadores aritméticos
# a = 10
# b = 3
# print(a + b)  # Suma → 13
# print(a - b)  # Resta → 7
# print(a * b)  # Multiplicación → 30
# print(a / b)  # División → 3.333...
# print(a // b) # División entera → 3
# print(a % b)  # Módulo (resto de la división) → 1
# print(a ** b) # Potencia → 1000 (10^3)

# Operadores de comparación
# x = 5
# y = 10
# print(x == y)  # ¿Son iguales? → False
# print(x != y)  # ¿Son diferentes? → True
# print(x > y)   # ¿x es mayor que y? → False
# print(x < y)   # ¿x es menor que y? → True
# print(x >= y)  # ¿x es mayor o igual que y? → False
# print(x <= y)  # ¿x es menor o igual que y? → True

# Operadores lógicos (and, or, not)
# edad = 20
# es_estudiante = True
# print((edad > 18) and es_estudiante)  # True (ambas condiciones son ciertas)
# print((edad > 18) and not es_estudiante)  # True (ambas condiciones son ciertas)
# print((edad < 18) or es_estudiante)  # True (al menos una es cierta)
# print((edad < 18) or not es_estudiante)  # True (al menos una es cierta)
# print(not es_estudiante)  # False (invierte el valor)

# Operadores de asignación
# x = 10  # Asignación simple
# print(x)
# x += 5  # Suma y asigna (x = x + 5)
# print(x)
# x -= 3  # Resta y asigna (x = x - 3)
# print(x)
# x *= 2  # Multiplica y asigna (x = x * 2)
# print(x)
# x /= 4  # Divide y asigna (x = x / 4)
# print(x)
# Otros ejemplos:
# a, b, c = 5, 10, 15  # Asignación múltiple (asigna 5 a 'a', 10 a 'b' y 15 a 'c').
# print(a, b, c)
# p = q = r = 0  # Asignación del mismo valor a múltiples variables (asigna 0 a 'p', 'q' y 'r').
# print(p, q, r)
## Start: Intercambio directo
# x, y = 10, 20
# print(x, y)
# x, y = y, x
# print(x, y)
## End: Intercambio directo

# Start: Input (stdin)
# nombre = input("¿Cuál es tu nombre? ")
# print("Hola,", nombre + "!")

# dato_1 = float(input("Dame el dato 1: "))
# dato_2 = float(input("Dame el dato 2: "))
# print(f"La suma de los dos números es: {dato_1 + dato_2}")
# End: Input

# Start: Conversión de tipos de datos básicos
## Conversión implícita
# a = 5 # int
# b = 2.0 # float
# c = a + b # float
# print(type(a), type(b), type(c))
## Conversión explícita
# Conversión a entero
# num_str = "20"
# print(type(num_str))
# num_int = int(num_str)  # num_int será 20
# print(type(num_int))

# Conversión a flotante
# num = 10
# print(type(num))
# num_float = float(num)  # num_float será 10.0
# print(type(num_float))
# End: Conversión de tipos de datos básicos

# End: Operadores aritméticos


# Start: Condicionales
# num_input = float(input("Ingresa un número: "))
# if num_input < 0:
#     # Bloque de código que se ejecuta
#     print("Número negativo.")
# elif num_input == 0:
#     # Bloque de código que se ejecuta
#     print("Cero.")
# else:
#     # Bloque de código que se ejecuta
#     print("Número positivo.")

# 1. Implementa un programa que solicite la edad y que este determine si la persona es menor de edad, mayor o tiene edad de jubilación.
# Code of Fabiola
# num_input = int(input("ingrese edad: "))
# if num_input >= 70:
#     print("Edad para jubilarse")
# elif num_input >= 18:
#     print("mayoria de edad")
# else:
#     print("menor de edad")
# Code of Heymi
# edad_persona = int(input("Ingresa tu edad: "))
# if edad_persona < 18:
#     print("Menor de edad")
# elif edad_persona >= 18 and edad_persona <= 69:
#     print("Mayor de edad")
# else:
#     print("Edad de jubilacion")
# Posible solución problema 1:
# edad = int(input("Ingresa tu edad: "))
# if edad < 18:
#     print("Eres menor de edad.")
# elif edad >= 65:
#     print("Ya puedes jubilarte.")
# else:
#     print("Eres un adulto.")

# 2. Implementa un programa que solicite una contraseña y verifica si es correcta o incorrecta. “Tú defines cuál es la contraseña correcta”.
# Code of Fabiola
# contra = input("ingrese contrasena: ")
# if contra == "0":
#     print("contrasena correcta")
# else:
#     print("contrasena incorrecta")
# Posible solución problema 2:
# contraseña_correcta = "Python123"
# contraseña_usuario = input("Ingresa la contraseña: ")
# if contraseña_usuario == contraseña_correcta:
#     print("¡Acceso concedido!")
# else:
#     print("Contraseña incorrecta. Inténtalo de nuevo.")
# 3. Implementa un programa que solicite dos números, determina cuál es el mayor, o si son iguales.
# Posible solución problema 3:
# num1 = float(input("Ingresa el primer número: "))
# num2 = float(input("Ingresa el segundo número: "))
# if num1 > num2:
#     print(f"El número mayor es {num1}")
# elif num2 > num1:
#     print(f"El número mayor es {num2}")
# else:
#     print("Ambos números son iguales")

# End: Condicionales


# Start: Bucle While
# a, b = 0, 1
# while a < 10:
#     print(a, b)
#     a = b
#     b = a + b

# num_recorrer = int(input("Números a recorrer: "))
# num_actual = 1
# while True:
#     num_actual += 1
#     print(num_actual)
#     if num_actual == 10:
#         break

# while True:  # Bucle infinito hasta que el usuario ingrese un número negativo
#     numero = int(input("Ingrese un número (negativo para salir): "))
#     if numero < 0:
#         print("Número negativo detectado. ¡Fin del programa!")
#         break  # Rompe el bucle
#     print(f"El número ingresado es: {numero}")

# numero = 0
# while numero < 10:
#     numero += 1
#     if (numero % 2) != 0:  # Si el número es impar...
#         continue  # Salta el resto del código y pasa a la siguiente iteración
#     print(numero)  # Solo imprime los números pares

# End: Bucle While

# Start: Bucle For
# words = ['gato', 'perro', 'pájaro']
# for word in words:         # Recorre cada palabra en la lista
#     print(word, len(word)) # Muestra la palabra y con la función len(), la longitud de la misma.

# for i in range(5):  # Crea una secuencia del 0 al 4.
#     print(i)
# print('')

# for i in range(2, 7): # Crea una secuencia del 2 al 6.
#     print(i)
# print('')

# for i in range(1, 10, 2): # Crea una secuencia del 1 al 9 saltando de 2 en 2.
#     print(i)
# print('')

# for i in range(10, 0, -2): # Crea una secuencia en reversa del 10 al 2 saltando de 2 en 2.
#     print(i)
# print('')

# Ejercicio 1: Escribe un programa que pida un número y haga una cuenta regresiva hasta 0 usando while.
# num = int(input("Ingrese un número: "))
# while num >= 0:
#     print(num)
#     num -= 1  # Disminuye el número

# Ejercicio 2: Escribe un programa para mostrar los números pares  desde 0 hasta 20.
# for i in range(0, 21, 2):  # Empieza en 0, aumenta de 2 en 2 hasta 20
#     print(i)

# Ejercicio 3: Crea una lista de números y úsala para calcular la suma total.
# numeros = [3, 7, 5, 1, 9]
# suma = 0
# for n in numeros:
#     suma += n  # Acumula los valores
# print("La suma total es:", suma)

# Ejercicio 4: Crea un programa que pida una contraseña hasta que sea correcta. “Tú defines cuál es la contraseña correcta”.
# Posible solución:
# contraseña_correcta = "Python123"
# while True:  # Bucle infinito hasta que la condición se cumpla o el bucle se rompa con "break"
#     contraseña_usuario = input("Ingrese la contraseña: ")
#     if contraseña_correcta == contraseña_usuario:
#         print("¡Acceso concedido!")
#         break
#     print("Contraseña incorrecta, intenta de nuevo.\n")
# Code of Jimena:
# passwd_correcta = "123Python"
# passwd = ""
# while passwd != passwd_correcta:
#     passwd = input("Ingresa contraseña: ")
#     if passwd == passwd_correcta:
#         print("¡Contraseña correcta!")
#         break
#     else:
#         print("Contraseña incorrecta, intentalo de nuevo")

# End: Bucle For

# Start: Librería estándar en Python
# while True:
#     num_ale = random.randint(0, 20)
#     print(num_ale)
#     if num_ale == 20:
#         break
# print()
# print(math.sqrt(16))
# print(math.pi)
# End: Librería estándar en Python
