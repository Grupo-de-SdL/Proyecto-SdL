# This Python file uses the following encoding: utf-8
import pygame, sys
from pygame.locals import * #importamos todos los modulos de pygame

class General(pygame.sprite.Sprite): #Esta es la clase abarca todos los objetos del juego
	def __init__ (self, imagen, posInicialX, posInicialY): #Todos tienen una imagen y una posicion inicial
		pygame.sprite.Sprite.__init__(self)
		self.image = imagen        
		self.rect = self.image.get_rect()  #Rectangulo de la imagen (necesitamos el rectangulo para las colisiones)
		self.rect.left = posInicialX
		self.rect.top = posInicialY			

	def update(self, superficie):				#Este metodo actualiza el objeto en una superficie que le pasemos como parametro
		superficie.blit(self.image, self.rect)	#Podria estar solamente en la subclase "Fondo" ya que es la unica clase que realmente lo usa.

	def setImagen(self, imagen): #Metodo para setear la imagen del objeto (Podria sacarse. No es tan necesario)
		self.image = imagen

	def setearPosicionInicial(self, posInicialX, posInicialY): #Metodo para setear la posicion inicial de un objeto (también podria sacarse)
		self.rect.left = posInicialX						   #Los valores se pueden asignar sin un metodo. Además son pocos
		self.rect.top = posInicialY

class CuadradoConMovimiento(General): #¿Que objetos se moveran? -> El jugador y las cajas
	def __init__(self, imagen, posInicialX, posInicialY):		 
			General.__init__(self, imagen, posInicialX, posInicialY)	
			self.sonidoColision = None	#Sonido que hara el objeto al colisionar

	def colisiono(self, rectanguloChoque):	#Ese metodo nos dira si objeto colisiono con otro objeto que le pasamos como parametro
		colision = False					#¿Por qué esta en esta clase? -> El jugador y las cajas son los que chocan contra otras cosas
		if (self.rect.colliderect(rectanguloChoque)): 
			colision = True
		return colision				

	def mover(self, movimientoEnX, movimientoEnY):	#Mueve el objeto tantas posiciones en "x" y tantas posiciones en "y"
		self.rect.move_ip(movimientoEnX, movimientoEnY)
		
class ZonaApoyo(General):	#Clase para las zonas de apoyo -> Las zonas de apoyo tienen algo que ningun otro elemento del juego tiene:
	def __init__(self, imagen, posInicialX, posInicialY):	#Las zonas de apoyo tienen un "estado" que es el que va a determinar si un objeto esta sobre ella o no
		General.__init__(self, imagen, posInicialX, posInicialY)
		self.estado = False	

class Jugador(CuadradoConMovimiento): #Clase para el jugador -> ¿Que tiene el jugador que los demás objetos no? -> Una velocidad y sonidos caracteristicos cuando gana o pierde
	def __init__(self, imagen, posInicialX, posInicialY):		  #Las cajas se mueven y por ende, también podria decirse que tienen velocidad. Pero, ¿no se mueven a
		General.__init__(self, imagen, posInicialX, posInicialY)	#la misma velocidad que el jugador? Por ende, en este caso, solo vamos a definirla en Jugador y luego reutilizar esta velocidad en las cajas
		self.velocidad = 48 										#y luego reutilizar esta velocidad en las cajas
		self.hablarPerdio = None #Aqui ira un sonido
		self.hablarGano = None	 #Aqui ira un sonido

class Fondo(General):		#¿Por qué una clase fondo cuando solo fondo es una imagen o un rectangulo con una imagen?
	def __init__(self, imagen, posInicialX, posInicialY):
		General.__init__(self, imagen, posInicialX, posInicialY)
		self.sonidoFondo = None #Porque en este caso vamos a hacer que el fondo sea el que tenga la musica "incorporada"

