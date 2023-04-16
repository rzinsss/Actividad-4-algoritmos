mes_actual = int(input())
año_actual = int(input())
numero_de_personas_por_atender = int(input())
Cantidad_de_gente_aprobada = 0
Cantidad_de_Arstotzkanos = 0
cantidad_respuestas_correctas = 0
respuesta = 0
cantidad_rublos = 0 
oracion = str()
for i in range(0,numero_de_personas_por_atender):
    print("Papers, please")
    nombre = input()
    lugar = input()
    if lugar == "Arstotzka":
        print("Puede pasar", nombre)
        Cantidad_de_Arstotzkanos += 1
        Cantidad_de_gente_aprobada += 1
    elif lugar == "3Z1C":
        mision = input()
        if mision == "transcripcion":
            cant_palabras = int(input())
            for i in range(0,cant_palabras):
                palabra1 = input()
                palabra2 = input()
                palabra3 = input()
                oracion = oracion+palabra1+" "
            print(oracion+"-EZIC")
            oracion = str()
        elif mision == "soborno":
            dinero = int(input())
            cantidad_rublos += dinero
            print("Gracias por su donacion de",dinero,"rublos a Arstotzka")
            print("Ahora tengo un total de",cantidad_rublos,"rublos")
        elif mision == "sabotaje":
            tarea = input()
            rublos_necesarios = int(input())
            if cantidad_rublos >= rublos_necesarios:
                print("Yo me encargo de",tarea)
                cantidad_rublos -= rublos_necesarios
                print("Ahora tengo un total de",cantidad_rublos,"rublos")
            else:
                print("No tengo rublos suficientes para",tarea)
                print("Ahora tengo un total de",cantidad_rublos,"rublos")
    elif lugar != "Arstotzka" and lugar != "3Z1C":
        print("Permiso de entrada por favor")
        nombre_pasaporte = input()
        mes_vencimiento = int(input())
        año_vencimiento = int(input())
        if nombre != nombre_pasaporte or año_vencimiento<año_actual or (año_actual == año_vencimiento and mes_vencimiento<mes_actual):
            print("No puede pasar", nombre)
            if nombre != nombre_pasaporte:
                print("Su nombre en su permiso no coincide con el de su pasaporte")
            elif año_vencimiento<año_actual or (año_actual == año_vencimiento and mes_vencimiento<mes_actual):
                print("Su permiso de entrada esta vencido")
        else:
            razon_viaje = str(input())
            print("Indique su razon de entrada a la gloriosa nacion de Arstotzka")
            if razon_viaje == "trabajo":
                print("Resuelva esta interrogacion de calculo")
                while not respuesta == 1:
                    num1 = int(input())
                    num2 = int(input())
                    operacion = input()
                    respuesta_migrante = int(input())
                    if operacion == "sumar":
                        suma = num1+num2
                        if respuesta_migrante == suma:
                            print("Tu respuesta esta correcta")
                            cantidad_respuestas_correctas += 1
                        else:
                            print("Tu respuesta fue",respuesta_migrante,"y deberia ser",suma,"esta incorrecta")
                            respuesta = 1
                    elif operacion == "restar":
                        resta = num1-num2
                        if respuesta_migrante == resta:
                            print("Tu respuesta esta correcta")
                            cantidad_respuestas_correctas += 1
                        else:
                            print("Tu respuesta fue",respuesta_migrante,"y deberia ser",resta,"esta incorrecta")
                            respuesta = 1
                    elif operacion == "multiplicar":
                        multiplicacion = num1*num2
                        if respuesta_migrante == multiplicacion:
                            print("Tu respuesta esta correcta")
                            cantidad_respuestas_correctas += 1
                        else:
                            print("Tu respuesta fue",respuesta_migrante,"y deberia ser",multiplicacion,"esta incorrecta")
                            respuesta = 1
                    elif operacion == "resto":
                        resto = num1%num2
                        if respuesta_migrante == resto:
                            print("Tu respuesta esta correcta")
                            cantidad_respuestas_correctas += 1
                        else:
                            print("Tu respuesta fue",respuesta_migrante,"y deberia ser",resto,"esta incorrecta")
                            respuesta = 1
                    elif operacion == "parte entera":
                        parte_entera = num1//num2
                        if respuesta_migrante == parte_entera:
                            print("Tu respuesta esta correcta")
                            cantidad_respuestas_correctas += 1
                        else:
                            print("Tu respuesta fue",respuesta_migrante,"y deberia ser",parte_entera,"esta incorrecta")
                            respuesta = 1
                if cantidad_respuestas_correctas >= 3:
                    print("Puede pasar", nombre_pasaporte)
                    Cantidad_de_gente_aprobada += 1
                    cantidad_respuestas_correctas = 0
                    respuesta = 0
                else:
                    print("No puede pasar",nombre_pasaporte)
                    print("Faltan respuestas correctas")
                cantidad_respuestas_correctas = 0
                respuesta = 0
            elif razon_viaje == "turismo":
                numero_serie_pasaporte = int(input())
                if ((numero_serie_pasaporte//10000000) + (numero_serie_pasaporte//1000000)%10 + (numero_serie_pasaporte//100000)%10 + (numero_serie_pasaporte//10000)%10 + (numero_serie_pasaporte//1000)%10 + (numero_serie_pasaporte//100)%10 + (numero_serie_pasaporte//10)%10 + numero_serie_pasaporte%10)%5 != 0:
                    print(nombre_pasaporte,"a detencion")
                    print("Su documentacion esta falsificada")
                else:
                    print("Puede pasar",nombre_pasaporte)
                    Cantidad_de_gente_aprobada += 1
            elif razon_viaje != "turismo" or razon_viaje != "trabajo":
                print("No puede pasar",nombre_pasaporte)
    else:
        Cantidad_de_gente_aprobada += 1
print("Gloria a Arstotzka!")
print("Cantidad de gente aprobada:", Cantidad_de_gente_aprobada)
print("Cantidad de Arstotzkanos:", Cantidad_de_Arstotzkanos)
print("este archivo fue modificado")
