class Persona:

    contador_personas = 0

    def __init__(self, nombre, apellido, fecha_de_nacimiento):
        Persona.contador_personas += 1
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fecha_de_nacimiento = fecha_de_nacimiento

    def presentarse(self):
        return f"Hola, mucho gusto. Mi nombre es {self.nombre} {self.__apellido}"
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        if nombre.isalpha():
            self.__nombre = nombre
        else:
            print("El nombre no debe contener numeros.")

    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self, apellido):
        if apellido.isalpha():
            self.__apellido = apellido
        else:
            print("El nombre no debe contener numeros.")

    @property
    def fecha_de_nacimiento(self):
        return self.__fecha_de_nacimiento
    
    @fecha_de_nacimiento.setter
    def fecha_de_nacimiento(self, fecha):
        if fecha.isalpha():
            self.__fecha_de_nacimiento = fecha
        else:
            print("El nombre no debe contener numeros.")

    
pers = Persona("jorge", "fierro", "27/01/2004")