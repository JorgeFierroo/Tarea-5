from Persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, apellido, fecha_nacimiento, numero_empleado, departamento):
        super().__init__(nombre, apellido, fecha_nacimiento)
        self.__numero_empleado = numero_empleado
        self.__departamento = departamento

    def enseñar(self, materia):
        return f"enseñando {materia}"

    def presentarse(self):
        return f"Hola, mucho gusto. Mi nombre es {self.nombre} {self.apellido} y pertenezco al departamento de {self.departamento}"
    
    @property
    def numero_empleado(self):
        return self.__numero_empleado
    
    @numero_empleado.setter
    def numero_empleado(self, numero):
        if numero.isalpha():
            self.__numero_empleado = numero
        else:
            print("El nombre no debe contener numeros.")

    @property
    def departamento(self):
        return self.__departamento
    
    @departamento.setter
    def departamento(self, departamento):
        if departamento.isalpha():
            self.__departamento = departamento
        else:
            print("El nombre no debe contener numeros.")

    

    
prof = Profesor("David", "Martinez", "27/01/2004", "210", "fisica")

print(prof.presentarse())