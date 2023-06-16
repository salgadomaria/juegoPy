import pygame

pygame.init()

class Buttonimg():
    def __init__(self,image, holdImg ,pos):
        self.image = image
        self.holdImg = holdImg
        #self.imgCmb = image
        self.x_pos= pos[0]
        self.y_pos = pos[1]
        self.rect=self.image.get_rect(center=(self.x_pos, self.y_pos))

    def crearbtn(self, ventana):
        ventana.blit(self.image, self.rect)
    #le pasamos la ubicacion del mouse si hizo click
    def sobreBtn(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
    #le pasamos la ubiacion del mouse y comprobamos si esta sobre el boton
    def cambioImg (self, position, ventana):
        if position[0] in range(self.rect.left,self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            #si la posision del mouse actual esta en el rango de la posision actual del boton la imagen cambia
            ventana.blit(self.holdImg, self.rect)
        else:
            ventana.blit(self.image, self.rect)


class Pistallave():

    def __init__(self,image ,encontrada):
        self.image = image
        self.encontrada = encontrada
        self.rect=self.image.get_rect()

    def crearllave(self, ventana, posiciones):
        self.rect.top, self.rect.left = (posiciones[1], posiciones[0])
        ventana.blit(self.image, self.rect)


    def esllave (self, ventana,persRec):
        pygame.init()

        if self.rect.colliderect(persRec):
            #si la posision del mouse actual esta en el rango de la posision actual del boton la imagen cambia
            ventana.blit(self.encontrada, self.rect)
            return True
        else:
            ventana.blit(self.image, self.rect)
            return False

    def found(self, ventana):
        ventana.blit(self.encontrada, self.rect)



class Buttontxt():
    def __init__(self,image,pos,text_input,font, base_color, hovering_color):
        self.image = image
        self.x_pos= pos[0]
        self.y_pos = pos[1]
        self.font=font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = self.text_input
        self.text = self.font.render(self.text_input,True,self.base_color)
        if self.image is None:
            self.image=self.text
        self.rect=self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, ventana):
        if self.image is not None:
            ventana.blit(self.image, self.rect)
        ventana.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right)and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
    def cambioColor (self, position):
        if position[0] in range(self.rect.left,self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_inut, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)



