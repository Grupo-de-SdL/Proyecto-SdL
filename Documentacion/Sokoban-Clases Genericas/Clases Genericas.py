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

def nivel_1(imFondo, imPared, imZona,imCaja,imJugador):

    f1 = Fondo(imFondo, 0, 0)

    p1 = Pared(imPared, 152, 192)
    p2 = Pared(imPared, 152, 240)
    p3 = Pared(imPared, 152, 288)
    p4 = Pared(imPared, 200, 192)
    p5 = Pared(imPared, 200, 288)
    p6 = Pared(imPared, 248, 144)
    p7 = Pared(imPared, 248, 192)
    p8 = Pared(imPared, 248, 288)
    p9 = Pared(imPared, 296, 144)
    p10 = Pared(imPared, 296, 288)
    p11 = Pared(imPared, 344, 144)
    p12 = Pared(imPared, 344, 240)
    p13 = Pared(imPared, 344, 288)
    p14 = Pared(imPared, 392, 144)
    p15 = Pared(imPared, 392, 240)
    p16 = Pared(imPared, 440, 144)
    p17 = Pared(imPared, 440, 192)
    p18 = Pared(imPared, 440, 240)

    z1 = Zona_Apoyo(imZona, 200, 240)
    z2 = Zona_Apoyo(imZona, 392, 192)

    c1 = Caja(imCaja, 248, 240)
    c2 = Caja(imCaja, 344, 192)

    j1 = Jugador(imJugador, 296, 240)

    fondo = f1
    paredes = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18]
    zonas = [z1, z2]
    cajas = [c1, c2]
    jugador = j1

    return fondo, paredes, zonas, cajas, jugador

def nivel_2(imFondo, imPared, imZona, imCaja, imJugador):

    f1 = Fondo(imFondo, 0, 0)

    p1 = Pared(imPared, 104, 0)
    p2 = Pared(imPared, 104, 48)
    p3 = Pared(imPared, 104, 96)
    p4 = Pared(imPared, 104, 144)
    p5 = Pared(imPared, 104, 192)
    p6 = Pared(imPared, 152, 0)
    p7 = Pared(imPared, 152, 192)
    p8 = Pared(imPared, 152, 240)
    p9 = Pared(imPared, 152, 288)
    p10 = Pared(imPared, 152, 336)
    p11 = Pared(imPared, 152, 384)
    p12 = Pared(imPared, 200, 0)
    p13 = Pared(imPared, 200, 192)
    p14 = Pared(imPared, 200, 240)
    p15 = Pared(imPared, 200, 384)
    p16 = Pared(imPared, 248, 0)
    p17 = Pared(imPared, 248, 384)
    p18 = Pared(imPared, 296, 0)
    p19 = Pared(imPared, 296, 48)
    p20 = Pared(imPared, 296, 96)
    p21 = Pared(imPared, 296, 144)
    p22 = Pared(imPared, 296, 192)
    p23 = Pared(imPared, 296, 384)
    p24 = Pared(imPared, 344, 144)
    p25 = Pared(imPared, 344, 192)
    p26 = Pared(imPared, 344, 288)
    p27 = Pared(imPared, 344, 336)
    p28 = Pared(imPared, 344, 384)
    p29 = Pared(imPared, 392, 96)
    p30 = Pared(imPared, 392, 144)
    p31 = Pared(imPared, 392, 192)
    p32 = Pared(imPared, 392, 336)
    p33 = Pared(imPared, 440, 96)
    p34 = Pared(imPared, 440, 336)
    p35 = Pared(imPared, 488, 96)
    p36 = Pared(imPared, 488, 144)
    p37 = Pared(imPared, 488, 192)
    p38 = Pared(imPared, 488, 240)
    p39 = Pared(imPared, 488, 288)
    p40 = Pared(imPared, 488, 336)

    z1 = Zona_Apoyo(imZona, 440, 144)
    z2 = Zona_Apoyo(imZona, 440, 192)
    z3 = Zona_Apoyo(imZona, 440, 240)

    c1 = Caja(imCaja, 200, 96)
    c2 = Caja(imCaja, 200, 144)
    c3 = Caja(imCaja, 248, 96)

    j1 = Jugador(imJugador, 152, 48)

    fondo = f1
    paredes = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, p31, p32, p33, p34, p35, p36, p37, p38, p39, p40]
    zonas = [z1, z2, z3]
    cajas = [c1, c2, c3]
    jugador = j1

    return fondo, paredes, zonas, cajas, jugador

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

    def ocupada(self, cosa):
        if cosa.rect.left == self.rect.left and cosa.rect.top == self.rect.top:
            if isinstance(cosa, Jugador):
                self.estado = False
            elif isinstance(cosa, Caja):
                self.estado = True

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

class Jugador(Rectangulo_Generico):

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

class Fondo(Rectangulo_Generico):
    pass
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

#Inicializacion de cosas

    for juego in range(1, 3):#Requiere de un "range" de x+1, donde x es el numero de nivele implementados
        if juego == 1:
            fondo, paredes, zonas, cajas, jugador = nivel_1('fondo_generico.png', 'Pared.png', 'Zona.png', 'Caja.png', 'Jugador.png')
        if juego == 2:
            fondo, paredes, zonas, cajas, jugador = nivel_2('fondo_generico.png', 'Pared.png', 'Zona.png', 'Caja.png', 'Jugador.png')

        fondo_render = pygame.sprite.RenderPlain((fondo))
        paredes_render = pygame.sprite.RenderPlain((paredes))
        zonas_render = pygame.sprite.RenderPlain((zonas))
        cajas_render = pygame.sprite.RenderPlain((cajas))
        jugador_render = pygame.sprite.RenderPlain((jugador))

        bandera = 0
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
                    jugador.moverse(event)

                    for k in range(len(cajas)):
                        cajas[k].mover(event, jugador)
                        for l in range(len(cajas)):
                            if k != l:
                                cajas[k].chocada(event, cajas[l], jugador) # Cajas que rebotan en cajas

                    for i in range(len(paredes)):
                        paredes[i].chocada(event, jugador) # Juagador rebota en paredes
                        for j in range(len(cajas)):
                            paredes[i].chocada(event, cajas[j], jugador) # Cajas rebotan en paredes

                    for m in range(len(zonas)):
                        for n in range(len(cajas)):
                            zonas[m].ocupada(jugador)
                            zonas[m].ocupada(cajas[n])

                    bandera = 0
                    for r in range(len(zonas)): # Si todas las zonas tienen una caja ensima se cambia el valor de bandera
                        if zonas[r].estado:
                            bandera += 1

                    if bandera == len(zonas):# Si bandera esta en True se reinicia la posicion del jugador
                        going = False

            fondo_render.draw(screen)
            paredes_render.draw(screen)
            zonas_render.draw(screen)
            cajas_render.draw(screen)
            jugador_render.draw(screen)

            pygame.display.update()

    pygame.quit()

#esta llama al main
if __name__ == '__main__':
    main()