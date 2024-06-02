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
background_rect = background.get_rect()

# Базовый класс для спрайтов
class Entity(pygame.sprite.Sprite):
    def __init__(self, image_file, speed=0, x=0, y=0):
        super().__init__()
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed

    def update(self):
        pass

# Класс игрока
class Player(Entity):
    def __init__(self):
        super().__init__(r'C:\\Users\\sedof\\Documents\\vscode\\ITiABD-PM22-7-Nikolay-Sedov\\Practicum\\pygame\\laba3\\Bringer-of-Death_Walk_7.png', 1, 100, screen_height // 2)

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        self.rect.clamp_ip(screen.get_rect())  # Ограничение перемещения внутри экрана

        # Обновление позиции фона
        global background_x, background_y
        if self.rect.right >= screen_width - 100:
            background_x -= self.speed
            if background_x < screen_width - background_rect.width:
                background_x = screen_width - background_rect.width
        if self.rect.left <= 100:
            background_x += self.speed
            if background_x > 0:
                background_x = 0
        if self.rect.bottom >= screen_height - 100:
            background_y -= self.speed
            if background_y < screen_height - background_rect.height:
                background_y = screen_height - background_rect.height
        if self.rect.top <= 100:
            background_y += self.speed
            if background_y > 0:
                background_y = 0

# Класс врага
class Enemy(Entity):
    def __init__(self, x, y):
        super().__init__(r'C:\\Users\\sedof\\Documents\\vscode\\ITiABD-PM22-7-Nikolay-Sedov\\Practicum\\pygame\\laba3\\idle.png', 0, x, y)

# Класс стрелы
class Arrow(Entity):
    def __init__(self, x, y):
        super().__init__(r'C:\\Users\\sedof\\Documents\\vscode\\ITiABD-PM22-7-Nikolay-Sedov\\Practicum\\pygame\\laba3\\arrow.png', 1, x, y)
        self.image = pygame.transform.scale(self.image, [50, 20])  # Уменьшим размер изображения для более адекватного отображения
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.centery = y

    def update(self):
        self.rect.x += self.speed
        if self.rect.x > screen_width:
            self.kill()  # Удалить, если вышла за пределы экрана

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
