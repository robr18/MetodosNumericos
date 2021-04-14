"""Importacion de la libreria 'sympy' para las operaciones"""
"""Instalacion en windows: pip install sympy """
"""Instalacion en linux: pip3 install sympy"""
import sympy as sp



""" Prueba de Integracion Definida en un punto"""

x= sp.symbols('x') #Define el symbolo de la variable con la que se va trabajar

fx = 2*x**2        #Se define la funcion con el simbolo que se difinio arriba

"""Integracion con la funcion 'integrate' recibe (fx,x),
donde fx: es la funcion a evaluar
x: es la variable sobre la cual se va evaluar la funcion"""

integral = sp.integrate(fx,x).subs(x,5)     #el agregado .subs(x,valor) sustituye la variable x por el valor que pongamos (5) 
                                            #asi evalua la funcion en el punto dado

"""Derivacion con la funcion 'diff' recibe (fx,x),
donde fx: es la funcion a evaluar
x: es la variable sobre la cual se va evaluar la funcion"""

derivada = sp.diff(fx,x).subs(x,5)      #el agregado .subs(x,valor) sustituye la variable x por el valor que pongamos (5) 
                                        ##si evalua la funcion en el punto dado


"""Impresion de los resultados de las operaciones"""

print("Solucion de la integral :"+str(integral))    #str(variable) = esto convierte la variable en un string para imprimir sin cambiarle el tipo a la variable original

print("Solucion de la derivada :"+str(derivada))

#Para realizar la integra y derivada indefinida simplemente se borra el .subs(x,valor)
#Disculpen la falta de acentos uso un teclado en ingles