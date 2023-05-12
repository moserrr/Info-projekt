import pygame

# Initialisieren Sie Pygame
pygame.init()

# Definieren Sie die Größe des Fensters
size = (700, 750)

# Öffnen Sie das Pygame-Fenster mit der Hintergrundfarbe Blau
screen = pygame.display.set_mode(size)
screen.fill((255, 192, 203))

# Schleife, um das Fenster geöffnet zu halten
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()


# Festlegen der Schriftart und Größe
font = pygame.font.SysFont("Arial", 30)

    

