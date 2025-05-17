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


## Polimorfismo
### Operadores
# print(len("Hola"))
# print(len((1, 2, 3, 4)))
# print(len([1, 2, 3, 4]))
### Métodos (sobre escritura)
# class Animal:
#     def hablar(self):
#         print("...")


# class Gato(Animal):
#     def hablar(self):
#         print("Miau")


# class Perro(Animal):
#     def hablar(self):
#         print("Guau")


# mascotas = (Gato(), Perro())
# for mascota in mascotas:
#     mascota.hablar()


### Sobrecarga de métodos
# class Pedido:
#     """Clase para procesar pedidos con opciones flexibles."""

#     def procesar_pedido(self, cantidad, **kwargs):
#         """Simula sobrecarga permitiendo múltiples configuraciones en un pedido."""
#         mensaje = f"Pedido de {cantidad} productos."

#         if "metodo_pago" in kwargs:
#             mensaje += f" Pago con {kwargs['metodo_pago']}."

#         if "direccion_envio" in kwargs:
#             mensaje += f" Envío a {kwargs['direccion_envio']}."

#         if "descuento" in kwargs:
#             mensaje += f" Aplicado {kwargs['descuento']}% de descuento."

#         print(mensaje)


# pedido = Pedido()
# pedido.procesar_pedido(3)
# pedido.procesar_pedido(5, metodo_pago="Tarjeta")
# pedido.procesar_pedido(2, direccion_envio="Quito")
# pedido.procesar_pedido(
#     10, metodo_pago="PayPal", descuento=15, direccion_envio="Guayaquil"
# )


### Duck typing
# class Pato:
#     def volar(self):
#         print("El pato vuela")


# class Avion:
#     def volar(self):
#         print("El avión despega")


# def despegar(obj):
#     obj.volar()


# despegar(Pato())
# despegar(Avion())

## Abstracción
# from abc import ABC, abstractmethod


# class Vehiculo(ABC):
#     def __init__(self, nombre):
#         self.nombre = nombre

#     @abstractmethod
#     def arrancar(self):
#         pass

#     @abstractmethod
#     def detener(self):
#         pass


# class Auto(Vehiculo):
#     def arrancar(self):
#         return f"El auto {self.nombre} ha arrancado"

#     def detener(self):
#         return f"El auto {self.nombre} se ha detenido"


# class Moto(Vehiculo):
#     def arrancar(self):
#         return f"La moto {self.nombre} ha arrancado"

#     def detener(self):
#         return f"La moto {self.nombre} se ha detenido"


# def vehiculo_arrancar(obj):
#     return obj.arrancar()


# def vehiculo_detener(obj):
#     return obj.detener()


# vehiculos = (Auto("Beto"), Moto("Martita"))
# for vehiculo in vehiculos:
#     print(vehiculo_arrancar(vehiculo))
#     print(vehiculo_detener(vehiculo))


## Encapsulamiento
# class Cuenta:
#     def __init__(self, saldo):
#         self.__saldo = saldo

#     def mostrar_saldo(self):
#         return f"Saldo: {self.__saldo}"


# c = Cuenta(100)
# OtraCuenta()
# # print(c.__saldo)  # Sin name-mangling.
# print(c._Cuenta__saldo)  # Con name-mangling.
# print(c.mostrar_saldo())


### Propiedades con @property
# Sin @property
# class Empleado:
#     """Clase para representar un empleado."""

#     def __init__(self, nombre, salario):
#         # No uses getters ni setters en atributos públicos que son muy simples,
#         # accede directamente a ellos.
#         self.nombre = nombre
#         self._salario = salario

#     def __str__(self):
#         return f"Empleado: {self.nombre} con un salario de ${self._salario}"

#     def get_salario(self):
#         """Método para retornar el salario de un empleado."""
#         return self._salario

#     def set_salario(self, valor):
#         """Método para asignar el salario a un empleado."""
#         if valor < 0:
#             raise ValueError("Salario no puede ser negativo")
#         self._salario = valor


# e = Empleado("Ana", 5000)
# print(e, e.get_salario())
# e.nombre = "Anabel"
# e.set_salario(6000)
# print(e)
# e.set_salario(-100)


# Con @property
# class Empleado:
#     """Clase para representar un empleado."""

#     def __init__(self, nombre, salario):
#         # No uses getters ni setters en atributos públicos que son muy simples,
#         # accede directamente a ellos.
#         self.nombre = nombre
#         self._salario = salario

#     def __str__(self):
#         return f"Empleado: {self.nombre} con un salario de ${self._salario}"

#     @property
#     def salario(self):
#         """Método para retornar el salario de un empleado."""
#         return self._salario

#     # Define sólo los setters que realmente necesites; de lo contrario,
#     # expón sólo el getter para hacerlo de sólo lectura.
#     @salario.setter
#     def salario(self, valor):
#         if valor < 0:
#             raise ValueError("Salario no puede ser negativo")
#         self._salario = valor


# e = Empleado("Ana", 5000)
# print(e, e.salario)
# e.nombre = "Anabel"
# e.salario = 6000
# print(e)
# e.salario = -100


### Validaciones con getters y setters
# class PersonaSinValidacion:
#     """Clase para representar a una persona con su atributo edad no validado."""

#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad  # Se asigna directamente sin validación


# persona = PersonaSinValidacion("Ana", 25)
# persona.edad = -5
# print("La edad es:", persona.edad)


# class Persona:
#     def __init__(self, nombre, edad):
#         self._nombre = nombre
#         self._edad = None
#         self.edad = edad

#     @property
#     def edad(self):
#         """Getter para edad."""
#         return self._edad

#     @edad.setter
#     def edad(self, valor):
#         """Setter para edad."""
#         if not isinstance(valor, int) or valor <= 0:
#             raise ValueError(
#                 f"La edad que ingresaste ({valor}) debe ser un número positivo."
#             )
#         self._edad = valor
#         # self.edad = valor # Error recursion infinita.


# persona = Persona("Ana", 25)
# try:
#     persona.edad = -5
# except ValueError as e:
#     print(f"Error: {e}")


### Métodos privados
# class Calculadora:
#     """Clase para representar a una calculadora."""

#     def __init__(self):
#         pass

#     def __sumar(self, a, b):
#         return a + b

#     def __restar(self, a, b):
#         return a - b

#     def resultado(self, a, b, operacion="sumar"):
#         """Método para retornar el resultado de una operación matemática."""
#         if operacion == "sumar":
#             return self.__sumar(a, b)
#         elif operacion == "restar":
#             return self.__restar(a, b)
#         else:
#             raise ValueError("Operación no válida. Usa 'sumar' o 'restar'.")


# c = Calculadora()
# print(c.resultado(2, 3, "sumar"))
# print(c.resultado(5, 2, "restar"))
# c.__restar(5, 2) # Da error.


# End: POO
