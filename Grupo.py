from Estudiante import Estudiante
from Profesor import Profesor
from Asignatura import Asignatura

class Grupo:

    contador_grupos = 0

    def __init__(self, numero_grupo, asignatura, profesor):
        Grupo.contador_grupos += 1
        self.__numero_grupo = numero_grupo
        self.__asignatura = asignatura
        self.__profesor = profesor
        self._estudiantes = []

    @property
    def numero_grupo(self):
        return self.__numero_grupo
    
    @numero_grupo.setter
    def numero_grupo(self, numero_grupo):
        if isinstance(numero_grupo, int):
            self.__numero_grupo = numero_grupo
        else:
            print("El numero de grupo no es un entero.")

    @property
    def asignatura(self):
        return self.__asignatura
    
    @asignatura.setter
    def asignatura(self, asignatura):
        if isinstance(asignatura, Asignatura):
            self.__asignatura = asignatura
            print("La asignatura se cambio correctamente")
        else:
            raise TypeError("Solo se pueden agregar instancias de la clase 'Asignatura'.")

    def agregar_estudiante(self, estudiante):
        if isinstance(estudiante, Estudiante):
            self._estudiantes.append(estudiante)
            return(f"Estudiante {estudiante.nombre} agregado a la asignatura {self.__asignatura.nombre}.")
        else:
            raise TypeError("Solo se pueden agregar instancias de la clase 'Estudiante'.")
        
    def estudiantes(self):
        return[estudiante.nombre for estudiante in self._estudiantes]

    @property
    def profesor(self):
        return self.__profesor.nombre

    @profesor.setter
    def profesor(self, profesor):
        if isinstance(profesor, Profesor):
            self.__profesor = profesor
            print("El profesor se cambio correctamente")
        else:
            raise TypeError("Solo se pueden agregar instancias de la clase 'Profesor'.")
        
    def mostrar_grupo(self):
        return f"numero del grupo: {self.__numero_grupo} Asignatura: {self.__asignatura.nombre} Profesor: {self.__profesor.nombre}"