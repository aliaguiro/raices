from math import sqrt

def raices ():
    opc=int(input("""
PRESIONE
    1 para hacer obtener raices
    2 para salir \n"""))
    while (opc >0 and opc <2):
        a=int(input('Ingrese a: '))
        b=int(input('Ingrese b: '))
        c=int(input('Ingrese c: '))
        if ((pow(b,2))-4*a*c) < 0:
            print("La solución de la ecuación es con numeros complejos")
            opc=int(input("""
PRESIONE
    1 para hacer obtener raices
    2 para salir \n"""))
        else:
            x1 = ((-1*b)+sqrt(pow(b,2)-(4*a*c)))/(2*a)
            x2 = ((-1*b)-sqrt(pow(b,2)-(4*a*c)))/(2*a)
            print('raiz 1=', x1)
            print('raiz 2=', x2)
            opc=int(input("""
PRESIONE
    1 para hacer obtener raices
    2 para salir \n"""))



raices()
