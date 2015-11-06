# This Python file uses the following encoding: utf-8
import pygame, sys
from pygame.locals import * #importamos todos los modulos de pygame

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

#Nivel1() -> Setea las imagenes y posiciones de casi todos los elementos del nivel 1.
def nivel1(jugadorPrincipal, caja1, caja2, caja3, caja4, zona1, zona2, zona3, zona4, piso):
	#Jugador
	imagenJugadorPrincipal= pygame.image.load("NivelSimpsons/jugadorHomero.png")
	jugadorPrincipal.hablarPerdio =	pygame.mixer.Sound("NivelSimpsons/homeroDoh.wav")
	jugadorPrincipal.hablarGano = pygame.mixer.Sound("NivelSimpsons/homeroFestejo.wav")
	jugadorPrincipal.hablarPerdio.set_volume(0.05)
	jugadorPrincipal.hablarGano.set_volume(0.05)
	jugadorPrincipal.setImagen(imagenJugadorPrincipal)
	jugadorPrincipal.setearPosicionInicial(148,192)
	#Caja
	imagenCaja= pygame.image.load("NivelSimpsons/cajaSimpsons.png")
	caja1.sonidoColision = pygame.mixer.Sound("NivelSimpsons/golpeCaja.wav")
	caja2.sonidoColision = pygame.mixer.Sound("NivelSimpsons/golpeCaja.wav")
	caja3.sonidoColision = pygame.mixer.Sound("NivelSimpsons/golpeCaja.wav")
	caja4.sonidoColision = pygame.mixer.Sound("NivelSimpsons/golpeCaja.wav")
	caja1.sonidoColision.set_volume(0.05)
	caja2.sonidoColision.set_volume(0.05)
	caja3.sonidoColision.set_volume(0.05)
	caja4.sonidoColision.set_volume(0.05)
	caja1.setImagen(imagenCaja)
	caja1.setearPosicionInicial(148,144)
	caja2.setImagen(imagenCaja)
	caja2.setearPosicionInicial(244,192)
	caja3.setImagen(imagenCaja)
	caja3.setearPosicionInicial(388,192)
	caja4.setImagen(imagenCaja)
	caja4.setearPosicionInicial(340,240)
	#ZonaDeApoyo
	imagenZona = pygame.image.load("NivelSimpsons/zonaRosca.png")
	zona1.setImagen(imagenZona)
	zona1.setearPosicionInicial(148,240)
	zona2.setImagen(imagenZona)
	zona2.setearPosicionInicial(148,288)
	zona3.setImagen(imagenZona)
	zona3.setearPosicionInicial(196,240)
	zona4.setImagen(imagenZona)
	zona4.setearPosicionInicial(196,288)
	#Piso nivel -> En este nivel seguiremos usando el piso base -> solo seteamos su posicion
	piso.setearPosicionInicial(100,96)


