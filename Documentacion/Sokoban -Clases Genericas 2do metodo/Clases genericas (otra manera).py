# This Python file uses the following encoding: utf-8
import pygame

class General(pygame.sprite.Sprite): #Esta aclase abarca todos los objetos del juego
	def __init__ (self, imagen):
		self.imagen = imagen        #Todos los objetos tendran una imagen
		self.rect = self.imagen.get_rect()  #Todos los objetos tendran un rectangulo de esa imagen (para manejar las colisiones)
		self.rect.left = 0			#Todos los objetos tendran una posicion en "x" (0 por default)
		self.rect.top = 0			#Todos los objetos tendran una posicion en "y" (0 por default tambien)

	def update(self, superficie):	#Este metodo actualiza el objeto en una superficie que le pasemos como parametro
		superficie.blit(self.imagen, self.rect)

	def colisiono(self, rectanguloChoque):	#Ese metodo nos dira si objeto colisiono con otro objeto que le pasamos como parametro
		colision = False
		if (self.rect.colliderect(rectanguloChoque)):
			colision = True
		return colision

	def setImagen(self, imagen): #Metodo para setear la imagen del objeto
		self.imagen = imagen
		   
	def setearPosicionInicial(self, posInicialX, posInicialY): #Metodo para setear la posicion inicial del objeto (en "x" y en "y")
		self.rect.left = posInicialX
		self.rect.top = posInicialY

class CuadradoConMovimiento(General): #Clase especifica para ciertos objetos -> ¿Que objetos se moveran? -> El jugador y las cajas
	def __init__(self, imagen):		  #Ya que esta clase solo implementa un metodo y no atributos, los parametros que se  pasan
			General.__init__(self, imagen)	#Al momento de crear un objeto de esta clase iran al constructor de la clase padre
			self.sonidoColision = None

	def mover(self, movimientoEnX, movimientoEnY):	#Mueve el objeto tantas posiciones en "x" y tantas posiciones en "y"
		self.rect.move_ip(movimientoEnX, movimientoEnY)
		
class ZonaApoyo(General):	#Clase para las zonas de apoyo -> Las zonas de apoyo tienen algo que ningun otro elemento del juego tiene:
	def __init__(self, imagen):	#Las zonas de apoyo tienen un "estado" que es el que va a determinar si un objeto esta sobre ella o no
		General.__init__(self, imagen)	#Podemos ver que el unico parametro que recibe el constructor va para el constructor de la clase "General" como antes
		self.estado = False	#Esto es porque el unico atributo que tienen las zonas de apoyo se esta seteando por defecto y no con parametros

class Jugador(CuadradoConMovimiento): #Clase para el jugador -> ¿Que tiene el jugador que los demás objetos no? -> Una velocidad y sonidos caracteristicos cuando gana o pierde
	def __init__(self, imagen):		  #Las cajas se mueven...También podria decirse que tienen velocidad. Pero, ¿no se mueven a 
		General.__init__(self, imagen)	#la misma velocidad que el jugador? Por ende, en este caso, solo vamos a definirla en Jugador
		self.velocidad = 48
		self.hablarPerdio = None 
		self.hablarGano = None