import pygame
import sys

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

# rectangulos por ahora
player_img = pygame.Surface((50, 40))
player_img.fill((0, 255, 0))  # Verde

bullet_img = pygame.Surface((5, 10))
bullet_img.fill((255, 0, 0))  # Rojo

# Clases
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
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

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = -10

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()

player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

bullets_group = pygame.sprite.Group()

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

    # Dibujar
    screen.fill(BLACK)
    player_group.draw(screen)
    bullets_group.draw(screen)
    
    pygame.display.flip()

# Salir
pygame.quit()
sys.exit()
