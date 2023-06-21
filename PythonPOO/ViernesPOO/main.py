from Cosas import *

def main():
    per1 = Persona("Jose",19)
    print(per1)
    print(Persona.descripcion)
    print("-------Herencia--------")
    al1 = Alumno("Jose",19,"232344554223","ICO")
    print(al1)
    print(Alumno.descripcion)

    al2 = Alumno.constructor_defecto()
    print(al2)
    al2.nombre = "Juan"
    print(al2)
    al2.dormir()

    print("-----herencia Profe-----")
    profe1= Profesor("Jesus",30+16,21323231,"Ingenieria en software")
    print(profe1)
    profe1.dormir()

    print("------Herencia de ayudamte Profesot---------")
    ayudante = AyudanteProfesor("Adrian",20,"32324242432","ICO",1213141,"Ingenieria en software",4)

    ayudante.dormir()

    ayudante.nombre = "Abraham"
    
main()