#AdministradorNivel1() -> Administra todo el nivel uno: - Colisiones que pueden existir entre los objetos, -Controlar zonas de apoyo
def AdministradorNivel1(jugadorPrincipal, cajaAnalizar, cajaX, cajaZ, cajaY, caja_posAnterior, rect_movimientoEnX, rect_movimientoEnY, j_posAnterior, pared1, pared2, pared3, pared4, pared5, pared6, pared7, pared8, pared9, pared10, zona1, zona2, zona3, zona4):
	#Si el jugador principal choca contra algunas de las paredes
		#Vuelve a la posicion anterior antes de chocar
	if ((jugadorPrincipal.colisiono(pared1)) or (jugadorPrincipal.colisiono(pared2))):
		(jugadorPrincipal.rect.left, jugadorPrincipal.rect.top) = j_posAnterior


	if ((jugadorPrincipal.colisiono(pared3)) or (jugadorPrincipal.colisiono(pared4))):
		(jugadorPrincipal.rect.left, jugadorPrincipal.rect.top) = j_posAnterior

	if ((jugadorPrincipal.colisiono(pared5)) or (jugadorPrincipal.colisiono(pared6))):
		(jugadorPrincipal.rect.left, jugadorPrincipal.rect.top) = j_posAnterior
			

	if ((jugadorPrincipal.colisiono(pared7)) or (jugadorPrincipal.colisiono(pared8))):
		(jugadorPrincipal.rect.left, jugadorPrincipal.rect.top) = j_posAnterior

	if ((jugadorPrincipal.colisiono(pared9)) or (jugadorPrincipal.colisiono(pared10))):
		(jugadorPrincipal.rect.left, jugadorPrincipal.rect.top) = j_posAnterior	

	#Si el jugador colisiona (empuja) una caja (que va a ser la "caja_a_Analizar" -> Esto de la caja se explica más adelante)
		#Va a preguntar si la caja, a su vez, colisiona con una pared, con una zona de apoyo o con otra caja.

	if (jugadorPrincipal.colisiono(cajaAnalizar)):
				cajaAnalizar.mover(rect_movimientoEnX, rect_movimientoEnY)
				if ((cajaAnalizar.colisiono(pared1)) or (cajaAnalizar.colisiono(pared2)) or (cajaAnalizar.colisiono(pared3)) or (cajaAnalizar.colisiono(pared4))):
					cajaAnalizar.sonidoColision.play()
					(cajaAnalizar.rect.left, cajaAnalizar.rect.top) = caja_posAnterior
					(jugadorPrincipal.rect.left, jugadorPrincipal.rect.top) = j_posAnterior

				if ((cajaAnalizar.colisiono(pared5)) or (cajaAnalizar.colisiono(pared6)) or (cajaAnalizar.colisiono(pared7))):
					cajaAnalizar.sonidoColision.play()
					(cajaAnalizar.rect.left, cajaAnalizar.rect.top) = caja_posAnterior
					(jugadorPrincipal.rect.left, jugadorPrincipal.rect.top) = j_posAnterior

				if ((cajaAnalizar.colisiono(pared8)) or (cajaAnalizar.colisiono(pared9)) or (cajaAnalizar.colisiono(pared10))):
					cajaAnalizar.sonidoColision.play()
					(cajaAnalizar.rect.left, cajaAnalizar.rect.top) = caja_posAnterior
					(jugadorPrincipal.rect.left, jugadorPrincipal.rect.top) = j_posAnterior

				if ((cajaAnalizar.colisiono(cajaX)) or (cajaAnalizar.colisiono(cajaY)) or (cajaAnalizar.colisiono(cajaZ))):
					cajaAnalizar.sonidoColision.play()
					(cajaAnalizar.rect.left, cajaAnalizar.rect.top) = caja_posAnterior
					(jugadorPrincipal.rect.left, jugadorPrincipal.rect.top) = j_posAnterior

				#Si alguna de las cajas (incluida la caja de los if anteriores) esta apoyada sobre una zona de apoyo:
					#El estado de esta es "True"
					#De lo contrario -> Es "False"

				if ((cajaAnalizar.colisiono(zona1)) or (cajaX.colisiono(zona1)) or (cajaY.colisiono(zona1)) or (cajaZ.colisiono(zona1))):
 					zona1.estado = True
 				else:
 					zona1.estado = False

 				if ((cajaAnalizar.colisiono(zona2)) or (cajaX.colisiono(zona2)) or (cajaY.colisiono(zona2)) or (cajaZ.colisiono(zona2))):
 					zona2.estado = True
 				else:
 					zona2.estado = False

 				if ((cajaAnalizar.colisiono(zona3)) or (cajaX.colisiono(zona3)) or (cajaY.colisiono(zona3)) or (cajaZ.colisiono(zona3))):
 					zona3.estado = True
 				else:
 					zona3.estado = False

 				if ((cajaAnalizar.colisiono(zona4)) or (cajaX.colisiono(zona4)) or (cajaY.colisiono(zona4)) or (cajaZ.colisiono(zona4))):
 					zona4.estado = True

 				else:
 					zona4.estado = False

 				#Si todas las zonas estan en "True" -> El jugador ya gano el nivel
 				if ((zona1.estado == True) and (zona2.estado == True) and (zona3.estado == True) and (zona4.estado == True)):
 					jugadorPrincipal.hablarGano.play()
 					jugadorPrincipal.velocidad = 0

