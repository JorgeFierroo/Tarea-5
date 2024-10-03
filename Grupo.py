from Estudiante import Estudiante
from Profesor import Profesor
from Asignatura import Asignatura

class Grupo:
    def __init__(self, numero_grupo, asignatura, profesor):
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
            print(f"Estudiante {estudiante.nombre} agregado a la asignatura {self.__asignatura.nombre}.")
        else:
            raise TypeError("Solo se pueden agregar instancias de la clase 'Estudiante'.")
        
    def estudiantes(self):
        print([estudiante.nombre for estudiante in self._estudiantes])

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
        
est = Estudiante("jorge", "fierro", "27/01/2004", "2023","ingenieria civil informatica", 2)
est1 = Estudiante("pepito", "fierro", "27/01/2004", "2023","ingenieria civil informatica", 2)
prof = Profesor("David", "Martinez", "27/01/2004", "210", "fisica")
prof1 = Profesor("Julio", "Martinez", "27/01/2004", "210", "fisica")
asig = Asignatura("Fisica", "A321", 1)  

grupo1 = Grupo(1, asig, prof)

grupo1.agregar_estudiante(est)
grupo1.agregar_estudiante(est1)
grupo1.estudiantes()
grupo1.profesor = prof1
print(grupo1.profesor)