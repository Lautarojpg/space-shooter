import pygame
import sys
import random

pygame.init()

# Configuración de pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invader")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# FPS
clock = pygame.time.Clock()
FPS = 60

# Imágenes (rectángulos por ahora)
player_img = pygame.Surface((50, 40))
player_img.fill((0, 255, 0))  # Verde

bullet_img = pygame.Surface((5, 10))
bullet_img.fill((255, 0, 0))  # Rojo

enemy_img = pygame.Surface((40, 30))
enemy_img.fill((0, 0, 255))  # Azul

# Clases (esto correspondderia con la historia de usuario de jugador)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() #otro caso de prueba es si el jugador se puedde moverse)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        bullets_group.add(bullet)

#(esto correspondderia con la historia de usuario de jugador)
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = bullet_img #otro caso de prueba es si las balas son disparadas cuando se presiona el boton
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = -10

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()
#(esto correspondderia con la historia de usuario de enemigo)
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = enemy_img #un caso de prueba seria si aparece en la pantalla
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass  # Los enemigos no se mueven por ahora

# Grupos
player = Player()
player_group = pygame.sprite.Group(player)
bullets_group = pygame.sprite.Group()
enemies_group = pygame.sprite.Group()

# Crear enemigos
for i in range(5):
    x = random.randint(0, WIDTH - 40)
    y = random.randint(20, 100)
    enemy = Enemy(x, y)
    enemies_group.add(enemy)

# Game loop
running = True
while running:
    clock.tick(FPS)
    
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Disparar
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # Lógica
    keys = pygame.key.get_pressed()
    player.update(keys)
    bullets_group.update()
    enemies_group.update()

    # Colisiones: bala con enemigo
    pygame.sprite.groupcollide(bullets_group, enemies_group, True, True)

    # Dibujar
    screen.fill(BLACK)
    player_group.draw(screen)
    bullets_group.draw(screen)
    enemies_group.draw(screen)
    
    pygame.display.flip()

# Salir
pygame.quit()
sys.exit()