#cargaNivel1() -> Crea y setea las imagenes, sonidos y posiciones de todos los elementos del nivel 1.
def cargaNivel1():
	#Jugador 
	imagenJugadorPrincipal= pygame.image.load("NivelSimpsons/jugadorHomero.png")
	jugadorPrincipal = Jugador(imagenJugadorPrincipal, 148, 192)
	jugadorPrincipal.hablarPerdio =	pygame.mixer.Sound("NivelSimpsons/homeroDoh.wav")
	jugadorPrincipal.hablarGano = pygame.mixer.Sound("NivelSimpsons/homeroFestejo.wav")
	jugadorPrincipal.hablarPerdio.set_volume(0.05)
	jugadorPrincipal.hablarGano.set_volume(0.05)
	#Caja
	imagenCaja= pygame.image.load("NivelSimpsons/cajaSimpsons.png")
	caja1= CuadradoConMovimiento(imagenCaja, 148, 144)
	caja2= CuadradoConMovimiento(imagenCaja, 244, 192)
	caja3= CuadradoConMovimiento(imagenCaja, 388, 192)
	caja4= CuadradoConMovimiento(imagenCaja, 340, 240)
	caja1.sonidoColision = pygame.mixer.Sound("NivelSimpsons/golpeCaja.wav")
	caja2.sonidoColision = pygame.mixer.Sound("NivelSimpsons/golpeCaja.wav")
	caja3.sonidoColision = pygame.mixer.Sound("NivelSimpsons/golpeCaja.wav")
	caja4.sonidoColision = pygame.mixer.Sound("NivelSimpsons/golpeCaja.wav")
	caja1.sonidoColision.set_volume(0.05)
	caja2.sonidoColision.set_volume(0.05)
	caja3.sonidoColision.set_volume(0.05)
	caja4.sonidoColision.set_volume(0.05)
	#ZonaDeApoyo
	imagenZona = pygame.image.load("NivelSimpsons/zonaRosca.png")
	zona1= ZonaApoyo(imagenZona, 148, 240)
	zona2= ZonaApoyo(imagenZona, 148, 288)
	zona3= ZonaApoyo(imagenZona, 196, 240)
	zona4= ZonaApoyo(imagenZona, 196, 288)
	#Paredes
	imagenPared_336x48 = pygame.image.load("NivelSimpsons/Simpsonpared 336x48.png")  #En este codigo, las paredes no son objetos iguales -> Tienen triangulos distintos ya las paredes se crearon por bloques y no por la union de objetos 48x48 seteados en diversas posiciones
	imagenPared_48x96 = pygame.image.load("NivelSimpsons/Simpsonpared 48x96.png")
	imagenPared_48x192 = pygame.image.load("NivelSimpsons/Simpsonpared 48x192.png")
	imagenPared_48x48 = pygame.image.load("NivelSimpsons/Simpsonpared 48x48.png")
	imagenPared_48x144 = pygame.image.load("NivelSimpsons/Simpsonpared 48x144.png")
	imagenPared_144x48 = pygame.image.load("NivelSimpsons/Simpsonpared 144x48.png")	
	pared_a_roja = General(imagenPared_336x48, 100, 48)  #A = arriba
	pared_ab_roja= General(imagenPared_336x48, 100, 336)  #AB = abajo
	pared_ai_rosa = General(imagenPared_48x96, 100, 96)  #AI = arriba izquierda
	pared_abm_rosa = General(imagenPared_48x96, 244, 240) #ABM = abajo medio
	pared_mi_verde = General(imagenPared_48x192, 52, 144) #MI = medio izquierda
	pared_abi_sinPintar = General(imagenPared_48x48, 100, 288) #ABI = Abajo izquierda
	pared_abd_celeste = General(imagenPared_48x144, 436, 240)  #ABD = Abajo derecha
	pared_md_celeste = General(imagenPared_48x144, 484, 144)   #MD = medio derecha
	pared_ad_amarilla = General(imagenPared_144x48, 388, 96)  #AD = arriba derecha
	pared_sinAgarrar_amarilla = General(imagenPared_144x48, 196, 144) #AMsinAgararr = arriba medio sin agarrar
	#Piso
	imagenBasePiso= pygame.image.load("NivelSimpsons/piso.png")
	piso1= General(imagenBasePiso, 100, 96)
	#Fondo
	imagenFondo = pygame.image.load("NivelSimpsons/fondo.png")
	fondoNivel1 = Fondo(imagenFondo, 0, 0)
	fondoNivel1.sonidoFondo = pygame.mixer.music.load("NivelSimpsons/cancionSimpsons.mp3")
	pygame.mixer.music.set_volume(0.05)	
	pygame.mixer.music.play(10)

	#Estas variables se explicaran más adelante. Se puede ver que estamos guardando ciertos objetos en una lista. Esto nos servira para administarlos mejor
	fondo = fondoNivel1
	jugador = jugadorPrincipal
	piso = piso1
   	paredes= [pared_a_roja, pared_ab_roja, pared_ai_rosa, pared_abm_rosa, pared_mi_verde, pared_abi_sinPintar, pared_abd_celeste, pared_md_celeste, pared_ad_amarilla, pared_sinAgarrar_amarilla]   
	zonas= [zona1, zona2, zona3, zona4]
	cajas= [caja1, caja2, caja3, caja4]

	return paredes, zonas, cajas, jugador, piso, fondo

