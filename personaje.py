import pygame,sys

pygame.init()

class Personaje(pygame.sprite.Sprite):


    def __int__(self):
        self

    derechaPieD = pygame.image.load('derechoderecho.png')
    derechaPieI = pygame.image.load('derechoizquierdo.png')
    derecha = pygame.image.load('pixeles\personaje\parado\derecha.png')
    ladoDerecho = [derechaPieD, derecha, derechaPieI]

    izquiquierdaPieD = pygame.image.load("pixeles\personaje\caminando\izquierdaderecho.png")
    izquiquierdaPieI = pygame.image.load("pixeles\personaje\caminando\izquierdaIzquierdo.png")
    izquierda = pygame.image.load("pixeles\personaje\parado\izquierda.png")
    ladoIzquierdo = [izquiquierdaPieD, izquierda, izquiquierdaPieI]

    frentePieD = pygame.image.load('pixeles\personaje\caminando\dfrentepiederecho.png')
    frentePieI = pygame.image.load('pixeles\personaje\caminando\dfrentepieizquierdo.png')
    frente = pygame.image.load("pixeles\personaje\parado\dfrente.png")
    deFrente = [frentePieD, frente, frentePieI]

    esaldaPieD = pygame.image.load('pixeles\personaje\caminando\espaldaderecho.png')
    esaldaPieI = pygame.image.load('pixeles\personaje\caminando\espaldaizquierda.png')
    espalda = pygame.image.load('pixeles\personaje\parado\espalda.png')
    deEspalda = [esaldaPieD, espalda, esaldaPieI]

    actual = 0
    imagen = frente
    rect = imagen.get_rect()
    a,s,d,w =0,0,0,0

    def crear(self,superficie,posiciones):
        self.rect.top, self.rect.left = (posiciones[1], posiciones[0])
        superficie.blit(self.imagen, self.rect)

    def obtPosisiones(self):
            return self.rect.left, self.rect.top

    def obtener(self):
        return self.rect
    def mover(self, event, superficie, i,seguir):

        sigueDerecha, sigueIzquierda, sigueFrente, sigueEspalda = seguir

        if event.key == pygame.K_a: #or sigueIzquierda == True:
            sigueIzquierda = True
            seguir = sigueDerecha, sigueIzquierda, sigueFrente, sigueEspalda
            self.imagen = self.ladoIzquierdo[i]

            self.rect.move_ip(-10, 0)
            superficie.blit(self.imagen, self.rect)

            return seguir
        elif event.key == pygame.K_s: #or sigueFrente == True:
            sigueFrente = True
            seguir = sigueDerecha, sigueIzquierda, sigueFrente, sigueEspalda
            self.imagen = self.deFrente[i]

            self.rect.move_ip(0, 10)
            superficie.blit(self.imagen, self.rect)

            return seguir
        elif event.key == pygame.K_d:# or sigueDerecha == True:
            sigueDerecha = True
            seguir = sigueDerecha, sigueIzquierda, sigueFrente, sigueEspalda
            self.imagen = self.ladoDerecho[i]
            self.rect.move_ip(10, 0)
            superficie.blit(self.imagen, self.rect)
            return seguir
        elif event.key == pygame.K_w:# or sigueEspalda == True:
            sigueEspalda = True
            seguir = sigueDerecha, sigueIzquierda, sigueFrente, sigueEspalda

            self.imagen = self.deEspalda[i]

            self.rect.move_ip(0, -10)
            superficie.blit(self.imagen, self.rect)

            return seguir
        else:
            seguir = False, False, False, False
            return seguir

    def parar(self, event, seguir):

        sigueDerecha, sigueIzquierda, sigueFrente, sigueEspalda = seguir

        if event.key == pygame.K_a:
            sigueIzquierda == False
            seguir = sigueDerecha, sigueIzquierda, sigueFrente, sigueEspalda
            return seguir
        elif event.key == pygame.K_s:
            sigueFrente == False
            seguir = sigueDerecha, sigueIzquierda, sigueFrente, sigueEspalda
            return seguir
        elif event.key == pygame.K_d:
            sigueDerecha == False
            seguir = sigueDerecha, sigueIzquierda, sigueFrente, sigueEspalda
            return seguir
        elif event.key == pygame.K_w:
            sigueEspalda == False
            seguir = sigueDerecha, sigueIzquierda, sigueFrente, sigueEspalda
            return seguir
        else:
            seguir = False, False, False, False
            return seguir