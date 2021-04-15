import pygame
import random

class Object:
    def __init__(self, x, y, x_change, y_change):
        self.x = x
        self.y = y
        self.x_change = x_change
        self.y_change = y_change

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getX_change(self):
        return self.x_change

    def getY_change(self):
        return self.y_change

def draw_player(x, y):
    # screen.blit(image, (x, y)) draws an image on the screen
    screen.blit(playerImage, (x, y))

def draw_enemy(x, y):
    # draws enemy
    screen.blit(enemyImage, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImage, (x+16, y+10))

# Initialize the Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((1000, 800))

# Loads in the background image
background = pygame.image.load("background.jpg")

# Loads in Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

player = Object(370, 480, 0, 0)
playerImage = pygame.image.load("player.png")
playerX = player.getX()
playerY = player.getY()
playerX_change = player.getX_change()
playerY_change = player.getY_change()

enemyX = random.randint(0, 800)
enemyY = random.randint(50, 100)
enemy = Object(enemyX, enemyY, 3, 30)
enemyImage = pygame.image.load("enemy.png")
enemyX_change = enemy.getX_change()
enemyY_change = enemy.getY_change()

bullet = Object(0, 480, 0, 25)
bulletImage = pygame.image.load("bullet.png")
bulletX = bullet.getX()
bulletY = bullet.getY()
bulletX_change = bullet.getX_change()
bulletY_change = bullet.getY_change()
bullet_state = "ready"  # ready - can't see bullet; fire - bullet is currently firing

running = True
while running:
    # Red, Green, Blue. Intervals [0, 255] this sets the color of the screen
    screen.fill((0, 0, 0)) # 0,0,0 is a black screen

    # Draws background image
    screen.blit(background, (-10, -10))

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Trying to quit the window is considered an EVENT
            running = False

        # if we press a key on the keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_UP:
                playerY_change = -5
            if event.key == pygame.K_DOWN:
                playerY_change = 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletX = playerX
                bulletY = playerY
                # draws a bullet and shoots it upwards
                fire_bullet(bulletX, bulletY)

        # if we lift our finger up from the keyboard
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    # Makes the player able to move left or right
    playerX += playerX_change
    playerY += playerY_change

    # creates the boundaries for the left and right sides
    if playerX <= 0:
        playerX = 0
    elif playerX >= 936:
        playerX = 936
    if playerY <= 0:
        playerY = 0
    elif playerY >= 736:
        playerY = 736

    # Makes it able to shoot more than 1 bullet
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    # Makes it able to shoot a bullet and shoots it upwards
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 4
        enemyY += enemyY_change
    elif enemyX >= 936:
        enemyX_change = -4
        enemyY += enemyY_change

    # draws player.png on the screen
    draw_player(playerX, playerY)

    # draws an enemy to the screen
    draw_enemy(enemyX, enemyY)
    pygame.display.update()