import pygame, sys
pygame.init()

# Colores
BLACK   = (   0,   0,   0)
WHITE   = ( 255, 255, 255)
GREEN   = (   0, 255,   0)
RED     = ( 255,   0,   0)
BLUE    = (   0,   0, 255)

# Pantalla
screen_size = (800,600)

# FPS
clock = pygame.time.Clock()
screen = pygame.display.set_mode(screen_size)

# Ciclo inicial
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    # Color de fondo
    screen.fill(BLACK)

    ### --------------- Zona de dibujo


    ### --------------- Zona de dibujo


    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(60)

    pass