#cargarNivel2() -> Crea y setea las imagenes, sonidos y posiciones de todos los elementos del nivel 2.
def cargarNivel2():
	#Jugador
	imagenJugadorPrincipal = pygame.image.load("nivelRpg/jugador-mago.png")
	jugadorPrincipal= Jugador(imagenJugadorPrincipal, 144, 48)
	jugadorPrincipal.hablarPerdio =	pygame.mixer.Sound("NivelRpg/Game-Over.wav")
	jugadorPrincipal.hablarGano = pygame.mixer.Sound("NivelRpg/Victory_Fanfare.wav")
	jugadorPrincipal.hablarPerdio.set_volume(0.05)
	jugadorPrincipal.hablarGano.set_volume(0.05)
	#Cajas
	imagenCaja = pygame.image.load("nivelRpg/caja.png")
	caja1= CuadradoConMovimiento(imagenCaja, 192, 96)
	caja2= CuadradoConMovimiento(imagenCaja, 192, 144)
	caja3= CuadradoConMovimiento(imagenCaja, 240, 96)
	caja1.sonidoColision = pygame.mixer.Sound("NivelRpg/golpe_caja_rpg.wav")
	caja2.sonidoColision = pygame.mixer.Sound("NivelRpg/golpe_caja_rpg.wav")
	caja3.sonidoColision = pygame.mixer.Sound("NivelRpg/golpe_caja_rpg.wav")
	caja1.sonidoColision.set_volume(0.05)
	caja2.sonidoColision.set_volume(0.05)
	caja3.sonidoColision.set_volume(0.05)
    #Zonas de apoyo
	imagenZona = pygame.image.load("nivelRpg/zona apoyo.png")
	zona1 = ZonaApoyo(imagenZona, 432, 144)
	zona2 = ZonaApoyo(imagenZona, 432, 192)
	zona3 = ZonaApoyo(imagenZona, 432, 240)
    #Paredes
	imagenPared_240x48 = pygame.image.load("nivelRpg/RpgPared 240x48.png")
	imagenPared_144x48 = pygame.image.load("nivelRpg/RpgPared 144x48.png")
	imagenPared_48x192 = pygame.image.load("nivelRpg/RpgPared 48x192.png")
	imagenPared_48x96 = pygame.image.load("nivelRpg/RpgPared 48x96.png")
	imagenPared_48x48 = pygame.image.load("nivelRpg/RpgPared 48x48.png")
	pared_a_rosa = General(imagenPared_240x48, 96, 0)
	pared_ab_rosa = General(imagenPared_240x48, 144, 384)
	pared_ai_verde = General(imagenPared_48x192, 96, 48)
	pared_abi_verde = General(imagenPared_48x192, 144, 192)
	pared_am_verde = General(imagenPared_48x192, 288, 48)
	pared_abd_verde = General(imagenPared_48x192, 480, 144)
	pared_ai_azul = General(imagenPared_48x96, 192, 192)
	pared_md_azul = General(imagenPared_48x96, 384, 144)
	pared_ad_rosa = General(imagenPared_144x48, 384, 96)
	pared_abd_rosa = General(imagenPared_144x48, 336, 336)
	pared_abi_sinPintar = General(imagenPared_48x48, 480, 336)
	pared_abm_sinPintar = General(imagenPared_48x48, 336, 288)
	pared_mm_sinPintar = General(imagenPared_48x48, 336, 192)
    #Piso
	imagenPiso = pygame.image.load("nivelRpg/RpgPiso.png")
	piso1 = General(imagenPiso, 144, 48)
	#Fondo
	imagenFondo = pygame.image.load("nivelRpg/fondo.png")
	fondoNivel2 = General(imagenFondo, 0, 0)
	fondoNivel2.sonidoFondo = pygame.mixer.music.load("NivelRpg/Blue-Caverns.mp3")
	pygame.mixer.music.set_volume(0.05)	
	pygame.mixer.music.play(10)

	#Lo mismo que en la funcion anterior. Notese que guardamos ciertas cosas en listas. Generalmente los objetos de un cierto tipo que a la vez son más de uno.
	fondo = fondoNivel2
	jugador = jugadorPrincipal
	piso = piso1
	paredes = [pared_a_rosa, pared_ab_rosa, pared_ai_verde, pared_abi_verde, pared_am_verde, pared_abd_verde, pared_ai_azul, pared_md_azul, pared_ad_rosa, pared_abd_rosa, pared_abi_sinPintar, pared_abm_sinPintar, pared_mm_sinPintar]
	zonas = [zona1, zona2, zona3]
	cajas = [caja1, caja2, caja3]
	return paredes, zonas, cajas, jugador, piso, fondo

