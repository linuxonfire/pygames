#Importar libreria usar un paquete de funciones relativa a
#imagenes, audio etc..
import pygame

ANCHO = 640
ALTO = 480

class Bolita(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #Cargar imagen
        self.image = pygame.image.load('/home/itzeljaimes/Documents/python/pygames/pendejin.jpg')
        #Obtener rectangulo de la imagen 
        self.rect = self.image.get_rect()
        #Centrar posicion inicial en la pantalla
        self.rect.centerx = ANCHO / 2
        self.rect.centery = ALTO / 2

#inicializar pantalla
pantalla = pygame.display.set_mode((ANCHO,ALTO))

#Configurar titulo de la pantalla

pygame.display.set_caption('Juego de itzel')

bolita = Bolita()
while True:
    #Revisar todos los eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()

    #DIbujar bolita en la pantalla
    pantalla.blit(bolita.image, bolita.rect)

    #Actualizar elementos en pantalla
    pygame.display.flip()