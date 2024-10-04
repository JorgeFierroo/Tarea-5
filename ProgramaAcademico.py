from Grupo import Grupo

class ProgramaAcademico:

    contador_programas = 0

    def __init__(self, nombre, codigo):
        ProgramaAcademico.contador_programas += 1
        self.__nombre = nombre
        self.__codigo = codigo
        self.__grupos = []

    def agregar_grupo(self, grupo):

        if self.__grupos == []:
            self.__grupos.append(grupo)
            return "el grupo se agrego correctamente"

        for i in self.__grupos:
            if grupo.numero_grupo == i.numero_grupo:
                return("el grupo ya se encuentra agregado")         
            elif isinstance(grupo, Grupo):
                self.__grupos.append(grupo)

    def mostrar_programa(self):
        return f"nombre del programa: {self.__nombre}\ncodigo: {self.__codigo}\nlista de grupos: {self.grupos}"
    
    def eliminar_grupo(self, numero_grupo):

        if self.__grupos == []:
            return "la lista esta vacia"
        for i in self.__grupos:
            if i.numero_grupo == numero_grupo:
                self.__grupos.remove(i)
                return "Ha sido eliminado el grupo"
            else:
                return "EL grupo no existe"
            
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
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        if codigo.isalpha():
            self.__codigo = codigo
        else:
            print("El nombre no debe contener numeros.")
    
    @property
    def grupos(self):
        return self.__grupos