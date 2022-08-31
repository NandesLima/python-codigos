import pygame

pygame.mixer.init()
pygame.init()
musica = input('Digite o arquivo da música: ')
pygame.mixer.music.load(musica + ".mp3")
pygame.mixer.music.play()
pygame.event.wait()
