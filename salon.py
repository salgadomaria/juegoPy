import question
import pygame, sys
import time
import personaje
import botones

pygame.init()

def gameover(pant):
    finfondo = pygame.image.load('pixeles\endeljuego.png')
    pant.blit(finfondo, (0, 0))
    pygame.display.update()
    time.sleep(10)

def comprobarPregunta(pregunta,rta,vidasactivas,screen):
    p1 = question.pregunta()
    p1.contestar(pregunta, rta,vidasactivas)
    # Abre el archivo para leerlo
    with open("rta.txt", "r") as archivo:
        # Lee el contenido del archivo
        rtafinal = archivo.read()
    if rtafinal == "True":
        # SIGUIENTE NIVEL
        return (False, False, True, vidasactivas)
    else:
        vidasactivas = vidasactivas - 1
        #print(f"va devolver {vidasactivas}")
        if vidasactivas == 0:
            gameover(screen)
            return (True, False, False, 3)
        else:
            return (False, True, False, vidasactivas)


def Salon_ed_fisica(edFisica, vidaActivada, vidaDesactivada, minutos, reloj1, fuente, vidasactivas, tardo):
    if edFisica == True:
        screenedFisica = pygame.display.set_mode((1000, 700))
        fondoEdFisica = pygame.image.load('pixeles\salones\edFisica.png')
        llaveImg = pygame.image.load('pixeles\otones\llave.png')
        llaveEncontrada = pygame.image.load('pixeles\otones\llaveEncontrada.png')
        pygame.display.set_caption(" Nivel: Facil   Educacion Fisica")
        sigueDerecha, sigueIzquierda, sigueFrente, sigueEspalda = False, False, False, False
        seguir = sigueDerecha, sigueIzquierda, sigueFrente, sigueEspalda

        inc=True
        x= 310
        y=110
        i=0
        colortemp = 255, 255, 255
        inc2 = False
        c, j, p, f, ultimo = False, False, False, False, False
        ll1 = False
        ll2 = False
        ll3 = False
        llaves = False, False, False


        while edFisica == True:
            screenedFisica.fill((0, 0, 0))
            screenedFisica.blit(fondoEdFisica, (0, 0))
            #cronometro
            tiempo = round(pygame.time.get_ticks() / 1000)
            segundos = round(tiempo) - tardo
            fin = segundos
            #print(f"{tiempo} - {tardo} = {segundos}")

            # print(segundos)
            if segundos == 60 and c == False:
                minutos +=1
                c = True
            if segundos == 120 and j == False:
                minutos +=1
                j = True
            if segundos == 180 and p == False:
                minutos +=1
                p = True
            if segundos == 240 and f == False:
                minutos +=1
                f = True
            if segundos == 300 and ultimo == False:
                minutos +=1
                ultimo = True

            if segundos > 239:
                segundos = segundos-60
                colortemp = 255, 0, 0
            if segundos > 179: segundos = segundos-60
            if segundos > 119: segundos = segundos-60
            if segundos > 59: segundos = segundos-60
            #print(segundos)

            if inc == True:
                per = personaje.Personaje()
                per.crear(screenedFisica, (x, y))
                llave1 = botones.Pistallave(llaveImg, llaveEncontrada)
                llave2 = botones.Pistallave(llaveImg, llaveEncontrada)
                llave3 = botones.Pistallave(llaveImg, llaveEncontrada)

                inc = False
            else:
               per.crear(screenedFisica, (x,y))

            if ll1 == False:
                llave1.crearllave(screenedFisica, (400, 100))
            else:
                llave1.found(screenedFisica)

            if ll2 == False:
                llave2.crearllave(screenedFisica, (500, 250))
            else:
                llave2.found(screenedFisica)

            if ll3 == False:
                llave3.crearllave(screenedFisica, (800, 500))
            else:
                llave3.found(screenedFisica)



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYUP:
                    per.parar(event, seguir)
                #print(f"{seguir} primero")
                if event.type == pygame.KEYDOWN or any(seguir):
                 #   print(f"{seguir} segundo")
                    if hasattr(event, 'key'):
                        if i > 2:
                            i = 0
                        seguir = per.mover(event, screenedFisica, i, seguir)
                        i = i+1
                        if event.key == pygame.K_f:
                            persRec = per.obtener()
                            if ll1 == False: ll1 = llave1.esllave(screenedFisica, persRec)
                            if ll2 == False: ll2 = llave2.esllave(screenedFisica, persRec)
                            if ll3 == False: ll3 = llave3.esllave(screenedFisica, persRec)

            x, y = per.obtPosisiones()
            reloj1.tick(60)



            if fin > 299 :
                cronometro = fuente.render(f" Tiempo 5:00", 0, (colortemp))
                screenedFisica.blit(cronometro, (20, 5))
                #edFisica= False
                #matematica = False
                #devuelve inicio edFisica ingles vidasActiva
                #print("menu inicial")
                gameover(screenedFisica)
                return (True, False, False, 3, 0, 0, 0)
                # devolver true para inicio y crear in while edFisica = Inicio(reloj1, menu, edFisica, matematica)
            else:
                cronometro = fuente.render(f" Tiempo {minutos}:{segundos}", 0, (colortemp))
                screenedFisica.blit(cronometro, (20, 5))

            llaves = (ll1, ll2, ll3)

            if all(llaves) == True:
                menu = None
                esta =None
                sigue = None
                menu, esta, sigue, vidasactivas =comprobarPregunta("¿Por cuantos jugadores esta compuesto un equipo de futbol?","11",vidasactivas,screenedFisica)
                #print(f"mi 1 valor es  {menu}")
                if sigue == True:
                    #avanza de nivel
                    tiempo = round(pygame.time.get_ticks() / 1000)
                    #print(f"minutos: {minutos}  segundos:{segundos}  segundos Totales:{tiempo}")
                    return (False, False, True, vidasactivas, minutos, segundos, tiempo)
                if menu == True:
                    #ya no tiene mas vidas
                    return (True, False, False, 3, 0 ,0,0)



            if vidasactivas == 3:
                screenedFisica.blit(vidaActivada, (690, 0))
                screenedFisica.blit(vidaActivada, (790, 0))
                screenedFisica.blit(vidaActivada, (890, 0))
            elif vidasactivas == 2:
                screenedFisica.blit(vidaActivada, (690, 0))
                screenedFisica.blit(vidaActivada, (790, 0))
                screenedFisica.blit(vidaDesactivada, (890, 0))
            elif vidasactivas == 1:
                screenedFisica.blit(vidaActivada, (690, 0))
                screenedFisica.blit(vidaDesactivada, (790, 0))
                screenedFisica.blit(vidaDesactivada, (890, 0))



            # if all(llaves) == True and inc2 == False:
            #     p1 = question.pregunta()
            #     p1.contestar("¿Por cuantos jugadores esta compuesto un equipo de futbol?", "11")
            #     inc2 = True
            #     # Abre el archivo para leerlo
            #     with open("rta.txt", "r") as archivo:
            #         # Lee el contenido del archivo
            #         rtafinal = archivo.read()
            #     if rtafinal == "True":
            #         # SIGUIENTE NIVEL
            #         return False, False, True, False, False, 3
            #     else:
            #         vidasactivas = vidasactivas - 1
            #         if vidasactivas == 0:
            #             gameover(screenedFisica)
            #             edFisica = False
            #             matematica = False
            #             return True, False, False, False, False,3

            # if vidasactivas == 1:
            #     pygame.display.update()
            #     p1.contestar("¿Por cuantos jugadores esta compuesto un equipo de futbol?", "11")
            #     # Abre el archivo para leerlo
            #     with open("rta.txt", "r") as archivo:
            #         #Lee el contenido del archivo
            #         rtafinal = archivo.read()
            #     if rtafinal == "True":
            #         #SIGUIENTE NIVEL
            #         return False, False, True, False, False,vidasactivas
            #     else:
            #         vidasactivas = vidasactivas - 1
            #         gameover(screenedFisica)
            #         return True, False, False,False, False,3


            # if vidasactivas == 2:
            #     pygame.display.update()
            #     p1.contestar("¿Por cuantos jugadores esta compuesto un equipo de futbol?", "11")
            #     # Abre el archivo para leerlo
            #     with open("rta.txt", "r") as archivo:
            #         #Lee el contenido del archivo
            #         rtafinal = archivo.read()
            #     if rtafinal == "True":
            #         # SIGUIENTE NIVEL
            #         return False, False, True, False, False, vidasactivas
            #     else:
            #         vidasactivas = vidasactivas - 1






            # Actualiza la pantalla
            pygame.display.update()


