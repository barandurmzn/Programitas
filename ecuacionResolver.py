
print "Este es un programa que prueba todas las combinaciones de numeros positivos hasta resolver la ecuacion"
print "Es un metodo poco efectivo, por lo que se recomiendan numeros pequenos"
print "Debes escribir la ecuacion en el programa"
print "Para ello haz clic izquierdo y dale a editar"

#Sintaxis de la ecuacion:
#Sumar +
#Restar -
#Multiplicar *
#Dividir /
#Resto de division %
#Elevar **
#Es igual ==
#No es igual !=
#Mayor o igual >=
#Menor o igual <=


def bruteForceEcuacion(nIncog, nMax):
    x = 0
    y = 0
    z = 0
    noTieneSolucion = True 
    print "Calculando..."
    while x<=nMax:
        if nIncog >= 2:
            while y <= nMax:
                if nIncog >= 3:
                    while z <= nMax:
                        if(6*(x**2)*y - 5*(x**3)- 7*y*z- 2*x == 0): #Aqui debes poner la ecuacion si tiene 3 incognitas
                            print "x es %s , y es %s z es %s" % (x, y, z)
                            noTieneSolucion = False
                        z+=1
                else:
                    if(x+y==18): #Aqui debes poner la ecuacion si tiene 2 incognitas
                        print "x es %s e y es %s" % (x, y)
                        noTieneSolucion = False
                y+=1
                z=0
        else:
            if(x==18): #Aqui debes poner la ecuacion si tiene 1 incognita
                print "x es %s" % (x)
                noTieneSolucion = False
        z=0
        y=0
        x+=1
    if noTieneSolucion:
        print "La ecuacion no tiene solucion con incognitas hasta %s" % (nMax)

bruteForceEcuacion(int(raw_input("Pon el numero de incognitas(x, y, z). Expresar mediante un numero del 1 al 3: ")), int(raw_input("Pon el numero maximo al que pueden llegar las incognitas: ")))

raw_input("Dale a enter para salir ")
