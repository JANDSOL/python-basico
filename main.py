# Start: Métodos de los strings
## Mayúsculas
# word = "Programa en Python 3"
# word_upper = word.upper()
# print(word + '\n' + word_upper)

## Notación título
# word = "programa en python 3"
# word_title = word.title()
# print(word + '\n' + word_title)

## Reemplazo
# word = "Programa En Python 3"
# word_new = word.replace(" ", "_")
# print(word + '\n' + word_new)

## Eliminación de espacios
# word = "    Programa En Python 3    "
# word_lstrip = word.lstrip()
# print('"' + word_lstrip + '"')
# word = "    Programa En Python 3    "
# word_rstrip = word.rstrip()
# print('"' + word_rstrip + '"')
# word = "    Programa En Python 3    "
# word_strip = word.strip()
# print('"' + word_strip + '"')

## Separador
# word = "Programa En Python 3"
# word_split = word.split()
# print(word_split)
# email = "example@gmail.com"
# email_split = email.split("@")
# print(email_split)

# End: Métodos de los strings

# Start: Estructura de datos

## Listas
### Creación
# frutas = ["🍎", "🍌", "🍒"]
# frutas_vacias = list()
# print(frutas)
# print(frutas_vacias)

### Slicing (rebanadas)
# Sintaxis: lista[dig_inicio:dig_fin-1:dig_paso]
# frutas = ["🍎", "🍌", "🍒"]
# # Obtener el primer elemento
# print(frutas[0])  # 🍎
# # Obtener el segundo elemento
# print(frutas[1])  # 🍌
# # Obtener los dos primeros elementos
# print(frutas[:2])  # ["🍎", "🍌"]
# # Obtener el último elemento
# print(frutas[-1])  # 🍒
# # Obtener los dos últimos elementos
# print(frutas[-2:])  # ["🍌", "🍒"]
# # Extraer elementos saltando de 2 en 2
# print(frutas[::2])  # ["🍎", "🍒"]
# # Obtener la lista invertida
# print(frutas[::-1])  # ["🍒", "🍌", "🍎"]
# # Obtener una sublista sin el primer ni último elemento
# print(frutas[1:-1])  # ["🍌"]
# # Intentar acceder más allá del rango (no genera error)
# print(frutas[:10])  # ["🍎", "🍌", "🍒"]
# # El slicing también funciona perfectamente con cadenas de texto, ya que en Python las cadenas son secuencias de caracteres. Aquí tienes un ejemplo rápido:
# texto = "Python"
# # Obtener los primeros tres caracteres
# print(texto[:3])  # "Pyt"
# # Obtener los últimos tres caracteres
# print(texto[-3:])  # "hon"
# # Invertir la cadena
# print(texto[::-1])  # "nohtyP"

### Acceder y modificar elementos
# frutas = ["🍎", "🍌", "🍒"]
# print(frutas)
# frutas[1] = "🥝"
# print(frutas)
### Agregar y eliminar
# frutas = ["🍎", "🍌", "🍒", "🍌", "🍒", "🍎"]
# print(frutas)
# frutas.append("🍊")
# print(frutas)
# frutas.insert(0, "🍐")
# print(frutas)
# frutas.remove("🍒")
# print(frutas)
# elemento = frutas.pop()
# print(frutas, elemento)
### Ordenar y reordenar
# numeros = [3, 1, 4, 1, 5]
# print(numeros)
# numeros.sort()
# print(numeros)
# numeros.reverse()
# print(numeros)

### Iterar
# frutas = ["🍎", "🍌", "🍒"]
# for fruta in frutas:
#     print(fruta)

### List Comprehension
# frutas = ["manzana", "banana", "cereza"]
# Sin List Comprehension
# frutas_mayus = []
# for fruta in frutas:
#     frutas_mayus.append(fruta.upper())
# Con List Comprehension
# frutas_mayus = [fruta.upper() for fruta in frutas]
# print(frutas_mayus)

### Ejercicios propuestos
# Ejercicio 1: Define una lista con 5 números y cambia el tercer elemento.
# numeros = [10, 20, 30, 40, 50]  # Lista inicial
# numeros[2] = 99  # Cambiamos el tercer elemento (índice 2)
# print(numeros)  # [10, 20, 99, 40, 50]