#administrarNivel() -> Administra todas las colisiones y determina si el nivel ha terminado o no
def administrarNivel(paredes, zonas, cajas, jugador, j_posAnterior, caja1_posAnterior, caja2_posAnterior, caja3_posAnterior, caja4_posAnterior, rect_movimientoEnX, rect_movimientoEnY):
	nivelCompleto = False	#Lo usaremos para configurar si el nivel esta completo o no
	colisionParedJugador = False #Para saber si el jugador choco contra una pared
	colisionCajaJugador = False	 #Para saber si el jugador choca contra una caja
	colisionCajaPared = False	 #Para saber si la caja choco contra una pared
	colisionCajaCaja = False	 #Para saber si la caja choco contra otra caja
	cantidadZonasActivas = 0     #Contendra la cantidad de zonas que tienen una caja encima 
	indiceChocada = 0            #Se explicara en breve

	for a in range(len(paredes)):  	#Vamos recorriendo la lista de paredes y preguntamos si el jugador choco con alguna de todas estas
		if jugador.colisiono(paredes[a]):
			(jugador.rect.left, jugador.rect.top) = j_posAnterior #Si es asi, que el jugador vuelva a su posicion anterior
			colisionParedJugador = True #Existe una colision entre Pared y jugador. 
			a = len(paredes) #Terminamos el bucle. Ya encontramos la colision que buscabamos

	if (colisionParedJugador != True): #Si no choco con una pared...
		for b in range(len(cajas)):    #Vamos a ver si choco contra alguna de todas las cajas...
			if jugador.colisiono(cajas[b]): #Si fue asi, 
				cajas[b].mover(rect_movimientoEnX, rect_movimientoEnY) #Movemos la caja
				indiceChocada = b #Guardamos el indice de la caja que el jugador choco. Esta caja especifica es la que tendremos que mover
				colisionCajaJugador = True	
				b = len(cajas) #Terminamos el bucle. Ya encontramos la colision que buscabamos

	if (colisionCajaJugador == True): #Si existio una colision entre caja y jugador
		for c in range(len(paredes)): #Preguntamos si cuando movimos la caja esta choco contra alguna de todas las paredes...
			if (cajas[indiceChocada].colisiono(paredes[c])):
				if (indiceChocada == 0): #Si la que choco era la que estaba en cajas[0], sabemos que era la caja1
					cajas[indiceChocada].sonidoColision.play()
					(cajas[indiceChocada].rect.left, cajas[indiceChocada].rect.top) = caja1_posAnterior #No dejamos que avance
					(jugador.rect.left, jugador.rect.top) = j_posAnterior #No dejamos que avance el jugador tampoco
				if (indiceChocada == 1):
					cajas[indiceChocada].sonidoColision.play()
					(cajas[indiceChocada].rect.left, cajas[indiceChocada].rect.top) = caja2_posAnterior
					(jugador.rect.left, jugador.rect.top) = j_posAnterior
				if (indiceChocada == 2):
					cajas[indiceChocada].sonidoColision.play()
					(cajas[indiceChocada].rect.left, cajas[indiceChocada].rect.top) = caja3_posAnterior
					(jugador.rect.left, jugador.rect.top) = j_posAnterior
				if (indiceChocada == 3):
					cajas[indiceChocada].sonidoColision.play()
					(cajas[indiceChocada].rect.left, cajas[indiceChocada].rect.top) = caja4_posAnterior
					(jugador.rect.left, jugador.rect.top) = j_posAnterior
				colisionCajaPared = True #La caja efectivamente choco contra una pared
				c = len(paredes) #Terminamos el bucle. Ya encontramos la colision que buscabamos

	if (colisionCajaPared != True): #Si la caja no choco contra una pared cuando se movio, pudo haber chocado contra otra caja
		for d in range(len(cajas)):	#Preguntamos si la caja especifica que se movio choco contra alguna de las otras cajas
			if ((indiceChocada != d) and (cajas[indiceChocada].colisiono(cajas[d]))): #con indiceChocada !=d evitamos que pregunte si choco contra sigo misma
				if (indiceChocada == 0): #Si la caja que choco era la que estaba en cajas[0]
					cajas[d].sonidoColision.play()
					(cajas[indiceChocada].rect.left, cajas[indiceChocada].rect.top) = caja1_posAnterior #No dejamos que la caja avance
					(jugador.rect.left, jugador.rect.top) = j_posAnterior #No dejamos que avance el jugador tampoco...
				if (indiceChocada == 1):
					cajas[d].sonidoColision.play()
					(cajas[indiceChocada].rect.left, cajas[indiceChocada].rect.top) = caja2_posAnterior
					(jugador.rect.left, jugador.rect.top) = j_posAnterior
				if (indiceChocada == 2):
					cajas[d].sonidoColision.play()
					(cajas[indiceChocada].rect.left, cajas[indiceChocada].rect.top) = caja3_posAnterior
					(jugador.rect.left, jugador.rect.top) = j_posAnterior
				if (indiceChocada == 3):
					cajas[d].sonidoColision.play()
					(cajas[indiceChocada].rect.left, cajas[indiceChocada].rect.top) = caja4_posAnterior
					(jugador.rect.left, jugador.rect.top) = j_posAnterior
				colisionCajaCaja = True #Hubo una colision caja con caja
				d = len(cajas) #Terminamos el bucle. Ya encontramos la colision que buscabamos

	for e in range(len(zonas)): #Recorremos todas las zonas de apoyo y las seteamos en false. Decimos ademas que no hay zonas activas
		zonas[e].estado = False #¿Por qué? Si yo no hago esto puede haber quedado una zona activa en base a un movimiento anterior y...
		cantidadZonasActivas = 0 #si ahora la caja que tenia encima esa zona no la tiene más, no lo contemplaria y seguiria estando como True.

	for f in range(len(cajas)): #Ahora si, con todas las zonas limpias, preguntamos cuantas estan activas para este momento determinado.
		for g in range(len(zonas)): #Con este for anidado podemos contrastar cada caja contra cada zona de apoyo
			if cajas[f].colisiono(zonas[g]): 
				zonas[g].estado = True #La caja colisiono con alguna de las zonas. Seteamos el estado de la zona de apoyo a = True
				cantidadZonasActivas = cantidadZonasActivas + 1 #Suma uno a la cantidad de zonas activas
				g = len(zonas) #Ya encontramos la colision que queriamos. Pasamos a preguntar por la siguiente caja

 	if (cantidadZonasActivas == len(zonas)): #Si la cantidad de zonas activas es igual a la cantidad de zonas existentes
 		nivelCompleto = True #El nivel ha sido ganado
 		
 	return nivelCompleto

