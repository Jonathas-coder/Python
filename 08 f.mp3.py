import pygame
from pygame import mixer
mixer.init()
pygame.init()
pygame.mixer.music.load('08 f.mp3')
pygame.mixer.music.play()
pygame.event.wait()