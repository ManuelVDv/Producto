from MySql.Persona import Persona

class Estudiante(Persona):

    def __init__(self, nombre, edad, programa):
        super().__init__(nombre, edad)
        self.__programa = programa

    def get_programa(self):
        return self.__programa

    def set_programa(self, programa):
        self.__programa = programa

    def saludar(self):
        return f"Hola, soy {self.get_nombre()}, tengo {self.get_edad()} años y estudio {self.__programa}."
