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


## Start: Atributos y métodos de las clases (incluyendo métodos especiales)
### Métodos especiales (str y repr)
# class Persona:
#     """Clase para representar a una persona."""

#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad

#     def __str__(self):
#         return f"{self.nombre}, {self.edad} años"

#     def __repr__(self):
#         return f"Persona(nombre={self.nombre!r}, edad={self.edad})"


# p = Persona("Laura", 40)
# print(p, ".---.", str(p))
# print(repr(p))

### Métodos especiales (eq)
# class Punto:
#     """Clase para representar un punto en una coordenada."""

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, otro_obj):
#         return (
#             isinstance(otro_obj, Punto)
#             # isinstance() es una función incorporada que verifica si
#             # un objeto pertenece a una determinada clase o subclase.
#             and self.x == otro_obj.x
#             and self.y == otro_obj.y
#         )

#     def __repr__(self):
#         return f"Punto({self.x}, {self.y})"


# p1 = Punto(3, 4)
# p2 = Punto(3, 4)
# print(p1, p2)
# print(p1 == p2)  # True gracias a __eq__
# print(p1, p2)  # Punto(3, 4) gracias a __repr__


### Métodos de instancia
# class Persona:
#     """Clase para representar a una persona."""

#     def __init__(self, nombre):
#         self.nombre = nombre

#     def saludar(self):
#         """Método de instancia que saluda a una persona."""
#         return f"Hola, soy {self.nombre}"


# p = Persona("Juan")
# print(p.saludar())
# p_2 = Persona("Felipe")
# print(p_2.saludar())


### Métodos de clase
# class Persona:
#     """Clase para representar a una persona."""

#     contador = 0

#     def __init__(self, nombre):
#         self.nombre = nombre
#         Persona.contador += 1

#     @classmethod
#     def total_personas(cls):
#         """Método de clase para mostrar cuántas personas se han creado con la clase."""
#         return f"Se han creado {cls.contador} personas."


# p_1 = Persona("Ana")
# p_2 = Persona("Luis")
# print(Persona.total_personas())


### Métodos estáticos
# class Matematicas:
#     """Clase para representar algunas operaciones matemáticas."""

#     @staticmethod
#     def sumar(a, b):
#         """Método estático para sumar dos números"""
#         return a + b

#     @staticmethod
#     def restar(a, b):
#         """Método estático para sumar dos números"""
#         return a - b


# print(Matematicas.sumar(5, 3))
# print(Matematicas.restar(5, 3))


## Herencia
# class Animal:
#     """Clase para representar a un animal."""

#     def saludar(self):
#         """Método de saludar"""
#         print("¡Hola, soy un animal!")


# class Perro(Animal):
#     """Clase para representar a un perro."""

#     def saludar(self):
#         print("¡Guau! soy un perro")


# mi_obj_perro = Perro()
# mi_obj_perro.saludar()


# class Padre:
#     def __init__(self, apellido):
#         self.apellido = apellido

#     def saludar(self):
#         return f"Hola, soy {self.apellido} el Padre"


# class Hija(Padre):
#     def __init__(self, nombre, apellido, edad):
#         super().__init__(apellido)  # Llamamos al constructor de la clase Padre.
#         self.nombre = nombre
#         self.edad = edad

#     def saludar(self):
#         return_saludar_del_padre = super().saludar()
#         return f"{return_saludar_del_padre}. Y yo soy {self.nombre} {self.apellido} la Hija y tengo {self.edad} años."


# persona = Hija("Ana", "Paredes", 25)
# print(persona.saludar())


# Ejemplo más realista
# class Persona:
#     """Clase para representar a una persona."""

#     def __init__(self, nombre):
#         self.nombre = nombre


# class Empleado(Persona):
#     """Clase para representar a un empleado."""

#     def __init__(self, nombre, puesto):
#         super().__init__(nombre)
#         self.puesto = puesto

#     def saludar(self):
#         """Método para saludar."""
#         print(f"Hola, soy {self.nombre} y trabajo como {self.puesto}")


# emp = Empleado("Ana", "Diseñadora")
# emp.saludar()


# class Persona:
#     """Clase para representar a una persona."""

#     def __init__(self, nombre):
#         self.nombre = nombre


# class Cliente(Persona):
#     """Clase para representar a un cliente."""

#     def __init__(self, nombre, numero):
#         super().__init__(nombre)
#         self.numero = numero

#     def info(self):
#         """Método para mostrar la información del cliente."""
#         return f"Cliente {self.nombre}, Nº {self.numero}"


# class ClienteVIP(Cliente):
#     """Clase para representar a un cliente VIP."""

#     def __init__(self, nombre, numero, descuento):
#         super().__init__(nombre, numero)
#         self.descuento = descuento

#     def info(self):
#         """Método para mostrar la información del cliente."""
#         return f'Cliente {self.nombre} "VIP", Nº {self.numero}, Descuento: {self.descuento}%'


# cliente = Cliente("Pedro", 101)
# print(cliente.info())
# vip = ClienteVIP("Juan", 102, 20)
# print(vip.info())


# class Motor:
#     """Clase para representar a un motor."""

#     def __init__(self, caballos):
#         self.caballos = caballos

#     def describir(self):
#         return f"{self.caballos} caballos de vapor (CV)"


# class Coche:
#     def __init__(self, marca, motor):
#         self.marca = marca
#         self.motor = motor

#     def enceder(self):
#         print(f"{self.marca} arrancando con un motor de {self.motor.describir()}")

# motor_v6 = Motor(200)
# mi_auto = Coche(marca="Toyota", motor=motor_v6)
# mi_auto.enceder()

# End: POO
