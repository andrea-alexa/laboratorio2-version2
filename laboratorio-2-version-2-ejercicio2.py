'''Desarrollar un programa que solicite tres números enteros desde teclado al usuario,
luego el programa deberá determinar e indicar a través de un mensaje en pantalla,
cuál de los tres es el más grande sin importar el orden que se ingrese los números,
así mismos el número más pequeño y el número de en medio.'''

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

#Determinar el numero mayor
if num1 > num2 and num1 > num3:
    print("El numero ", num1, " es el numero mas grande de los 3")
elif num2 > num1 and num2 > num3:
    print("El numero ", num2, " es el numero mas grande de los 3")
else:
    print("El numero ", num3, " es el numero mas grande de los 3")

#Determinar el numero mas pequeño
if num1 < num2 and num1 < num3:
    print("El numero ", num1, " es el numero mas pequeño de los 3")
elif num2 < num1 and num2 < num3:
    print("El numero ", num2, " es el numero mas pequeño de los 3")
else:
    print("El numero ", num3, " es el numero mas pequeño de los 3")

#Determinar el numero del medio
if num1 != num2 and num1 != num3:
    print("El numero ", num1, " es el numero de en medio de los 3")
elif num2 != num1 and num2 != num3:
    print("El numero ", num2, " es el numero de en medio de los 3")
else:
    print("El numero ", num3, " es el numero de en medio de los 3")