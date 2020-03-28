import pygame

pygame.init()

def create_window():
    window = pygame.display.set_mode((800,600),pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.FULLSCREEN)


create_window()

isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_a:
                isRunning = False


pygame.quit()