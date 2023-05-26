import pygame
import sys

# Initialisieren Sie Pygame
pygame.init()

# Definieren Sie die Größe des Fensters
size = (700, 900)

# Öffnen Sie das Pygame-Fenster mit der Hintergrundfarbe Rosa
screen = pygame.display.set_mode(size)
screen.fill((255, 192, 203))

# Set up game variables
platform_width, platform_height = 150, 40
platform_x = size[0] // 2 - platform_width // 2
platform_y = 1
platform_speed = 5

# Laden Sie das Bild
player_image = pygame.image.load("MicrosoftTeams-image (6).png")

# Erhalten Sie die Größe des Bildes
player_width, player_height = player_image.get_rect().size

# Setzen Sie die Startposition des Bildes
player_x = size[0] // 2 - player_width // 2
player_y = size[1] - player_height

# Schleife, um das Fenster geöffnet zu halten
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Bewegen Sie den Balken nach links oder rechts
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= platform_speed
    if keys[pygame.K_RIGHT]:
        player_x += platform_speed

    # Begrenzen Sie die Position des Balkens innerhalb des Fensters
    if player_x < 0:
        player_x = 0
    elif player_x > size[0] - player_width:
        player_x = size[0] - player_width

    # Löschen Sie den vorherigen Frame
    screen.fill((255, 192, 203))

    # Zeichnen Sie den Balken
    pygame.draw.rect(screen, (255, 255, 0), (platform_x, platform_y, platform_width, platform_height))

    # Zeichnen Sie das Bild
    screen.blit(player_image, (player_x, player_y))

    # Aktualisieren Sie den Bildschirm
    pygame.display.update()

