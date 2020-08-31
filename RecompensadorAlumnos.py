import operator

def definirDetallesAlumnos():
    print()
    print("Ingrese el numero de alumnos")
    numeroDeEstudiantes = int(input())
    listaDeAlumnos = {}
    for alumno in range(0, numeroDeEstudiantes):
        print("Ingrese el nombre del Alumno")
        nombre = input()
        print("Ingrese la nota")
        nota = int(input())
        listaDeAlumnos[nombre] = nota
        print()
    return listaDeAlumnos

def rankearAlumnos(listaDeAlumnos):
    try:
            print()
            listaOrdenada = sorted(listaDeAlumnos.items(), key = operator.itemgetter(1),reverse = True)
            print(listaOrdenada)

            print("{} ha salido primero en la competencia de notas, sacando {} como nota".format(listaOrdenada[0][0], listaOrdenada[0][1]))
            print("{} ha salido segundo en la competencia de notas, sacando {} como nota".format(listaOrdenada[1][0], listaOrdenada[1][1]))
            print("{} ha salido tercero en la competencia de notas, sacando {} como nota".format(listaOrdenada[2][0], listaOrdenada[2][1]))
            print()
            return listaOrdenada
    except IndexError:
        print("Tiene que ingresar un minimo de al menos 3 alumnos")
        quit()


def recompensarAlumnos(listaOrdenada, recompensa):

    print("{} recibio una recompensa de {}".format(listaOrdenada[0][0], recompensa[0]))
    print("{} recibio una recompensa de {}".format(listaOrdenada[1][0], recompensa[1]))
    print("{} recibio una recompensa de {}".format(listaOrdenada[2][0], recompensa[2]))

def privilegiarAlumnos(listaOrdenada):
    print()
    for i in listaOrdenada:
        if i [1] >= 950:
            print("Felicitaciones por obtener {} como nota {}".format(i[1], i[0]))
        else:
            break

listaDeAlumnos = definirDetallesAlumnos()
listaOrdenada = rankearAlumnos(listaDeAlumnos)
recompensa = ("Un chocolate", "Una bolsa de caramelos", "Un chupetin")
recompensarAlumnos(listaOrdenada, recompensa)
privilegiarAlumnos(listaOrdenada)
