

import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка размеров окна
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Загрузка фонового изображения
background = pygame.image.load('C:\\Users\\sedof\\Documents\\vscode\\ITiABD-PM22-7-Nikolay-Sedov\\Practicum\\pygame\\laba3\\1700.jpg')
background_x, background_y = 0, 0

# Базовый класс для спрайтов
class Entity(pygame.sprite.Sprite):
    def __init__(self, image_file, speed=0, x=0, y=0):
        super().__init__()
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect(x=x, y=y)
        
        self.speed = speed

    def update(self):
        pass

# Класс игрока
class Player(Entity):
    def __init__(self):
        super().__init__(r'C:\\Users\\sedof\\Documents\\vscode\\ITiABD-PM22-7-Nikolay-Sedov\\Practicum\\pygame\\laba3\\Bringer-of-Death_Walk_7.png', 5, 100, screen_height // 2)

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        self.rect.x = max(0, min(screen_width - self.rect.width, self.rect.x))
        self.rect.y = max(0, min(screen_height - self.rect.height, self.rect.y))

# Класс врага
class Enemy(Entity):
    def __init__(self, x, y):
        super().__init__(r'C:\\Users\\sedof\\Documents\\vscode\\ITiABD-PM22-7-Nikolay-Sedov\\Practicum\\pygame\\laba3\\idle.png', 0, x, y)

# Класс стрелы
class Arrow(Entity):
    def __init__(self, x, y):
        super().__init__(r'C:\\Users\\sedof\\Documents\\vscode\\ITiABD-PM22-7-Nikolay-Sedov\\Practicum\\pygame\\laba3\\arrow.png', 1, x, y)
        self.image = pygame.transform.scale(self.image, [30,30] )
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > screen_width:
            self.kill() # Удалить, если вышла за пределы экрана

# Создание спрайтов
player = Player()
enemy1 = Enemy(400, 100)
enemy2 = Enemy(600, 300)

# Группы спрайтов
all_sprites = pygame.sprite.Group()
arrows = pygame.sprite.Group()
enemies = pygame.sprite.Group()

for entity in [player, enemy1, enemy2]:
    all_sprites.add(entity)
enemies.add(enemy1)
enemies.add(enemy2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                arrow = Arrow(player.rect.right, player.rect.centery)
                all_sprites.add(arrow)
                arrows.add(arrow)

    keys = pygame.key.get_pressed()
    player.update(keys)

    # Обновление спрайтов
    arrows.update()
    enemies.update()

    # Проверка столкновений
    for arrow in arrows:
        hit = pygame.sprite.spritecollide(arrow, enemies, True)
        if hit:
            arrow.kill()

    # Отрисовка
    screen.blit(background, (background_x, background_y))
    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()
