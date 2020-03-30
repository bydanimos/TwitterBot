#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Proyecto del bot de Twitter de @TryOfBot primera cuarentena

import tweepy
import time
import random
import codecs


print('This is my twitter warbot')

CONSUMER_KEY = '--------'
CONSUMER_SECRET = '------'
ACCESS_KEY = '-----'
ACCESS_SECRET = '-----'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.trucos = []
    self.kills = ''
  def agregar_truco(self, truco):
        self.trucos.append(truco)


def muertes():
    L = []
    Jugadores = ["user1", "user2", "user3"]
    M = [" user1's atack.",
    " user2's atack.",
    " user3's atack."]
    M2 = [" user1's atack.",
    " user2's atack.",
    " user3's atack."]
    print (len(Jugadores), len(M), len(M2))

    Muertos = []
    f = codecs.open("escoger.txt", "r", "utf-8")
    lista = []
    dato = f.readline()
    lista.append(dato[:-1])
    f.close()
    print (str(dato))
    if str(lista[0]) ==  "0":
        k = 0
        while k < len(Jugadores):
            L.append(Person(Jugadores[k], 3))
            L[k].agregar_truco(M[k])
            L[k].agregar_truco(M2[k])
            L[k].kills = 0

            print (L[k].name, L[k].age, L[k].trucos[0], L[k].trucos[1], L[k].kills)
            k += 1
    else:
        f = codecs.open("fichero.txt", "r", "utf-8")
        dato = f.readlines()
        L = []
        if __name__ == "__main__":
            lineas = []
            for linea in dato:
                lineas.append(linea[:-1])
            k = 0
            while k < len(lineas):
                  L.append(Person(lineas[k], lineas[k+1]))
                  x = k / 5
                  L[x].kills = lineas[k + 2]
                  L[x].agregar_truco(lineas[k+3])
                  L[x].agregar_truco(lineas[k+4])
                  k += 5
                  print (L[x].name, L[x].age, L[x].trucos[0], L[x].trucos[1], L[x].kills)
            f.close()
    f = open("contador.txt", "r")
    dato = f.readlines()
    contadores = []
    for linea in dato:
        contadores.append(linea[:-1])
    i = int(contadores[0])
    j = int(contadores[1])
    ataque = int(contadores[2])
    muerte = int(contadores[3])
    print (i, j, ataque, muerte)
    f.close()

    while len(L) > 1:

        a = b = 0
        while a == b:
            a = random.randint(0, len(L) - 1)
            b = random.randint(0, len(L) - 1)
            c = random.randint(0, 1)
        L[b].age = int(L[b].age) - 1
        print (a, b, c)
        if L[b].age == 0:
            muerte += 1; ataque += 1
            L[a].kills = int(L[a].kills) + 1
            print ("Siendo la muerte numero: " + str(muerte) + " y el ataque numero: " + str(ataque)+ "\n@" + L[a].name + " ha matado a @" + L[b].name + L[a].trucos[c] + "\n" + L[a].name + " lleva " + str(L[a].kills) + " kill(s).\nQuedan " + str(len(L) - 1) + " supervivientes! #WarBot")
            time.sleep(60)
            print ("1 seg para publicar\n")
            api.update_status("Siendo la muerte numero: " + str(muerte) + " y el ataque numero: " + str(ataque)+ "\n@" + L[a].name + " ha matado a @" + L[b].name + L[a].trucos[c] + "\n" + L[a].name + " lleva " + str(L[a].kills) + " kill(s).\nQuedan " + str(len(L) - 1) + " supervivientes! #WarBot")
            Muertos.append(L[b].name)
            L.pop(b)
            f = open("muertos.txt", "a")
            f.write(Muertos[-1] + "\n")
            f.close()
        else:
            ataque += 1
            print ("Siendo el ataque numero: " + str(ataque) + "\n@" + L[a].name + " ha herido a @" + L[b].name + L[a].trucos[c] + "\n" + L[b].name + " tiene: " + str(L[b].age) + " vidas.\nQuedan " + str(len(L)) + " supervivientes! #WarBot")
            time.sleep(60)
            print ("1 seg para publicar\n")
            api.update_status("Siendo el ataque numero: " + str(ataque) + "\n@" + L[a].name + " ha herido a @" + L[b].name + L[a].trucos[c] + "\n" + L[b].name + " tiene: " + str(L[b].age) + " vidas.\nQuedan " + str(len(L)) + " supervivientes! #WarBot")
        f = open("fichero.txt", "w")
        for k in range(len(L)):
            a = L[k].name; b = L[k].age; c = L[k].kills; d = L[k].trucos[0]; e = L[k].trucos[1]
            f.write(str(a) + "\n")
            f.write(str(b) + "\n")
            f.write(str(c) + "\n")
            f.write(str(d) + "\n")
            f.write(str(e) + "\n")
        f.close()
        f = open("escoger.txt", "w")
        f.write("1")
        f.close()
        if len(L) == 5 and j == 0:
            api.update_status("Quedan cinco supervivientes, atentos!!\nSuerte a: @" + L[0].name + " @" + L[1].name + " @" + L[2].name + " @" + L[3].name + " @" + L[4].name)
            print ("Quedan cinco supervivientes, atentos!!\nSuerte a: @" + L[0].name + " @" + L[1].name + " @" + L[2].name + " @" + L[3].name + " @" + L[4].name)
            j += 1
        elif len(L) == 4:
            j = 0
        elif len(L) == 3 and j == 0:
            api.update_status("Quedan tres supervivientes, atentos!!\nSuerte a: @" + L[0].name + " @" + L[1].name + " @" + L[2].name)
            print ("Quedan tres supervivientes, atentos!!\nSuerte a: @" + L[0].name + " @" + L[1].name + " @" + L[2].name)
            j += 1
        elif len(L) == 1:
            print ("Tenemos un ganador!! El ganador es... @" + L[0].name)
            print ("Enhorabuena por el top 3 a: @" + Muertos[-1] + " @" + Muertos[-2] + "\nMuchas gracias a todas y a todos por participar!!")
            api.update_status("Tenemos un ganador!! El ganador es... @" + L[0].name)
            api.update_status("Enhorabuena por el top 3 a: @" + Muertos[-1] + " @" + Muertos[-2] + "\nMuchas gracias a todas y a todos por participar!!")
        f = open("contador.txt", "w")
        i += 1
        f.write(str(i) + "\n")
        i -= 1
        f.write(str(j) + "\n")
        f.write(str(ataque) + "\n")
        f.write(str(muerte) + "\n")
        f.close()

        if i % 16 == 0:
            print ("Descansito ")
            time.sleep(60*60*8)
            #time.sleep(60)

        time.sleep(59*60)

        i += 1
        print (i)

muertes()
