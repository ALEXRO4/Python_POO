from cosas import Alumno


def main():
    """"
    al1 = Alumno()
    print(al1)
    al2 = Alumno()
    print(al1.facultado)
    print(al2.facultado)
    print(Alumno.facultado)
   # al1.facultado = "FES Aragon EDOMEX" se esta agregando otro atributo de instancia
    Alumno.facultado = "Fes Aragon EDOMEX"
    print(al1.facultado)
    print(al2.facultado)
    print(Alumno.facultado)
    print("-------- vistazo a los objetos----------")
    print(vars(al1))
    print(vars(al2))
    print("-------- Modificar atributos publicos----------")
    al1.edad = 999
    print(vars(al1))
    print(vars(al2))
    """

    al1 = Alumno("Diego", 19, "ICO")
    al2 = Alumno("Montse", 20, "ICO")
    print(vars(al1))
    al1.__edad = 333
    print(al1.__edad)
    print (


        vars(al1))
    """"
    print(al1.nombre)
    print(al1.facultado)
    print(al1.edad)
    print(al1.carrera)
    al2.edad = 999
    print(al2.edad)
    print(al2.carrera)
    print(al2.facultado)
"""
main()