def salonIngles(ingles, vidaActivada, vidaDesactivada, minutos, secont, secontAnt, reloj1, fuente,vidasactivas):
    if ingles == True:
        screen_ingles = pygame.display.set_mode((1000, 700))
        fondo_ingles = pygame.image.load('pixeles\salones\ingles.png')
        llaveImg = pygame.image.load('pixeles\otones\llave.png')
        llaveEncontrada = pygame.image.load('pixeles\otones\llaveEncontrada.png')
        pygame.display.set_caption(" Nivel: Intermedio Ingles")
        inc=True
        x= 590
        y=130
        i=0
        colortemp = 255, 255, 255
        inc2 = False
        rtafinal = None
        ultimaTecla = None
        c, j, p, f, ultimo = False, False, False, False, False
        ll1 = False
        ll2 = False
        ll3 = False
        llaves = False, False, False
        minxseg = minutos
        sgTotalAnt = 0
        segComp = secont
        sigueDerecha, sigueIzquierda, sigueFrente, sigueEspalda = False, False, False, False
        seguir = sigueDerecha, sigueIzquierda, sigueFrente, sigueEspalda

        while ingles == True:
            screen_ingles.fill((0, 0, 0))
            screen_ingles.blit(fondo_ingles, (0, 0))

            #screenedFisica.blit(cronometro,(300, 5))
            #cronometro
            if segComp < 60:
                #print(f"minutos: {minutos}  segundos:{secont}  segundos Totales:{secontAnt}")

                segundosIncr = round(pygame.time.get_ticks()/1000) - secontAnt
                #print(f"incre: {segundosIncr} = ahora:{round(pygame.time.get_ticks()/1000)}  menos:{secontAnt}")

                sgTotalAnt = round(pygame.time.get_ticks()/1000)
                segundos = segundosIncr + secont
                #print(f"seg:{segundos}  incre:{segundosIncr} + secont:{secont}")
                segComp = secont + segundosIncr
                if segundos == 60:
                   minxseg = minxseg + 1
            else:
                tiempo = round(pygame.time.get_ticks() / 1000)

                segundos = (round(tiempo) + (minxseg*60)) - sgTotalAnt
                #print(f"segundos:{segundos} S")



            if segundos == 60 and c == False:
                #print(f"60:{minutos} ENTRA")
                minutos +=1
                c = True
            if segundos == 120 and j == False:
                #print(f"120:{segundos} ENTRA")
                minutos +=1
                j = True
            if segundos == 180 and p == False:
                #print(f"180:{minutos} ENTRA")
                minutos +=1
                p = True
            if segundos == 240 and f == False:
                minutos +=1
                f = True
            if segundos == 300 and ultimo == False:
                minutos +=1
                ultimo = True


            if segundos > 239:
                segundos = segundos-60
                colortemp = 255, 0, 0
            if segundos > 179: segundos = segundos - 60
            if segundos > 119: segundos = segundos - 60
            if segundos > 59: segundos = segundos-60


            if inc == True:
                per = personaje.Personaje()
                per.crear(screen_ingles, (x, y))
                llave1 = botones.Pistallave(llaveImg, llaveEncontrada)
                llave2 = botones.Pistallave(llaveImg, llaveEncontrada)
                llave3 = botones.Pistallave(llaveImg, llaveEncontrada)

                inc = False
            else:
               per.crear(screen_ingles, (x,y))

            if ll1 == False:
                llave1.crearllave(screen_ingles, (480, 540))
            else:
                llave1.found(screen_ingles)

            if ll2 == False:
                llave2.crearllave(screen_ingles, (500, 250))
            else:
                llave2.found(screen_ingles)

            if ll3 == False:
                llave3.crearllave(screen_ingles, (740, 470))
            else:
                llave3.found(screen_ingles)



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYUP:
                    per.parar(event, seguir)
                # print(f"{seguir} primero")
                if event.type == pygame.KEYDOWN or any(seguir):
                    #   print(f"{seguir} segundo")
                    if hasattr(event, 'key'):
                        if i > 2:
                            i = 0
                        seguir = per.mover(event, screen_ingles, i, seguir)
                        i = i + 1
                        if event.key == pygame.K_f:
                            persRec = per.obtener()
                            if ll1 == False: ll1 = llave1.esllave(screen_ingles, persRec)
                            if ll2 == False: ll2 = llave2.esllave(screen_ingles, persRec)
                            if ll3 == False: ll3 = llave3.esllave(screen_ingles, persRec)

            x, y = per.obtPosisiones()
            reloj1.tick(60)

            if segundos > 299 :
                cronometro = fuente.render(f" Tiempo 5:00", 0, (colortemp))
                screen_ingles.blit(cronometro, (20, 5))
                gameover(screen_ingles)
                return True, False, False, 3, 0, 0, 0
                # devolver true para inicio y crear in while edFisica = Inicio(reloj1, menu, edFisica, matematica)
            else:
                cronometro = fuente.render(f" Tiempo {minutos}:{segundos}", 0, (colortemp))
                screen_ingles.blit(cronometro, (20, 5))

            llaves = (ll1, ll2, ll3)


            if all(llaves) == True:
                menu = None
                esta =None
                sigue = None
                menu, esta, sigue, vidasactivas = comprobarPregunta("El verb to be es : are is ¿Y?", "am", vidasactivas, screen_ingles)
                if sigue == True:
                    # avanza de nivel
                    tiempo = round(pygame.time.get_ticks() / 1000)
                    #print(f"minutos: {minutos}  segundos:{segundos}  segundos Totales:{tiempo}")
                    return (False, False, True, vidasactivas, minutos, segundos, tiempo)
                    #return (False, False, True, vidasactivas)
                if menu == True:
                    return (True, False, False, 3, 0, 0, 0)

            if vidasactivas == 3:
                screen_ingles.blit(vidaActivada, (690, 0))
                screen_ingles.blit(vidaActivada, (790, 0))
                screen_ingles.blit(vidaActivada, (890, 0))
            elif vidasactivas == 2:
                screen_ingles.blit(vidaActivada, (690, 0))
                screen_ingles.blit(vidaActivada, (790, 0))
                screen_ingles.blit(vidaDesactivada, (890, 0))
            elif vidasactivas == 1:
                screen_ingles.blit(vidaActivada, (690, 0))
                screen_ingles.blit(vidaDesactivada, (790, 0))
                screen_ingles.blit(vidaDesactivada, (890, 0))

            pygame.display.update()

