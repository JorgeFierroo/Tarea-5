from Persona import Persona
#a
class Estudiante(Persona):

    contador_estudiantes = 0

    def __init__(self, nombre, apellido, fecha_de_nacimiento, matricula, carrera, semestre):
        super().__init__(nombre, apellido, fecha_de_nacimiento)
        self.__matricula = matricula
        self.__carrera = carrera
        self.__semestre = semestre

    def estudiar(self, materia, horas):
        return f"{self.nombre} estuvo estudiando {materia} durante {horas} horas"
    
    def presentarse(self):
        return f"Hola, mucho gusto. Mi nombre es {self.nombre} {self.apellido} y estoy en la carrera de {self.carrera} en mi {self.semestre} semestre"

    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self, matricula):
        if matricula.isalpha():
            self.__matricula = matricula
        else:
            print("El nombre no debe contener numeros.")

    @property
    def carrera(self):
        return self.__carrera
    
    @carrera.setter
    def carrera(self, carrera):
        if carrera.isalpha():
            self.__carrera = carrera
        else:
            print("El nombre no debe contener numeros.")

    @property
    def semestre(self):
        return self.__semestre
    
    @semestre.setter
    def semestre(self, semestre):
        if isinstance(semestre, int):
            self.__semestre = semestre
        else:
            print("La variable no es un entero.")