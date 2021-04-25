import pygame
import pygame.camera
import sys
from pygame.locals import *

pygame.init()
pygame.camera.init()
screen = pygame.display.set_mode((320, 240))
cam = pygame.camera.Camera("/dev/video0", (320, 240), "JPEG")

cam.start()
while 1:
    image = cam.get_image()
    screen.blit(image, (0, 0))
    pygame.display.set_caption(str("Minha Câmera"))
    pygame.display.update()
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