def salonHistoria(historia, vidaActivada, vidaDesactivada, minutos, secont, secontAnt, reloj1, fuente,vidasactivas):
    if historia == True:
        screen_historia = pygame.display.set_mode((1000, 700))
        fondo_historia = pygame.image.load('pixeles\salones\historia.png')
        llaveImg = pygame.image.load('pixeles\otones\llave.png')
        llaveEncontrada = pygame.image.load('pixeles\otones\llaveEncontrada.png')
        pygame.display.set_caption(" Nivel: Intermedio Historia")
        inc=True
        x= 60
        y=200
        i=0
        colortemp = 255, 255, 255
        inc2 = False
        rtafinal = None
        ultimaTecla = None
        contsegundos = 0
        c, j, p, f, ultimo = False, False, False, False, False
        ll1 = False
        ll2 = False
        ll3 = False
        llaves = False, False, False
        minxseg = minutos
        sgTotalAnt = 0
        segComp = secont
        sigueDerecha, sigueIzquierda, sigueFrente, sigueEspalda = False, False, False, False
        seguir = sigueDerecha, sigueIzquierda, sigueFrente, sigueEspalda

        while historia == True:
            screen_historia.fill((0, 0, 0))
            screen_historia.blit(fondo_historia, (0, 0))


            #cronometro
            if segComp < 60:
                print(f"minutos: {minutos}  segundos:{secont}  segundos Totales:{secontAnt}")

                segundosIncr = round(pygame.time.get_ticks()/1000) - secontAnt
                #print(f"incre: {segundosIncr} = ahora:{round(pygame.time.get_ticks()/1000)}  menos:{secontAnt}")

                sgTotalAnt = round(pygame.time.get_ticks()/1000)
                segundos = segundosIncr + secont
                #print(f"seg:{segundos}  incre:{segundosIncr} + secont:{secont}")
                segComp = secont + segundosIncr
                if segundos == 60:
                   minxseg = minxseg + 1
            else:
                tiempo = round(pygame.time.get_ticks() / 1000)

                segundos = (round(tiempo) + (minxseg*60)) - sgTotalAnt
                #print(f"segundos:{segundos} S")


           # print(segundos)
            if segundos == 60 and c == False:
                minutos +=1
                c = True
            if segundos == 120 and j == False:
                minutos +=1
                j = True
            if segundos == 180 and p == False:
                minutos +=1
                p = True
            if segundos == 240 and f == False:
                minutos +=1
                f = True
            if segundos == 300 and ultimo == False:
                minutos +=1
                ultimo = True

            if segundos > 59 : contsegundos = contsegundos-60
            if segundos > 119 : contsegundos = contsegundos-60
            if segundos > 179 : contsegundos = contsegundos-60
            if segundos > 239 :
                contsegundos = contsegundos-60
                colortemp = 255,0,0

            if segundos > 299 : contsegundos = contsegundos-60


            if inc == True:
                per = personaje.Personaje()
                per.crear(screen_historia, (x, y))
                llave1 = botones.Pistallave(llaveImg, llaveEncontrada)
                llave2 = botones.Pistallave(llaveImg, llaveEncontrada)
                llave3 = botones.Pistallave(llaveImg, llaveEncontrada)

                inc = False
            else:
               per.crear(screen_historia, (x,y))

            if ll1 == False:
                llave1.crearllave(screen_historia, (700, 380))
            else:
                llave1.found(screen_historia)

            if ll2 == False:
                llave2.crearllave(screen_historia, (760, 190))
            else:
                llave2.found(screen_historia)

            if ll3 == False:
                llave3.crearllave(screen_historia, (130, 420))
            else:
                llave3.found(screen_historia)



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYUP:
                    per.parar(event, seguir)
                #print(f"{seguir} primero")
                if event.type == pygame.KEYDOWN or any(seguir):
                 #   print(f"{seguir} segundo")
                    if hasattr(event, 'key'):
                        if i > 2:
                            i = 0
                        seguir = per.mover(event, screen_historia, i, seguir)
                        i = i+1
                        if event.key == pygame.K_f:
                            persRec = per.obtener()
                            if ll1 == False: ll1 = llave1.esllave(screen_historia, persRec)
                            if ll2 == False: ll2 = llave2.esllave(screen_historia, persRec)
                            if ll3 == False: ll3 = llave3.esllave(screen_historia, persRec)

            x, y = per.obtPosisiones()
            reloj1.tick(60)

            if segundos > 299 :
                cronometro = fuente.render(f" Tiempo 5:00", 0, (colortemp))
                screen_historia.blit(cronometro, (20, 5))
                gameover(screen_historia)
                return True, False, False, 3, 0, 0, 0
                # devolver true para inicio y crear in while edFisica = Inicio(reloj1, menu, edFisica, matematica)
            else:
                cronometro = fuente.render(f" Tiempo {minutos}:{segundos}", 0, (colortemp))
                screen_historia.blit(cronometro, (20, 5))

            llaves = (ll1, ll2, ll3)

            if all(llaves) == True:
                menu = None
                esta = None
                sigue = None
                menu, esta, sigue, vidasactivas = comprobarPregunta("En que año fue la revoucion de mayo", "1810", vidasactivas, screen_historia)
                if sigue == True:
                    # avanza de nivel
                    tiempo = round(pygame.time.get_ticks() / 1000)
                    #print(f"minutos: {minutos}  segundos:{segundos}  segundos Totales:{tiempo}")
                    return (False, False, True, vidasactivas, minutos, segundos, tiempo)
                    #return (False, False, True, vidasactivas, )
                if menu == True:
                    return (True, False, False, 3, 0, 0, 0)


            # vidas
            if vidasactivas == 3:
                screen_historia.blit(vidaActivada, (690, 0))
                screen_historia.blit(vidaActivada, (790, 0))
                screen_historia.blit(vidaActivada, (890, 0))
            elif vidasactivas == 2:
                screen_historia.blit(vidaActivada, (690, 0))
                screen_historia.blit(vidaActivada, (790, 0))
                screen_historia.blit(vidaDesactivada, (890, 0))
            elif vidasactivas == 1:
                screen_historia.blit(vidaActivada, (690, 0))
                screen_historia.blit(vidaDesactivada, (790, 0))
                screen_historia.blit(vidaDesactivada, (890, 0))

            # Actualiza la pantalla
            pygame.display.update()


