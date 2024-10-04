from Asignatura import Asignatura
from Estudiante import Estudiante
from Grupo import Grupo
from Persona import Persona
from Profesor import Profesor
from ProgramaAcademico import ProgramaAcademico

est = Estudiante("jorge", "fierro", "27/01/2004", "2023","ingenieria civil informatica", 2)
est1 = Estudiante("pepito", "fierro", "27/01/2004", "2023","ingenieria civil informatica", 2)
prof = Profesor("David", "Martinez", "27/01/2004", "210", "fisica")
prof1 = Profesor("Julio", "Martinez", "27/01/2004", "210", "fisica")
asig = Asignatura("Fisica", "A321", 1)  

grupo1 = Grupo(1, asig, prof)
grupo2 = Grupo(2, asig, prof)

print(grupo1.agregar_estudiante(est))
print(grupo1.agregar_estudiante(est1))
print(grupo1.estudiantes())
grupo1.profesor = prof1
print(grupo1.profesor)

progra1 = ProgramaAcademico("holaa", "dada")

print(progra1.agregar_grupo(grupo1))
print(progra1.agregar_grupo(grupo2))
print(progra1.grupos())