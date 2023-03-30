'''Construye un programa que, registre que un policía de tránsito reporta a la central un promedio 
de N infracciones en el mes de las cuales el 20% se producen en las horas de la mañana, el 35% se producen
 en horas de la tarde y el 45% restante se producen en horas de la noche. Realizar un programa que calcule e imprima lo siguiente.
Promedio diario matutino de infracciones
Promedio diario vespertino de infracciones
Promedio diario nocturno de infracciones
'''
numInf = int(input("Escriba el numero de infracciones que regsitro el policia de transito: "))
diasMes = 30
infracciones = numInf/diasMes
print("Las infracciones reprtadas en el mes son: \n ", numInf)

print(" En la mañana se producen un total de ")
infracciones * 20/100
print(infracciones,"es el numero promedio diario de casos matutino. ")

print("====================================================================")

print(" En la tarde se producen un total de ")
infracciones * 35/100


print(infracciones,"es el numero promedio diario de casos vespertinos. ")

print("====================================================================")

print(" En la noche se producen un total de ")
infracciones * 45/100

print(infracciones,"es el numero promedio diario de casos nocturnos. ")

print("Fin del programa")











#NumInfr = int(input("Escriba la cantidad de infracciones:\n"))


