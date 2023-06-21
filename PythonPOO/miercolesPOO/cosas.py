class Alumno:
    facultad = "FES Aragón"

    def __init__(self, nom, ed, carr):
        self.__nombre = nom
        self.__edad = ed
        self.__carrera = carr


    def set_nombre(self,nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_edad(self,ed):
        if ed >= 8 and ed <120:
            self.__edad = ed
        else:
            print("Esa edad no es correcta")
            self.__edad = 0

    def get_edad(self):
        return self.__edad

    def set_carrera(self, carr):
        self.__carrera = carr

    def get_carrera(self):
        return  self.__carrera

    def __str__(self):
        cadena = " Nombre: "+self.__nombre
        cadena = cadena + "\n Edad: "+ str(self.__edad)
        cadena = cadena + "\n Carrera: "+ str(self.__carrera)
        return cadena

    def estudiar(self,horas = 1):
        print(f"El aulumno {self.__nombre} esta estudiando por {horas} horas")

class Perro:
    reino = "Canino"

    def __init__(self,raza,edad,estatura):
        self.__raza = raza
        self.__edad = edad
        self.__estatura = estatura

    @property
    def raza(self):
        return self.__raza

    @raza.setter
    def raza(self,raza):
        self.__raza = raza

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self,edad):
        if edad > 0 and edad < 20:
            self.__edad = edad
        else:
            print("Esa no es una edad valida")
            self.__edad = 0

    @property
    def estatura(self):
        return self.__estatura

    @estatura.setter
    def estatura(self,estatura):
        if estatura > 0.1 and estatura < 1.1:
            self.__estatura = estatura
        else:
            print("Esa no es una estatura valida")
            self.__estatura = 0

    def __str__(self):
        return  f"""        Raza: {self.__raza} 
        /Edad: {self.__edad} 
        /Estatura: {self.__estatura}"""

    def ladrar(self, ladridos):
        if ladridos < 10:
            print(f"El perro ladro {ladridos} veces")
        else:
            print("El perro no puede ladrar tanto ajsja ")


    @staticmethod #Hace que el metodo le pretenezca a la clase
    def es_cachorro(edad):
        return edad < 3

    @staticmethod
    def dormir(veces = 5):
        for n in range(veces):
            print(f"Dando vuelta {n+1}")
        print("ZZZzzzz!")

    @classmethod
    def perro_grande(cls,est):
        if est > 0.79:
            return cls("",0,est)