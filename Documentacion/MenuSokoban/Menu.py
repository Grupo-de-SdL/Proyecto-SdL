'''
Created on 7 de oct. de 2015

@author: Juan
'''
import pygame 
 # importo el modulo

class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def update(self):
        self.left,self.top=pygame.mouse.get_pos()
        
class Boton(pygame.sprite.Sprite):
    def __init__(self,imagen1,imagen2,x=200,y=200):
        self.imagen_normal=imagen1
        self.imagen_seleccion=imagen2
        self.imagen_actual=self.imagen_normal
        self.rect=self.imagen_actual.get_rect()
        self.rect.left,self.rect.top=(x,y)
        
    def update(self,pantalla,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual=self.imagen_seleccion
        else: self.imagen_actual=self.imagen_normal
        
        pantalla.blit(self.imagen_actual,self.rect)
         



#funcion main
def main():
    pygame.init() # inicializo el modulo
    
    # fijo las dimensiones de la pantalla a 300,300 y creo una superficie que va ser la principal
    pantalla=pygame.display.set_mode((640,480))
    
    pygame.display.set_caption("Mi Ventana") # Titulo de la Ventana
    #creo un reloj para controlar los fps
    reloj1=pygame.time.Clock()
    cursor1=Cursor()
    
    boton1a=pygame.image.load("Menu/SALIr.png")
    boton1b=pygame.image.load("Menu/SALIR2.png")
    boton2a=pygame.image.load("Menu/CREDITOS.png")
    boton2b=pygame.image.load("Menu/CREDITOS2.png")
    boton3a=pygame.image.load("Menu/jugar.png")
    boton3b=pygame.image.load("Menu/jugar2.png")
    boton4a=pygame.image.load("Menu/TITULO.png")
    boton4b=pygame.image.load("Menu/TITULO2.png")
    
    
    Boton1=Boton(boton1a,boton1b,250,350)
    Boton2=Boton(boton2a,boton2b,250,300)
    Boton3=Boton(boton3a,boton3b,250,250)
    
    
    Boton4=Boton(boton4a,boton4b,50,50)
    #
    
 
    
    
    
    
    sonido1=pygame.mixer.Sound("Menu/FIN.wav")
    sonido2=pygame.mixer.Sound("Menu/USADO.wav")
    
    
    
    
    
    #Boton2=Boton(azul1,azul2,200,200)
    #blanco=(255,255,255) # color blanco en RGB
    negro=(0,0,0)
    
    salir=False
    #LOOP PRINCIPAL
    while salir!=True:
        #recorro todos los eventos producidos
        #en realidad es una lista
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(Boton1.rect):
                    sonido2.play()
                    salir=True
                
                if cursor1.colliderect(Boton2.rect):
                    sonido2.play()
                    
                if cursor1.colliderect(Boton3.rect):
                    sonido2.play()
                if cursor1.colliderect(Boton4.rect):
                    sonido1.play()
               
                   
                   
        
        
        
            # si el evento es del tipo 
            # pygame.QUIT( cruz de la ventana)
            if event.type == pygame.QUIT:
                salir=True
        
        
        
        
        
        
        reloj1.tick(20)#operacion para que todo corra a 20fps
        pantalla.fill(negro) # pinto la superficie de blanco
        Boton1.update(pantalla,cursor1)
        Boton2.update(pantalla,cursor1)
        Boton3.update(pantalla,cursor1)
        Boton4.update(pantalla,cursor1)
        
        
        
        
        cursor1.update()
        pygame.display.update() #actualizo el display
        
    pygame.quit()
    
main() 