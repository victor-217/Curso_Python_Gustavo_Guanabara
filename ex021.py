# importa bibliotecas
import pygame
import os
# iniciar pygame
pygame.init()
# configurações código
if os.path.exists('ex021.mp3'):
    pygame.mixer.music.load('ex021.mp3')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1)

    clock = pygame.time.Clock()
    clock.tick(10)

    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)
else:
    print('O arquivo nao está no diretorio do script python')
# teste
