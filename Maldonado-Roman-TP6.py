class Persona():
    def __init__(self, nombre, edad, direccion):  # Constructor
        self.__nombre = nombre
        self.__edad = edad
        self.__direccion = direccion

    def mostrar(self):
        print('# Nombre:', self.__nombre)
        print('> Edad:', self.__edad)
        print('> Dirección:', self.__direccion)

    def changeName(self):
        name = input('Ingresa un nuevo nombre: ')
        self.__nombre = name

momo = Persona('Momo', 69, 'Montero 675')  # Objeto 1
coscu = Persona('Coscu', 31, 'La Dolfina 69')  # Objeto 2

print('---------------------------------')
momo.mostrar()
print('---------------------------------')
coscu.mostrar()
print('---------------------------------')

momo.changeName()
momo.mostrar()
