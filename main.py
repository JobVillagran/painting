import pygame

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Paint")

# Variables de color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Variables de dibujo
drawing = False
last_pos = None

# Bucle principal del programa
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Botón izquierdo del ratón
                drawing = True
                last_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Botón izquierdo del ratón
                drawing = False
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                current_pos = event.pos
                pygame.draw.line(screen, WHITE, last_pos, current_pos, 2)
                last_pos = current_pos

    pygame.display.flip()

# Salir de Pygame
pygame.quit()