from cosas import Alumno, Perro

def main():
    al1 = Alumno("Jose", 19, "ICO")

    print(vars(al1))
    al1.__nombre ="Diego"
    print(vars(al1))

    al1.set_nombre("Maria")
    print(vars(al1))

    print("--------To String---------")
    print(al1)
    al1.set_edad(999)
    print(al1)
    al1.estudiar(4)

    perrito = Perro("Poddle", 2,0.35)
    print(vars(perrito))
    perrito.raza = "De la calle " #set en formato phyton
    perrito.__raza = "otra"
    print(vars(perrito))
    perrito.ladrar(11)
    perrito.ladrar(3)
    perrito.edad = 12
    perrito.estatura = 0.43
    print(perrito)

    cachorro = Perro.es_cachorro(perrito.edad)
    print(cachorro)
    Perro.dormir()

    danes = Perro.perro_grande(0.8)
    print(danes)

main()