def salon_matematica(matematica, vidaActivada, vidaDesactivada, minutos, secont, secontAnt, reloj1, fuente,vidasactivas):
    if matematica == True:
        print(vidasactivas)
        screen_matematica = pygame.display.set_mode((1000, 700))
        fondo_matematica = pygame.image.load('pixeles\salones\matematica.png')
        llaveImg = pygame.image.load('pixeles\otones\llave.png')
        llaveEncontrada = pygame.image.load('pixeles\otones\llaveEncontrada.png')
        pygame.display.set_caption(" Nivel: Intermedio Matematica")
        inc = True
        x = 490
        y = 310
        i = 0
        colortemp = 255, 255, 255
        inc2 = False
        rtafinal = None
        ultimaTecla = None
        contsegundos = 0
        c, j, p, f, ultimo = False, False, False, False, False
        ll1 = False
        ll2 = False
        ll3 = False
        llaves = False, False, False
        minxseg = minutos
        sgTotalAnt = 0
        segComp = secont
        sigueDerecha, sigueIzquierda, sigueFrente, sigueEspalda = False, False, False, False
        seguir = sigueDerecha, sigueIzquierda, sigueFrente, sigueEspalda

        while matematica == True:
            screen_matematica.fill((0, 0, 0))
            screen_matematica.blit(fondo_matematica, (0, 0))

            # screenedFisica.blit(cronometro,(300, 5))
            # cronometro
            if segComp < 60:
                #print(f"minutos: {minutos}  segundos:{secont}  segundos Totales:{secontAnt}")

                segundosIncr = round(pygame.time.get_ticks()/1000) - secontAnt
                #print(f"incre: {segundosIncr} = ahora:{round(pygame.time.get_ticks()/1000)}  menos:{secontAnt}")

                sgTotalAnt = round(pygame.time.get_ticks()/1000)
                segundos = segundosIncr + secont
                #print(f"seg:{segundos}  incre:{segundosIncr} + secont:{secont}")
                segComp = secont + segundosIncr
                if segundos == 60:
                   minxseg = minxseg + 1
            else:
                tiempo = round(pygame.time.get_ticks() / 1000)

                segundos = (round(tiempo) + (minxseg*60)) - sgTotalAnt
                #print(f"segundos:{segundos} S")



            if segundos == 60 and c == False:
                minutos += 1
                c = True
            if segundos == 120 and j == False:
                minutos += 1
                j = True
            if segundos == 180 and p == False:
                minutos += 1
                p = True
            if segundos == 240 and f == False:
                minutos += 1
                f = True
            if segundos == 300 and ultimo == False:
                minutos += 1
                ultimo = True

            if segundos > 59: contsegundos = contsegundos - 60
            if segundos > 119: contsegundos = contsegundos - 60
            if segundos > 179: contsegundos = contsegundos - 60
            if segundos > 239:
                contsegundos = contsegundos - 60
                colortemp = 255, 0, 0

            if segundos > 299: contsegundos = contsegundos - 60

            if inc == True:
                per = personaje.Personaje()
                per.crear(screen_matematica, (x, y))
                llave1 = botones.Pistallave(llaveImg, llaveEncontrada)
                llave2 = botones.Pistallave(llaveImg, llaveEncontrada)
                llave3 = botones.Pistallave(llaveImg, llaveEncontrada)

                inc = False
            else:
                per.crear(screen_matematica, (x, y))

            if ll1 == False:
                llave1.crearllave(screen_matematica, (340, 240))
            else:
                llave1.found(screen_matematica)

            if ll2 == False:
                llave2.crearllave(screen_matematica, (790, 460))
            else:
                llave2.found(screen_matematica)

            if ll3 == False:
                llave3.crearllave(screen_matematica, (410, 600))
            else:
                llave3.found(screen_matematica)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYUP:
                    per.parar(event, seguir)
                #print(f"{seguir} primero")
                if event.type == pygame.KEYDOWN or any(seguir):
                 #   print(f"{seguir} segundo")
                    if hasattr(event, 'key'):
                        if i > 2:
                            i = 0
                        seguir = per.mover(event, screen_matematica, i, seguir)
                        i = i+1
                        if event.key == pygame.K_f:
                            persRec = per.obtener()
                            if ll1 == False: ll1 = llave1.esllave(screen_matematica, persRec)
                            if ll2 == False: ll2 = llave2.esllave(screen_matematica, persRec)
                            if ll3 == False: ll3 = llave3.esllave(screen_matematica, persRec)

            x, y = per.obtPosisiones()
            reloj1.tick(60)

            if segundos > 299:
                cronometro = fuente.render(f" Tiempo 5:00", 0, (colortemp))
                screen_matematica.blit(cronometro, (20, 5))
                gameover(screen_matematica)
                return False, False, False, 3, 0, 0, 0
                # devolver true para inicio y crear in while edFisica = Inicio(reloj1, menu, edFisica, matematica)
            else:
                cronometro = fuente.render(f" Tiempo {minutos}:{segundos}", 0, (colortemp))
                screen_matematica.blit(cronometro, (20, 5))

            llaves = (ll1, ll2, ll3)

            if all(llaves) == True:
                menu = None
                esta = None
                sigue = None
                menu, esta, sigue, vidasactivas = comprobarPregunta("En que año fue la revoucion de mayo", "1810", vidasactivas, screen_matematica)
                if sigue == True:
                    # avanza de nivel
                    tiempo = round(pygame.time.get_ticks() / 1000)
                    #print(f"minutos: {minutos}  segundos:{segundos}  segundos Totales:{tiempo}")
                    return (False, False, False, vidasactivas, minutos, segundos, tiempo)
                    #return (False, False, False, vidasactivas)
                if menu == True:
                    return (True, False, False, 3, 0, 0, 0)

            # vidas
            if vidasactivas == 3:
                screen_matematica.blit(vidaActivada, (690, 0))
                screen_matematica.blit(vidaActivada, (790, 0))
                screen_matematica.blit(vidaActivada, (890, 0))
            elif vidasactivas == 2:
                screen_matematica.blit(vidaActivada, (690, 0))
                screen_matematica.blit(vidaActivada, (790, 0))
                screen_matematica.blit(vidaDesactivada, (890, 0))
            elif vidasactivas == 1:
                screen_matematica.blit(vidaActivada, (690, 0))
                screen_matematica.blit(vidaDesactivada, (790, 0))
                screen_matematica.blit(vidaDesactivada, (890, 0))

            # Actualiza la pantalla
            pygame.display.update()
