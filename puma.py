import pygame, sys
from numpy.random import random_integers
import time

colores = {"verde": (98, 192, 73),
            "rojo": (192, 18, 18),
            "azul": (0, 160, 255),
            "amarillo": (208, 208, 0),
            "blanco":(255,255,255)}

cnombres = ["verde","rojo","azul","amarillo"]

im= {1 : pygame.transform.scale(pygame.image.load('esfera.png'), (50, 50)),
                2 : pygame.transform.scale(pygame.image.load('esfera1.png'), (50, 50)),
                3 : pygame.transform.scale(pygame.image.load('esfera2.png'), (50, 50)),
                4 : pygame.transform.scale(pygame.image.load('esfera3.png'), (50, 50))}

class Ventana():
    def __init__(self,ancho,alto,titulo,color):
        self.ancho = ancho
        self.alto = alto
        self.titulo = titulo
        self.color = color

def choose(lista):
    """
    Devuelve un elemento aleatorio de la lista
    """
    return lista[random_integers(len(lista))-1]

if __name__ == "__main__":
    pygame.init()
    
    v = Ventana(600,600,"Nueva ventana", (255,255,255))

    pantalla = pygame.display.set_mode((v.ancho,v.alto), 0, 32)
    pantalla.fill(v.color)
    pygame.display.set_caption(v.titulo)

    """
    NO LO BORES!!
    for i in range(80):
        pygame.draw.circle(pantalla,
            colores[choose(cnombres)],
            (random_integers(v.ancho),
            random_integers(v.alto)),
            random_integers(50),
            0)
    for i in range(122):
        pantalla.blit(im[random_integers(4)],pygame.Rect(random_integers(600),random_integers(600),50,50))
    """
    #Quitamos los circulos y la spelotas
    
    pygame.display.update() #Sin esta linea el juego no funciona
    
    pelotas = list()
    for i in range(1,5):
        pelotas.append({"img":im[i],
                        "rect":im[i].get_rect()})
    
    bob = {"img" : im[1], "rect" : im[1].get_rect()} #Declaramos a bob como un diccionario
    
    vertical = 0
    horizontal = 0
    while True: #Este es el bucle principal
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                #bob["rect"].left += 1
                if event.key == pygame.K_UP:
                    bob["rect"].top -= 4
                    vertical = -1
                    if bob["rect"].top < 0:
                        bob["rect"].top = 0
                if event.key == pygame.K_DOWN:
                    bob["rect"].top += 4
                    vertical = 1
                    if bob["rect"].top > v.alto-50:
                        bob["rect"].top = v.alto-50
                if event.key == pygame.K_LEFT:
                    bob["rect"].left -= 4
                    horizontal = -1
                    if bob["rect"].left < 0:
                        bob["rect"].left = 0
                if event.key == pygame.K_RIGHT:
                    bob["rect"].left += 4
                    horizontal = 1
                    if bob["rect"].left > v.ancho-50:
                        bob["rect"].left = v.ancho-50    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    vertical = 0
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    horizontal = 0
        
        if vertical:
            bob["rect"].top += 4*vertical
            if bob["rect"].top < 0:
                bob["rect"].top = 0
            if bob["rect"].top > v.alto-50:
                bob["rect"].top = v.alto-50
        if horizontal:
            bob["rect"].left += 4*horizontal
            if bob["rect"].left > v.ancho-50:
                bob["rect"].left = v.ancho-50
            if bob["rect"].left < 0:
                bob["rect"].left = 0
        
        pantalla.fill(colores["blanco"])
        
        """
        for pelota in pelotas:
            pelota["rect"].left += pelota["x"]
            pelota["rect"].top += pelota["y"]
            pantalla.blit(pelota["img"], pelota["rect"])
        """
        pantalla.blit(bob["img"],bob["rect"])
        
        pygame.display.update()
        
        time.sleep(0.02)
        

"""
Experimentos para hacer juegos en pygame



"""
