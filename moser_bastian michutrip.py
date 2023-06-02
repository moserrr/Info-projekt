import pygame
import sys

 

# Initialisieren Sie Pygame
pygame.init()

 

# Definieren Sie die Größe des Bildschirms
screen_width = 800
screen_height = 600
screen_size = (screen_width, screen_height)

 

# Erstellen Sie den Bildschirm
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Startknopf")

 

# Definieren Sie Farben
ROSA = (255, 192, 203)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

 

# Definieren Sie die Größe und Position des Startknopfs
button_width = 200
button_height = 100
button_pos = ((screen_width - button_width) // 2, (screen_height - button_height) // 2)

 

# Definieren Sie die Schriftart und Größe für den Text des Startknopfs
font = pygame.font.Font(None, 40)

 

# Definieren Sie den Text des Startknopfs
text = font.render("Start", True, BLACK)

 

# Definieren Sie das Rechteck für den Startknopf
button_rect = pygame.Rect(button_pos, (button_width, button_height))

 

# Variable, um den Startknopf anzuzeigen oder zu verbergen
button_visible = True

 

# Schleife, um den Bildschirm geöffnet zu halten
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button_rect.collidepoint(mouse_pos):
                button_visible = False
                print("Start button clicked!")

 

    # Hintergrund zeichnen
    screen.fill(ROSA)

 

    if button_visible:
        # Startknopf zeichnen
        pygame.draw.rect(screen, YELLOW, button_rect)
        screen.blit(text, (button_pos[0] + 70, button_pos[1] + 30))

    if not button.visible
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
    

 

    # Bildschirm aktualisieren
    pygame.display.update()

    


 



 


 


