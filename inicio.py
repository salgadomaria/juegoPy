import pygame, sys
import time
import botones
import personaje
import salon
from botones import Buttonimg
import question
from personaje import Personaje


# Inicializa Pygame
pygame.init()

class personajeInicio(pygame.sprite.Sprite):

    def __int__(self):
        self

    derechaPieD = pygame.image.load('derechoderecho.png')
    derechaPieI = pygame.image.load('derechoizquierdo.png')
    derecha = pygame.image.load('pixeles\personaje\parado\derecha.png')
    frente = pygame.image.load("pixeles\personaje\parado\dfrente.png")
    izquierda = pygame.image.load("pixeles\personaje\parado\izquierda.png")
    imagenes = [ derechaPieD, derecha, derechaPieI]
    actual = 0
    imagen = imagenes[actual]
    rect = imagen.get_rect()
    rect.top, rect.left = (450, 0)

        #def caminar(self):
        #te dice cuanto incrementar en x , y no la posicion ecxacta

        #self.rect.move_ip(1,0)

        #if  self.rect.left > 1000:
         #   self.rect.top, self.rect.left = (450, 0)

    def crear(self,superficie,t):

        #if t == 2:
         #   self.actual +=1
        self.actual = t
        if self.actual > (len(self.imagenes)-1):
            self.actual = 0


        self.rect.move_ip(10, 0)
        if self.rect.left > 1000:
            self.rect.top, self.rect.left = (450, 0)

        self.imagen=self.imagenes[self.actual]
        superficie.blit(self.imagen, self.rect)

#ACA ESTABA GAME OVER

def Inicio( menu, edFisica):

    reloj1 = pygame.time.Clock()

    if menu == True:
        # imgBoton
        screen = pygame.display.set_mode((1000, 700))
        fondoinicio = pygame.image.load('pixeles\salones\pasillo1.jpg')
        screen.fill((0, 0, 0))
        pygame.display.set_caption("Inicio")
        tardo = 0
        btnSf = pygame.image.load('pixeles\otones\otnrojojugar.png')  # salon
        btnSf2 = pygame.image.load('pixeles\otones\jugarsincolor.png')  # salon
        # boton
        btn = Buttonimg(btnSf2, btnSf, (500, 250))
        t = 0

        # Mantenemos la ventana abierta hasta que toquemos el boton
        while menu == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if btn.sobreBtn((pygame.mouse.get_pos())):
                        menu = False
                        edFisica = True
                        return edFisica, tardo

            # for event in pygame.event.get():
            reloj1.tick(15)
            tardo = round(pygame.time.get_ticks()/1000)
            print(tardo)
            screen.blit(fondoinicio, (0, 200))
            if t > 2:
                t = 0
            p = personajeInicio()
            p.crear(screen, t)
            t += 1
            btn.crearbtn(screen)
            btn.cambioImg(pygame.mouse.get_pos(), screen)

            # Actualiza la pantalla
            pygame.display.update()


def main():

    #a, s, d, w = 0, 0, 0, 0
    reloj1 = pygame.time.Clock()
    menu = True
    edFisica = False
    ingles = False
    historia = False
    matematica = False

    #SALONES
    #vidas
    vidaActivada = pygame.image.load('pixeles\otones\corazon.png')
    vidaDesactivada = pygame.image.load('pixeles\otones\corazonsincolor.png')

    vidasactivas = 3

    #fuente
    fuente = pygame.font.SysFont("Arial Black", 40, False, False)
    minutos = 0

    #ACA ESTABA EDFISICA


    while any((menu ,edFisica,ingles,historia)) == True:
        #en algun momento presionaran el boton y edFisica sera True

        edFisica, tardo = Inicio(menu, edFisica)

        menu, edFisica, ingles, vidasactivas, minutos, segundos, secontotal = salon.Salon_ed_fisica(edFisica, vidaActivada, vidaDesactivada, minutos, reloj1, fuente, vidasactivas, tardo)
        #print(f"a main {menu}")

        if menu != True:
            menu, ingles, historia, vidasactivas, minutos, segundos, secontotal = salon.salonIngles(ingles, vidaActivada, vidaDesactivada, minutos, segundos, secontotal, reloj1, fuente, vidasactivas)
            # print(vidasactivas)
            if menu != True:
                menu, historia, matematica, vidasactivas, minutos, segundos, secontotal = salon.salonHistoria(historia, vidaActivada, vidaDesactivada, minutos, segundos, secontotal, reloj1, fuente, vidasactivas)
                # print(vidasactivas)
                if menu != True:

                    menu, matematica, edFisica, vidasactivas, minutos, segundos, secontotal = salon.salon_matematica(matematica, vidaActivada, vidaDesactivada, minutos, segundos, secontotal, reloj1, fuente, vidasactivas)
                    # print(vidasactivas)

    if all((menu ,edFisica,ingles,historia, matematica)) == False:
        pygame.init()

        # Definir el tamaño de la ventana
        window_size = (1000, 700)
        fondo = pygame.image.load('pixeles\creditos.png')
        # Crear la superficie de pantalla
        screen = pygame.display.set_mode(window_size)
        pygame.display.set_caption("Gracias por Jugar")



        # Mantener la ventana abierta hasta que el usuario la cierre
        while True:
            for event in pygame.event.get():
                screen.fill((255,255,255))
                screen.blit(fondo, (0, 0))
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()



main()