#actualizarNivel() -> Actualiza jugador, fondo, piso, paredes, zonas de apoyo y cajas en la pantalla	
def actualizarNivel(ventana, jugador_render, cajas_render, zonas_render, paredes_render, piso_render, fondo):
			fondo.update(ventana)
			piso_render.draw(ventana) #Lo de render se explicara más adelante
			paredes_render.draw(ventana)
			zonas_render.draw(ventana)
			cajas_render.draw(ventana)
			jugador_render.draw(ventana)


def main():
	pygame.init() #Iniciamos pygame

	#Configuracion juego
	ventana = pygame.display.set_mode((640, 480)) #Tamaño de la ventana
	nombreVentana =	pygame.display.set_caption("Sokoban")	#Nombre del proyecto
	clock = pygame.time.Clock() #Nos definira los FPS del juego
	salir_nivel = False #Variable para definir el bucle del juego
	j_posAnterior = (0, 0) #Guardara la posicion del jugador antes de realizar el siguiente movimiento
	caja1_posAnterior = (0, 0) #Estas 4 filas guardan las posiciones anteriores de las cajas antes de realizar el siguiente movimiento
	caja2_posAnterior = (0, 0)
	caja3_posAnterior = (0, 0)
	caja4_posAnterior = (0, 0)


	for juego in range(1, 3): #"For" que administrar los niveles del juego

		if (juego == 1): #Si el ciclo del for es 1 entonces hay que cargar el nivel 1
			paredes, zonas, cajas, jugador, piso, fondo = cargaNivel1() #Decimos que todas estas variables quedaran definidas por el retorno de esta funcion
		if (juego == 2): #Si el ciclo del for es 1 entonces hay que cargar el nivel 2
			paredes, zonas, cajas, jugador, piso, fondo = cargarNivel2()

		#RenderPlain nos permite formar grupos de objetos tipo "sprite"
		piso_render = pygame.sprite.RenderPlain((piso)) #Entonces por ejemplo, piso_render = contendra un grupo dibujable de 1 objeto (hay un solo piso por nivel)
		paredes_render = pygame.sprite.RenderPlain((paredes)) #paredes_render -> contendra un grupo dibujable de "n" objetos pared
		zonas_render = pygame.sprite.RenderPlain((zonas)) 
		cajas_render = pygame.sprite.RenderPlain((cajas))
		jugador_render = pygame.sprite.RenderPlain((jugador))
		vecesCantoVictoria = 0 #Si una persona, a pesar de que el jugador este frenado, sigue tocando teclas despues de ganar el nivel -> El mensaje de victoria se repetira nuevamente
		#Esta variable ayuda a que esto no suceda. Una posible solucion -> Impedir las teclas de movimiento si ya se ha ganado el nivel

		salir_nivel = False
		while (salir_nivel != True): #Mientas salir_nivel sea falso
			clock.tick(60) #Decimos que el juego "corra" a 60 FPS
 
			rect_movimientoEnX = 0 #Va a guardar el movimiento que debe realizarse en "x" segun la tecla pulsada
			rect_movimientoEnY = 0 #Va a guardar el movimiento que debe realizarse en "y" segun la tecla pulsada

			j_posAnterior = (jugador.rect.left, jugador.rect.top) #Va a jugar la posicion anterior del jugador

			for i in range(len(cajas)): #Segun la lista de cajas, cada caja de la lista va a tener una variable que guarda su posicion anterior
				if (i == 0):
					caja1_posAnterior = (cajas[i].rect.left, cajas[i].rect.top)
				if (i == 1):
					caja2_posAnterior = (cajas[i].rect.left, cajas[i].rect.top)
				if (i == 2):
					caja3_posAnterior = (cajas[i].rect.left, cajas[i].rect.top)
				if (i == 3):
					caja4_posAnterior = (cajas[i].rect.left, cajas[i].rect.top)

			for event in pygame.event.get():  #Agarramos todos los eventos que se producen
				if (event.type == pygame.QUIT):	#Si tocamos cerrar la ventana ("x")
					pygame.quit()	#Salimos de pygame
					sys.exit()      #Cerramos la ventana
				if (event.type == pygame.KEYDOWN):  #Si se pulso una tecla hacia abajo
					if (event.key == pygame.K_UP):	#Depende de cual sea -> el jugador se movera tanto en X y tanto en Y
						rect_movimientoEnY = -jugador.velocidad # -48
						jugador.mover(0, rect_movimientoEnY) #(0, -48)
					if (event.key == pygame.K_DOWN):
						rect_movimientoEnY = jugador.velocidad
						jugador.mover(0, rect_movimientoEnY)
					if (event.key == pygame.K_LEFT):
						rect_movimientoEnX = -jugador.velocidad
						jugador.mover(rect_movimientoEnX, 0)
					if (event.key == pygame.K_RIGHT):
						rect_movimientoEnX = jugador.velocidad
						jugador.mover(rect_movimientoEnX, 0)	
					if (event.key == pygame.K_r): #Con R se resetea el nivel en el caso de que la persona se haya trabado
						#Primero preguntamos si el nivel se reseteo antes de ganarse -> Asi sabemos si tocar la musica de "Perdio" o no
						if (administrarNivel(paredes, zonas, cajas, jugador, j_posAnterior, caja1_posAnterior, caja2_posAnterior, caja3_posAnterior, caja4_posAnterior, rect_movimientoEnX, rect_movimientoEnY) == False):
							jugador.hablarPerdio.play() #El jugador lanza su mensaje de "perdio"
						pygame.mixer.music.play() #Iniciamos de nuevo la musica
						vecesCantoVictoria = 0 #Para permitir que si gana, el sonido de victoria se reproduzca -> Esto se pretende arreglar
						jugador.velocidad = 48 #Y ademas le devolvemos la velocidad al personaje (esto sirve en el caso de que ya haya ganado (la velocidad se puso en 0) y quiera repetir el nivel) repetir el nivel
						if(juego == 1): #Si cuando resteamos estabamos en el nivel 1...
							jugador.setearPosicionInicial(148,192) #Movemos el jugador a su posicion inicial en el nivel 1
						if(juego == 2):
							jugador.setearPosicionInicial(144,48)
						for k in range(len(cajas)): #Y, segun el nivel, las cajas
							if (k == 0):
								if (juego == 1):
									cajas[k].setearPosicionInicial(148,144)
								if (juego == 2):
									cajas[k].setearPosicionInicial(192,96)
							if (k == 1):
								if (juego == 1):
 									cajas[k].setearPosicionInicial(244,192)
 								if (juego == 2):
 									cajas[k].setearPosicionInicial(192,144)
 							if (k == 2):
 								if (juego == 1):
									cajas[k].setearPosicionInicial(388,192)
								if (juego == 2):
									cajas[k].setearPosicionInicial(240,96)
							if (k == 3):
								if (juego == 1):
									cajas[k].setearPosicionInicial(340,240)
					if (event.key == pygame.K_n): #Si apreto la letra "N" (pasar al siguiente nivel) -> Preguntamos si el nivel actual se completo. Sino, no puede.
						if (administrarNivel(paredes, zonas, cajas, jugador, j_posAnterior, caja1_posAnterior, caja2_posAnterior, caja3_posAnterior, caja4_posAnterior, rect_movimientoEnX, rect_movimientoEnY)):
							salir_nivel = True #Salimos del nivel para pasar al nivel 2

					#Contramos el nivel en cada ciclo -> ¿Gano el nivel? 
				if (administrarNivel(paredes, zonas, cajas, jugador, j_posAnterior, caja1_posAnterior, caja2_posAnterior, caja3_posAnterior, caja4_posAnterior, rect_movimientoEnX, rect_movimientoEnY)):
					vecesCantoVictoria = vecesCantoVictoria + 1  #Le sumamos uno a las veces que "Canto victoria"
					if (vecesCantoVictoria == 1): #Si ya la canto una vez, no puede cantarla más hasta que reincie el nivel o pase a uno nuevo (como dijimos antes, esto se pretende solucionar)
						jugador.velocidad = 0 #Todo esto se hace una vez sola. Una vez que gano pasa esto y si no sale (o reinicia) del nivel, no pasa otra vez.
 						pygame.mixer.music.stop()
 						jugador.hablarGano.play()

 				#Metodo que nos dibuja y actualiza todo en la pantalla		
				actualizarNivel(ventana, jugador_render, cajas_render, zonas_render, paredes_render, piso_render, fondo)

			pygame.display.update()

	pygame.quit()	

#Esto llama al main
if __name__ == '__main__':
    main()