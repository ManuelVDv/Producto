from MySql.Persona import Persona

class Profesor(Persona):

    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.__materia = materia

    def get_materia(self):
        return self.__materia

    def set_materia(self, materia):
        self.__materia = materia

    def saludar(self):
        return f"Hola, soy el profesor {self.get_nombre()}, tengo {self.get_edad()} años y enseño {self.__materia}."

