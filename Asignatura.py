class Asignatura:

    contador_asignaturas = 0

    def __init__(self, nombre, codigo, creditos):

        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser una cadena de texto (str).")
        
        if not isinstance(codigo, str):
            raise ValueError("El código debe ser una cadena de texto (str).")
        
        if not isinstance(creditos, int):
            raise ValueError("Los créditos deben ser un número entero (int).")
        
        self.__nombre = nombre
        self.__codigo = codigo
        self.__creditos = creditos

    def mostrar_informacion(self):
        return f"nombre: {self.__nombre}\ncodigo: {self.__codigo}\ncreditos: {self.__creditos}"

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        if nombre.replace(" ", "").isalpha():
            self.__nombre = nombre
        else:
            print("El nombre no debe contener numeros.")

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        if isinstance(codigo, int):
            self.__codigo = codigo
        else:
            print("La variable no es un entero.")

    @property
    def creditos(self):
        return self.__credito 
    
    @creditos.setter
    def creditos(self, creditos):
        if isinstance(creditos, int):
            self.__creditos = creditos
        else:
            print("La variable no es un entero.")