# Ejercicio 2: Dada la lista [4, 7, 2, 9, 1], ordénala de menor a mayor y luego invierte su orden.
# lista = [4, 7, 2, 9, 1]
# lista.sort()  # Ordenamos de menor a mayor
# print(lista)  # [1, 2, 4, 7, 9]
# lista.reverse()  # Invertimos el orden
# print(lista)  # [9, 7, 4, 2, 1]
# O también:
# lista = [4, 7, 2, 9, 1]
# lista_ordenada_invertida = sorted(lista)[::-1]
# print(lista_ordenada_invertida)  # [9, 7, 4, 2, 1]

# Ejercicio 3: Con la lista ["a", "b", "c", "d", "e"], obtén la sublista ["c", "d", "e"] usando slicing.
# letras = ["a", "b", "c", "d", "e"]
# sublista = letras[2:]  # Tomamos desde el índice 2 hasta el final
# print(sublista)  # ["c", "d", "e"]


## Tuplas
# coordenadas = (10, 20)
# print(coordenadas)

### Desempaquetado
# coordenadas = (10, 20)
# x, y = coordenadas
# print(x, y, coordenadas)

### Encontrar y acceder por el índice
# frutas = ("🍎", "🍌", "🍒")
# banana_index = frutas.index("🍌")
# print(banana_index, frutas[banana_index])

### Convertir tupla a lista y lista a tupla
# coordenadas = (10, 20)
# lista_de_coordenadas = list(coordenadas)
# print(lista_de_coordenadas)
# tupla = tuple(lista_de_coordenadas)
# print(tupla)

### Ejercicios propuestos
# Ejercicio 1: Crea una tupla con tres frutas y muestra la tercera fruta buscando y usando su índice.
# frutas = ("manzana", "banana", "cereza")
# cereza_index = frutas.index("cereza")
# print(frutas[cereza_index])  # Output: "cereza"

# Ejercicio 2: Dada la tupla punto = (7, 3), extrae sus coordenadas a dos variables y súmalas.
# punto = (7, 3)
# x, y = punto  # Desempaquetado de la tupla en variables
# resultado = x + y
# print(resultado)  # Output: 10

# Ejercicio 3: Convierte la lista ['a', 'b', 'c'] en tupla, e intenta agregar un elemento nuevo (observa qué sucede).
# lista = ['a', 'b', 'c']
# tupla = tuple(lista)  # Conversión de lista a tupla
# print(tupla)  # Output: ('a', 'b', 'c')

## Diccionarios
# alumno = {"nombre": "Luis", "curso": "Python", "nota": 8.5}
# print(alumno)

### Acceder y modificar
# alumno = {"nombre": "Luis", "curso": "Python", "nota": 8.5}
# print(alumno["curso"])
# print(alumno["nombre"])
# print(alumno["nota"])
# alumno["nota"] = 9
# print(alumno)

### Añadir y eliminar pares
# alumno = {"nombre": "Luis", "curso": "Python", "nota": 8.5}
# alumno["edad"] = 20
# valor = alumno.pop("curso")
# print(valor, alumno)
# del alumno["edad"]
# print(alumno)

### Iterar
# alumno = {"nombre": "Luis", "curso": "Python", "nota": 8.5}
# # print(alumno.keys())
# # print(alumno.values())
# # print(alumno.items())
# for clave in alumno.keys():
#     print(clave)
# for value in alumno.values():
#     print(value)
# for clave, valor in alumno.items():
#     print(clave, "->", valor)

### Manejo seguro
# alumno = {"nombre": "Luis", "curso": "Python", "nota": 8.5}
# # ciudad = alumno["ciudad"]
# ciudad = alumno.get("nombre", "Desconocido")
# print(ciudad)

### Operador in
# # En listas y tuplas
# frutas = ["manzana", "banana", "cereza"]
# print("banana" in frutas)  # True
# # En cadenas de texto
# texto = "Hola, ¿cómo estás?"
# print("cómo" in texto)  # True
# # En diccionarios (verifica si una clave existe)
# edades = {"Juan": 25, "María": 30, "Pedro": 22}
# print("María" in edades)  # True
# print("Laura" in edades)  # False