def main():
	pygame.init() #Iniciamos pygame
	
	#Configuracion juego
	ventana = pygame.display.set_mode((640, 480)) #Tamaño de la ventana
	nombreVentana =	pygame.display.set_caption("Sokoban")	#Nombre del proyecto
	salir_juego = False #Variable para definir el bucle infinito del juego
	contadorNivel = 1   #Regulador de nivel

	#Creamos todos los objetos que usaremos y definimos las variables que utilizaran
	j_posAnterior = (0, 0)	   #Guardara la posicion del jugador antes de realizar el siguiente movimiento
	caja1_posAnterior = (0, 0) #Estas 4 filas guardan las posiciones anteriores de las cajas antes de realizar el siguiente movimiento
	caja2_posAnterior = (0, 0)
	caja3_posAnterior = (0, 0)
	caja4_posAnterior = (0, 0)
	imagenBaseJugador = pygame.image.load("imagenesBase/cuadrado.png") #Objetos -> ¿Por qué les pasamos una imagen base si tiene que tener una especifica?
	jugadorPrincipal = Jugador(imagenBaseJugador)	#El atributo "rect" (rectangulo de la imagen) de la clase General no puede estar en "None" y necesita tener una imagen
	imagenBaseCaja = pygame.image.load("imagenesBase/caja sin pintar.png") #Se planea solucionar esto posteriormente -> Podria sacarnos lineas de codigo
	caja1 = CuadradoConMovimiento(imagenBaseCaja)
	caja2= CuadradoConMovimiento(imagenBaseCaja)
	caja3= CuadradoConMovimiento(imagenBaseCaja)
	caja4= CuadradoConMovimiento(imagenBaseCaja)
	imagenBaseZona = pygame.image.load("imagenesBase/zona apoyo.png")
	zona1= ZonaApoyo(imagenBaseZona)
	zona2= ZonaApoyo(imagenBaseZona)
	zona3= ZonaApoyo(imagenBaseZona)
	zona4= ZonaApoyo(imagenBaseZona)
	imagenPiso= pygame.image.load("imagenesBase/piso.png")
	piso= General(imagenPiso)
	imagenFondo= pygame.image.load("imagenesBase/fondo.png")
	fondo= General(imagenFondo)

	if(contadorNivel == 1):
		nivel1(jugadorPrincipal, caja1, caja2, caja3, caja4, zona1, zona2, zona3, zona4, piso) #Seteamos el nivel 1 -> ¿Por qué no paso el fondo tambien como parametro? Lo voy a tomar como general para todos los niveles
		imagenPared_336x48 = pygame.image.load("NivelSimpsons/Simpsonpared 336x48.png")  #En este codigo, las paredes no son objetos iguales -> Tienen triangulos distintos ya las paredes se crearon por bloques y no por la union de objetos 48x48 seteados en diversas posiciones
		imagenPared_48x96 = pygame.image.load("NivelSimpsons/Simpsonpared 48x96.png")
		imagenPared_48x192 = pygame.image.load("NivelSimpsons/Simpsonpared 48x192.png")
		imagenPared_48x48 = pygame.image.load("NivelSimpsons/Simpsonpared 48x48.png")
		imagenPared_48x144 = pygame.image.load("NivelSimpsons/Simpsonpared 48x144.png")
		imagenPared_144x48 = pygame.image.load("NivelSimpsons/Simpsonpared 144x48.png")	
		musicaFondo = pygame.mixer.music.load("NivelSimpsons/cancionSimpsons.mp3")
		pygame.mixer.music.set_volume(0.05)	
		pygame.mixer.music.play(10)
		pared_a_roja = General(imagenPared_336x48)  #A = arriba
		pared_a_roja.setearPosicionInicial(100, 48)
		pared_ab_roja= General(imagenPared_336x48)  #AB = abajo
		pared_ab_roja.setearPosicionInicial(100, 336)
		pared_ai_rosa = General(imagenPared_48x96)  #AI = arriba izquierda
		pared_ai_rosa.setearPosicionInicial(100, 96)
		pared_abm_rosa = General(imagenPared_48x96) #ABM = abajo medio
		pared_abm_rosa.setearPosicionInicial(244, 240)
		pared_mi_verde = General(imagenPared_48x192) #MI = medio izquierda
		pared_mi_verde.setearPosicionInicial(52, 144)
		pared_abi_sinPintar = General(imagenPared_48x48) #ABI = Abajo izquierda
		pared_abi_sinPintar.setearPosicionInicial(100, 288)
		pared_abd_celeste = General(imagenPared_48x144)  #ABD = Abajo derecha
		pared_abd_celeste.setearPosicionInicial(436, 240)
		pared_md_celeste = General(imagenPared_48x144)   #MD = medio derecha
		pared_md_celeste.setearPosicionInicial(484, 144)
		pared_ad_amarilla = General(imagenPared_144x48)  #AD = arriba derecha
		pared_ad_amarilla.setearPosicionInicial(388, 96)
		pared_sinAgarrar_amarilla = General(imagenPared_144x48) #AMsinAgararr = arriba medio sin agarrar
		pared_sinAgarrar_amarilla.setearPosicionInicial(196, 144)


	while (salir_juego != True): #Bucle infinito

		rect_movimientoEnX = 0 #Va a guardar el movimiento que debe realizarse en "x" segun la tecla pulsada
		rect_movimientoEnY = 0 #Va a guardar el movimiento que debe realizarse en "y" segun la tecla pulsada

		j_posAnterior = (jugadorPrincipal.rect.left, jugadorPrincipal.rect.top)

		if(contadorNivel == 1): #Esto podria sacarse ya que todos los niveles usan lo mismo (habria que ver con más niveles -> Pueden tener más cajas, menos, etc.)
			caja1_posAnterior = (caja1.rect.left, caja1.rect.top)
			caja2_posAnterior = (caja2.rect.left, caja2.rect.top)
			caja3_posAnterior = (caja3.rect.left, caja3.rect.top)
			caja4_posAnterior = (caja4.rect.left, caja4.rect.top)

		for event in pygame.event.get():  #Agarramos todos los eventos que se producen
			if (event.type == pygame.QUIT):	#Si tocamos cerrar la ventana ("x")
				pygame.quit()	#Salimos de pygame
				sys.exit()      #Cerramos la ventana
			if (event.type == pygame.KEYDOWN):  #Si se pulso una tecla hacia abajo
				if (event.key == pygame.K_UP):		#Depende cual sea el jugador se movera tanto en X y tanto en Y
					rect_movimientoEnY = -jugadorPrincipal.velocidad
					jugadorPrincipal.mover(0, rect_movimientoEnY)
				if (event.key == pygame.K_DOWN):
					rect_movimientoEnY = jugadorPrincipal.velocidad
					jugadorPrincipal.mover(0, rect_movimientoEnY)
				if (event.key == pygame.K_LEFT):
					rect_movimientoEnX = -jugadorPrincipal.velocidad
					jugadorPrincipal.mover(rect_movimientoEnX, 0)
				if (event.key == pygame.K_RIGHT):
					rect_movimientoEnX = jugadorPrincipal.velocidad
					jugadorPrincipal.mover(rect_movimientoEnX, 0)	
				if (event.key == pygame.K_r): #Con R se resetea el nivel en el caso de que la persona se haya trabado
					if(contadorNivel == 1):	#Si estabamos en el nivel 1
						jugadorPrincipal.hablarPerdio.play() #El jugador lanza su mensaje de "perdio"
						jugadorPrincipal.setearPosicionInicial(148,192) #Todos los objetos con movimiento vuelven donde empezaban
						caja1.setearPosicionInicial(148,144)
						caja2.setearPosicionInicial(244,192)
						caja3.setearPosicionInicial(388,192)
						caja4.setearPosicionInicial(340,240)
						jugadorPrincipal.velocidad = 48 #Y ademas le devolvemos la velocidad al personaje (esto sirve en el caso de que ya haya ganado y quiera repetir el nivel) repetir el nivel
		
		if (contadorNivel == 1):	
		#¿Se acuerdan que dijimos que ibamos a explicar lo de "CajaAnalizar"(parametro que es la primer caja que recibe esta funcion)?:
			#La funcion en realidad podria funcionar de otra forma sin un "CajaAnalizar pero, ¿por qué lo pusimos?
			#Si vemos en la funcion, "cajaAnalizar" es la caja por la que preguntamos si el jugador la ha chocado y
			#Dependiendo de esto se cumpla o no, se ejecutaran determinadas condiciones
			#Entonces, por cada vez que yo llame a esa funcion, aparte de controlar las cosas generales del nivel, regulare las colisiones
			#de una sola caja contra todas las paredes, el jugador y las demás cajas.
			#¿Que hace esto? -> Controlar solo una caja por cada llamada a la funcion que yo hago.
			#De lo contario, tendria que hacer 4 ciclos de control de colisiones, uno para cada caja.
			#Todavia hay que analizar en profundidad que forma es mejor.
				#Caja1
			AdministradorNivel1(jugadorPrincipal, caja1, caja2, caja3, caja4, caja1_posAnterior, rect_movimientoEnX, rect_movimientoEnY, j_posAnterior, pared_ab_roja, pared_a_roja, pared_abm_rosa, pared_ai_rosa, pared_ad_amarilla, pared_sinAgarrar_amarilla, pared_md_celeste, pared_abd_celeste, pared_abi_sinPintar, pared_mi_verde, zona1, zona2, zona3, zona4)
				#Caja2
			AdministradorNivel1(jugadorPrincipal, caja2, caja1, caja3, caja4, caja2_posAnterior, rect_movimientoEnX, rect_movimientoEnY, j_posAnterior, pared_ab_roja, pared_a_roja, pared_abm_rosa, pared_ai_rosa, pared_ad_amarilla, pared_sinAgarrar_amarilla, pared_md_celeste, pared_abd_celeste, pared_abi_sinPintar, pared_mi_verde, zona1, zona2, zona3, zona4)
				#Caja3
			AdministradorNivel1(jugadorPrincipal, caja3, caja1, caja2, caja4, caja3_posAnterior, rect_movimientoEnX, rect_movimientoEnY, j_posAnterior, pared_ab_roja, pared_a_roja, pared_abm_rosa, pared_ai_rosa, pared_ad_amarilla, pared_sinAgarrar_amarilla, pared_md_celeste, pared_abd_celeste, pared_abi_sinPintar, pared_mi_verde, zona1, zona2, zona3, zona4)
				#Caja4
			AdministradorNivel1(jugadorPrincipal, caja4, caja1, caja2, caja3, caja4_posAnterior, rect_movimientoEnX, rect_movimientoEnY, j_posAnterior, pared_ab_roja, pared_a_roja, pared_abm_rosa, pared_ai_rosa, pared_ad_amarilla, pared_sinAgarrar_amarilla, pared_md_celeste, pared_abd_celeste, pared_abi_sinPintar, pared_mi_verde, zona1, zona2, zona3, zona4)
		
		#Actualizamos en pantalla todo lo general para todos los niveles (en base a todos los niveles hasta ahora -> podria cambiar)
		fondo.update(ventana) #Todos tienen un fondo
		piso.update(ventana)	#Todos tienen un piso
		zona1.update(ventana)	#... 4 zonas de apoyo
		zona2.update(ventana)	
		zona3.update(ventana)
		zona4.update(ventana)
		caja1.update(ventana)   #... 4 cajas
		caja2.update(ventana)
		caja3.update(ventana)
		caja4.update(ventana)   #.... y 1 jugador
		jugadorPrincipal.update(ventana) #Pero, lo que debemos tener cuidado es con las paredes. No todos los niveles tendran las mismas paredes, ni tampoco la misma cantidad
		if (contadorNivel == 1):
			pared_ab_roja.update(ventana)
			pared_a_roja.update(ventana)
			pared_abm_rosa.update(ventana)
			pared_ai_rosa.update(ventana)
			pared_md_celeste.update(ventana)
			pared_abd_celeste.update(ventana)
			pared_ad_amarilla.update(ventana)
			pared_sinAgarrar_amarilla.update(ventana)
			pared_mi_verde.update(ventana)
			pared_abi_sinPintar.update(ventana)

		pygame.display.update()

main()