#!/usr/bin/env python

#modulos a importar

import os, pygame
from pygame.locals import *
from pygame.compat import geterror

if not pygame.font: print ('Warning, fonts disabled')
if not pygame.mixer: print ('Warning, sound disabled')

#funciones

main_dir = os.path.split(os.path.abspath(__file__))[0]
images_dir = os.path.join(main_dir, 'images')
sound_dir = os.path.join(main_dir, 'sound')

def load_image(name, colorkey=None):
    fullname = os.path.join(images_dir, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print ('Cannot load image:', fullname)
        raise SystemExit(str(geterror()))
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

def load_sound(name):
    class NoneSound:
        def play(self):
            pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    fullname = os.path.join(sound_dir, name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error:
        print ('Cannot load sound: %s' % fullname)
        raise SystemExit(str(geterror()))
    return sound

def bk(screen):
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
    return background

#funciones

#Clases

class Rectangulo_Generico(pygame.sprite.Sprite):

    def __init__(self, imagen, posX, posY):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(imagen, -1)
        self.rect.left = posX
        self.rect.top = posY
        self.estado = False

    def update(self,superficie):
        superficie.blit(self.image, self.rect)

class Pared(Rectangulo_Generico):

    def chocada(self, tecla, cosa1, cosa2 = None):
        if cosa1.rect.left == self.rect.left and cosa1.rect.top == self.rect.top:
            if isinstance(cosa1, Jugador):
                cosa1.rebotar(tecla)
            elif isinstance(cosa1, Caja):
                cosa1.rebotar(tecla)
                cosa2.rebotar(tecla)


class Zona_Apoyo(Rectangulo_Generico):

    def setEstado(self, est):
         self.estado = est

class Caja(Rectangulo_Generico):

    def mover(self, tecla, jugador):
        if jugador.rect.left == self.rect.left and jugador.rect.top == self.rect.top:
            if tecla.key == K_UP:
                self.rect.move_ip(0, -48)
            elif tecla.key == K_DOWN:
                self.rect.move_ip(0, 48)
            elif tecla.key == K_LEFT:
                self.rect.move_ip(-48, 0)
            elif tecla.key == K_RIGHT:
                self.rect.move_ip(48, 0)

    def rebotar(self, tecla):

            if tecla.key == K_UP:
                self.rect.move_ip(0, 48)
            elif tecla.key == K_DOWN:
                self.rect.move_ip(0, -48)
            elif tecla.key == K_LEFT:
                self.rect.move_ip(48, 0)
            elif tecla.key == K_RIGHT:
                self.rect.move_ip(-48, 0)

    def chocada(self, tecla, caja, jugador):
        if caja.rect.left == self.rect.left and caja.rect.top == self.rect.top:
            caja.rebotar(tecla)
            jugador.rebotar(tecla)

    def pociocionada(self, zona):
        for i in range(len(zona)):

            if zona[i].rect.left == self.rect.left and zona[i].rect.top == self.rect.top:
                zona[i].setEstado(True)
            else: zona[i].setEstado(False)

class Jugador(Rectangulo_Generico):

#moverse
    def moverse(self, tecla):

        if tecla.key == K_UP:
            self.rect.move_ip(0, -48)
        elif tecla.key == K_DOWN:
            self.rect.move_ip(0, 48)
        elif tecla.key == K_LEFT:
            self.rect.move_ip(-48, 0)
        elif tecla.key == K_RIGHT:
            self.rect.move_ip(48, 0)

    def rebotar(self, tecla):

        if tecla.key == K_UP:
            self.rect.move_ip(0, 48)
        elif tecla.key == K_DOWN:
            self.rect.move_ip(0, -48)
        elif tecla.key == K_LEFT:
            self.rect.move_ip(48, 0)
        elif tecla.key == K_RIGHT:
            self.rect.move_ip(-48, 0)

#Clases




#definir main<-todo corre dentro de esta
def main():

#Inicializacion de pantalla
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    background = bk(screen)

    screen.blit(background, (0, 0))
    pygame.display.flip()

#Inicializacion de pantalla

#Inicializacion de variables

#Inicializacion de variables

#Inicializacion de cosas

    p1 = Pared('Pared.png', 0, 0)
    p2 = Pared('Pared.png', 0, 48)
    p3 = Pared('Pared.png', 0, 96)
    p4 = Pared('Pared.png', 0, 144)
    p5 = Pared('Pared.png', 0, 192)
    p6 = Pared('Pared.png', 0, 240)
    p7 = Pared('Pared.png', 0, 288)
    p8 = Pared('Pared.png', 0, 336)
    p9 = Pared('Pared.png', 0, 384)
    p10 = Pared('Pared.png', 0, 432)
    p11 = Pared('Pared.png', 48, 0)
    p12 = Pared('Pared.png', 48, 432)
    p13 = Pared('Pared.png', 96, 0)
    p14 = Pared('Pared.png', 96, 432)
    p15 = Pared('Pared.png', 144, 0)
    p16 = Pared('Pared.png', 144, 432)
    p17 = Pared('Pared.png', 192, 0)
    p18 = Pared('Pared.png', 192, 432)
    p19 = Pared('Pared.png', 240, 0)
    p20 = Pared('Pared.png', 240, 432)
    p21 = Pared('Pared.png', 288, 0)
    p22 = Pared('Pared.png', 288, 432)
    p23 = Pared('Pared.png', 336, 0)
    p24 = Pared('Pared.png', 336, 432)
    p25 = Pared('Pared.png', 384, 0)
    p26 = Pared('Pared.png', 384, 432)
    p27 = Pared('Pared.png', 432, 0)
    p28 = Pared('Pared.png', 432, 432)
    p29 = Pared('Pared.png', 480, 0)
    p30 = Pared('Pared.png', 480, 432)
    p31 = Pared('Pared.png', 528, 0)
    p32 = Pared('Pared.png', 528, 432)
    p33 = Pared('Pared.png', 576, 0)
    p34 = Pared('Pared.png', 576, 48)
    p35 = Pared('Pared.png', 576, 96)
    p36 = Pared('Pared.png', 576, 144)
    p37 = Pared('Pared.png', 576, 192)
    p38 = Pared('Pared.png', 576, 240)
    p39 = Pared('Pared.png', 576, 288)
    p40 = Pared('Pared.png', 576, 336)
    p41 = Pared('Pared.png', 576, 384)
    p42 = Pared('Pared.png', 576, 432)

    z1 = Zona_Apoyo('Zona.png', 336, 192)
    z2 = Zona_Apoyo('Zona.png', 336, 240)
    z3 = Zona_Apoyo('Zona.png', 384, 192)
    z4 = Zona_Apoyo('Zona.png', 384, 240)
    c1 = Caja('Caja.png', 384, 96)
    c2 = Caja('Caja.png', 192, 144)
    c3 = Caja('Caja.png', 192, 288)
    c4 = Caja('Caja.png', 432, 288)
    j1 = Jugador('Jugador.png', 96, 240)

    paredes_render = pygame.sprite.RenderPlain((p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, p31, p32, p33, p34, p35, p36, p37, p38, p39, p40, p41, p42))
    zonas_render = pygame.sprite.RenderPlain((z1, z2, z3, z4))
    cajas_render = pygame.sprite.RenderPlain((c1, c2, c3, c4))
    jugador_render = pygame.sprite.RenderPlain((j1))

    paredes = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, p31, p32, p33, p34, p35, p36, p37, p38, p39, p40, p41, p42]
    zonas = [z1, z2, z3, z4]
    cajas = [c1, c2, c3, c4]

#Inicializacion de cosas

#Bucle principal
    going = True
    while going:
        clock.tick(60)
#Manejar eventos de salida
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                going = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                going = False
            if event.type == KEYUP:
                j1.moverse(event)

                for k in range(len(cajas)):
                    cajas[k].mover(event, j1) # Cajas movidas
                    cajas[k].pociocionada(zonas) # Ver si una caja esta en una zona. Repetir para todas las cajas
                    for l in range(len(cajas)):

                        if k != l:
                            cajas[k].chocada(event, cajas[l], j1) # Cajas que rebotan en cajas

                for i in range(len(paredes)):
                    paredes[i].chocada(event, j1) # Juagador rebota en paredes
                    for j in range(len(cajas)):
                        paredes[i].chocada(event, cajas[j], j1) # Cajas rebotan en paredes

#                for m in range(len(zonas)): # Cambiar estado de las zonas
#                    for n in range(len(cajas)):
#                        if m != n:
#                            zonas[m].setEstado(cajas[n])

                #for r in range(len(zonas)): # Si todas las zonas estan actibadas o no
                if zonas[0].estado and zonas[1].estado and zonas[2].estado and zonas[3].estado:
                    j1.rect.left = 96
                    j1.rect.top = 240

        paredes_render.draw(screen)
        zonas_render.draw(screen)
        cajas_render.draw(screen)
        jugador_render.draw(screen)

#<-toda la pantalla
        pygame.display.update()

    pygame.quit()

#esta llama al main
if __name__ == '__main__':
    main()