#encoding: UTF-8#Autor: Saúl Rodrigo Toral Luna, Matricula: A01745007#  Descripción: Ingresando la velocidad deseada, el usuario podra calcular las distancias recorridas#al igual que podrá calcular el tiempo en base a distancias.# Calcular: La distancia en km. que recorre en 6 hrs.# Calcular:La distancia en km. que recorre en 10 hrs.# Calcular: El tiempo en horas que requiere para recorrer 500 km# 1.- Ingresar la velocidad y establecer los valoresv = input("Ingresa la velocidad deseada: ")#2.- Realizar las operaciones para cada puntod1 = float(v) * (6)d2 = float(v) * (10)#3.- Calcular el tiempot1 = (500) / float(v)#4.- Imprimir resultadosprint("La distancia recorrida en 6hrs es de: ")print (d1, "km/h")print("La distancia recorrida en 10 hrs es de: ")print(d2, "km/h")print("El tiempo en recorrer 500 Km es de: ")print (t1, "horas")