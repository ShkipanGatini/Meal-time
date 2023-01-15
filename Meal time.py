def main():                                                       #Función principal
    time=input("Cual es el horario exacto?.Ex= 14:59")
    if convert(time)>=700 and convert(time)<=1159:                                           #El usuario pone el horario en el formato "hora:minutos"
        print("Es el horario del desayuno")                                                  #La función va a buscar (time ) a la subfunción más abajo
    elif convert(time) >=1200 and convert(time)<=1430:
        print("Es el horario del almuerzo")
    elif convert(time)>=1431 and convert(time)<=2030:
        print("Es muy tarde para almorzar y muy temprano para cenar, todavía no vamos a comer, tal vez una fruta?")
    elif convert(time)>=2031 and convert(time)<=2300:
        print("Hora de la cena!")
    else:
        print(" Es hora de dormir")

    



def convert(time):                                                        #Convert time toma el horario, lo abre en dos.
    hours, minutes =time.split(":")                                        #lo suma como si fuese un string.
    newtime=hours+minutes
    newtimeStr=int(newtime)                                                #lo pasa a INT
    return newtimeStr                                                       #Lo devuelve a MAIN.




main()
input("Aprete cualquier tecla para salir")