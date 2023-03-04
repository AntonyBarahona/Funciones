#una empresa actualmente se encuentra en proceso de seleccion de personal por lo que: se nesecita de un programa  que permita almacenar el nombre de las personas que llegan a entrevista y la cantidad total de personas entrevistadas en los diferentes dias 
postulantes=[]
def obtenerDatos():
    nombres=input("ingrese nombre postulante ")
    postulantes.append(nombres)
    print(nombres + " ha sido añadido correctamente")
    preguntaIngreso()

def salida():
    conteo=0
    for x in postulantes:
        conteo=conteo+1
        print(conteo," ",x)


def preguntaIngreso():
    print("¿Hay nuevos postulantes ?")
    respuesta=input("s/n ")
    if  respuesta=="S"or respuesta=="s":
        obtenerDatos()
    else:
        salida()
preguntaIngreso()