### Dict Comprehension
# # Ejemplo 1: Crear un diccionario a partir de una lista. "Cada número de la lista se convierte en una clave, y su cuadrado es el valor".
# numeros = [1, 2, 3, 4, 5]
# cuadrados = {num: num**2 for num in numeros}
# print(cuadrados)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# # Ejemplo 2: Transformar valores. "Las claves son palabras y los valores son su longitud".
# palabras = ["Python", "Java", "C++"]
# print(len(palabras))
# longitudes = {palabra: len(palabra) for palabra in palabras}
# print(longitudes)  # {'Python': 6, 'Java': 4, 'C++': 3}

### Ejercicios propuestos
# Ejercicio 1: Representa una lista de contactos donde la clave sea el nombre y el valor el número de teléfono.
# contactos = {
#     "Juan": "0987654321",
#     "María": "0998765432",
#     "Pedro": "0976543210"
# }
# print(contactos)  # {'Juan': '0987654321', 'María': '0998765432', 'Pedro': '0976543210'}

# Ejercicio 2: Dado el diccionario inventario = {"manzanas": 10, "naranjas": 5}, incrementa el valor de "manzanas" en 20%.
# inventario = {"manzanas": 10, "naranjas": 5}
# inventario["manzanas"] = int(inventario["manzanas"] * 1.2)  # Incremento del 20%
# print(inventario)  # {'manzanas': 12, 'naranjas': 5}

# Ejercicio 3: Elimina un elemento con pop() y luego verifica si la clave aún existe usando in.
# productos = {"leche": 2, "pan": 5, "huevos": 12}
# eliminado = productos.pop("pan")  # Eliminamos "pan"
# print(f'Elemento eliminado: {eliminado}')  # 5
# Verificamos si la clave aún existe
# print("pan" in productos)  # False

## Sets (Conjuntos)
# letras = {"a", "e", "i", "o", "u"}

### Agregar y eliminar
# letras.add("á")
# print(letras)
# letras.remove("o")
# print(letras)
# # letras.remove("z")
# letras.discard("z") # Eliminación segura

### Unir e intersectar sets
# pares = {2, 4, 6}
# impares = {1, 3, 4, 5}
# todos = pares | impares          # unión ∪: {1,2,3,4,5,6}
# print(todos)
# comunes = pares & {2, 3, 4}      # intersección ∩: {2,4}
# print(comunes)
# diff = pares - impares           # diferencia -: {2,6}
# print(diff)

### Eliminar duplicados
# numeros = [1, 2, 2, 3, 3, 3]
# unicos = set(numeros)
# print(numeros, unicos)

### Iterar (recorrer)
# numeros = {2, 5, 7, 9, 3}
# for n in numeros:
#     print(n)

### Ejercicios propuestos
# Ejercicio 1: Crea un set con los números del 1 al 5, elimina el 3 y añade el 10.
# numeros = {1, 2, 3, 4, 5}
# numeros.remove(3)  # Eliminar el número 3
# numeros.add(10)  # Agregar el número 10
# print(numeros)  # Output: {1, 2, 4, 5, 10}

# Ejercicio 2: Dados A = {1,2,3} y B = {3,4}, calcula A∪B, A∩B y B−A.
# A = {1, 2, 3}
# B = {3, 4}
# union = A | B  # Unión A∪B
# interseccion = A & B  # Intersección A∩B
# diferencia = B - A  # Diferencia B−A
# print(f"Unión: {union}")  # Output: {1, 2, 3, 4}
# print(f"Intersección: {interseccion}")  # Output: {3}
# print(f"Diferencia: {diferencia}")  # Output: {4}

# Ejercicio 3: A partir de la lista ['a','b','a','c','b','d'], genera un set para quedarse solo con los elementos únicos.
# lista = ['a', 'b', 'a', 'c', 'b', 'd']
# unicos = set(lista)  # Convierte la lista en un conjunto para eliminar duplicados
# print(unicos)  # Output: {'b', 'a', 'd', 'c'}

# End: Estructura de datos
