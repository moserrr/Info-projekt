import pygame
import sys
import random

 

# Initialize Pygame
pygame.init()

 

# Define the size of the screen
screen_width = 800
screen_height = 600
screen_size = (screen_width, screen_height)

 

# Create the screen
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Start Button")

 

# Define colors
ROSA = (255, 192, 203)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

 

# Define the size and position of the start button
button_width = 200
button_height = 100
button_pos = ((screen_width - button_width) // 2, (screen_height - button_height) // 2)

 

# Define the font and size for the start button text
font = pygame.font.Font(None, 40)

 

# Define the text for the start button
text = font.render("Start", True, BLACK)

 

# Define the rectangle for the start button
button_rect = pygame.Rect(button_pos, (button_width, button_height))

 

# Variable to show or hide the start button
button_visible = True

 

# Game loop to keep the start screen open
while button_visible:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button_rect.collidepoint(mouse_pos):
                button_visible = False
                print("Start button clicked!")

 

    # Clear the previous frame
    screen.fill(ROSA)

 

    # Draw the start button
    pygame.draw.rect(screen, YELLOW, button_rect)
    screen.blit(text, (button_pos[0] + 70, button_pos[1] + 30))

 

    # Update the screen
    pygame.display.update()

 

# Set up game variables
platform_width, platform_height = 150, 40
platform_speed = 1

 

# Load the image
player_image = pygame.image.load("MicrosoftTeams-image (6).png")

 

# Get the size of the image
player_width, player_height = player_image.get_rect().size

 

# Set the initial position of the image
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height

 

# List to store platform positions
platforms = []

 

# Number of platforms to create
num_platforms = 5

 

# Generate random platform positions
for _ in range(num_platforms):
    x = random.randint(0, screen_width - platform_width)
    y = random.randint(0, screen_height - platform_height)
    platforms.append(pygame.Rect(x, y, platform_width, platform_height))

 

# Variables for player jumping
jumping = False
jump_count = 10

 

# Game loop to keep the game window open
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

 

    # Move the player left or right
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= platform_speed
    if keys[pygame.K_RIGHT]:
        player_x += platform_speed

 

    # Limit the position of the player within the window
    if player_x < 0:
        player_x = 0
    elif player_x > screen_width - player_width:
        player_x = screen_width - player_width

 

    # Player jumping logic
    if not jumping:
        for platform in platforms:
            if platform.colliderect(pygame.Rect(player_x, player_y, player_width, player_height)):
                jumping = True
                jump_count = 10
                player_y = platform.y - player_height
                break
        else:
            player_y += platform_speed

 

    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            player_y -= (jump_count ** 2) * 0.9 * neg
            jump_count -= 1
        else:
            jumping = False

 

    # Clear the previous frame
    screen.fill(ROSA)

 

    # Draw the platforms
    for platform in platforms:
        pygame.draw.rect(screen, YELLOW, platform)

 

    # Draw the player
    screen.blit(player_image, (player_x, player_y))

 

    # Update the screen
    pygame.display.update()



