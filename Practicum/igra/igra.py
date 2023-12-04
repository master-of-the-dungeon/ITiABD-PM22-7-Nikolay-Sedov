import tkinter as tk
import random

# Основные параметры игры
WIDTH, HEIGHT = 600, 400
BULLET_SPEED = 10
PLAYER_LIVES = 3

# Параметры врагов
ENEMY_ROWS = 3
ENEMY_COLUMNS = 10
ENEMY_HORIZONTAL_SPACING = 50
ENEMY_VERTICAL_SPACING = 40
ENEMY_SPEED = 5
ENEMY_DIRECTION = 1  # 1 - движение вправо, -1 - движение влево

# Инициализация Tkinter
root = tk.Tk()
root.title("Space Invaders")
canvas = tk.Canvas(root, bg='black', width=WIDTH, height=HEIGHT)
canvas.pack()

# Игрок
player = canvas.create_rectangle(WIDTH/2-15, HEIGHT-30, WIDTH/2+15, HEIGHT-10, fill='blue')
player_lives = PLAYER_LIVES
score = 0

# Враги и снаряды
enemies = []
bullets = []

# Создание врагов в формации
for row in range(ENEMY_ROWS):
    for col in range(ENEMY_COLUMNS):
        x = col * ENEMY_HORIZONTAL_SPACING + 30
        y = row * ENEMY_VERTICAL_SPACING + 30
        enemy = canvas.create_rectangle(x, y, x+20, y+20, fill='red')
        enemies.append(enemy)

# Счетчик жизней и очков
lives_text = canvas.create_text(50, 10, text=f"Lives: {player_lives}", fill="white", font=('Helvetica', 12))
score_text = canvas.create_text(WIDTH - 50, 10, text=f"Score: {score}", fill="white", font=('Helvetica', 12))

# Функция для обновления позиции игрока
def move_player(event):
    x, y = canvas.coords(player)[:2]
    if event.keysym == 'Left' and x > 0:
        canvas.move(player, -10, 0)
    elif event.keysym == 'Right' and x < WIDTH - 30:
        canvas.move(player, 10, 0)
    elif event.keysym == 'space':
        fire_bullet()

# Функция для стрельбы
def fire_bullet():
    x1, y1, x2, y2 = canvas.coords(player)
    bullet_x = (x1 + x2) / 2
    bullet_y = y1
    bullet = canvas.create_rectangle(bullet_x-3, bullet_y-10, bullet_x+3, bullet_y, fill='yellow')
    bullets.append(bullet)

# Обновление счетчика жизней и очков
def update_lives():
    global player_lives
    canvas.itemconfig(lives_text, text=f"Lives: {player_lives}")

def update_score():
    global score
    canvas.itemconfig(score_text, text=f"Score: {score}")

# Проверка столкновений
def check_collisions():
    global score, player_lives
    for bullet in bullets.copy():
        bullet_coords = canvas.coords(bullet)
        if not bullet_coords:
            bullets.remove(bullet)
            continue
        bx1, by1, bx2, by2 = bullet_coords
        bx = (bx1 + bx2) / 2
        by = by1

        for enemy in enemies.copy():
            ex, ey, ex2, ey2 = canvas.coords(enemy)
            if bx > ex and bx < ex2 and by > ey and by < ey2:
                canvas.delete(enemy)
                canvas.delete(bullet)
                enemies.remove(enemy)
                bullets.remove(bullet)
                score += 10
                update_score()
                break

    for enemy in enemies.copy():
        ex, ey, ex2, ey2 = canvas.coords(enemy)
        px, py, px2, py2 = canvas.coords(player)
        if ex < px2 and ex2 > px and ey2 > py:
            player_lives -= 1
            canvas.delete(enemy)
            enemies.remove(enemy)
            update_lives()
            if player_lives == 0:
                game_over()
                return
        
        # Проверка касания врагом земли
        if ey2 >= HEIGHT:
            canvas.delete(enemy)
            enemies.remove(enemy)
            player_lives -= 1
            update_lives()
            if player_lives == 0:
                game_over()
                return

# Игра окончена
def game_over():
    canvas.create_text(WIDTH/2, HEIGHT/2, text="GAME OVER", fill="white", font=('Helvetica', 30))
    update_game.stop = True

# Обновление движения врагов
def update_enemies():
    global ENEMY_DIRECTION
    right_edge = WIDTH - ENEMY_HORIZONTAL_SPACING
    left_edge = 0
    move_down = False

    for enemy in enemies:
        x1, y1, x2, y2 = canvas.coords(enemy)
        if (x2 > right_edge and ENEMY_DIRECTION > 0) or (x1 < left_edge and ENEMY_DIRECTION < 0):
            ENEMY_DIRECTION *= -1
            move_down = True
            break

    for enemy in enemies:
        if move_down:
            canvas.move(enemy, 0, ENEMY_VERTICAL_SPACING / 2)
        canvas.move(enemy, ENEMY_SPEED * ENEMY_DIRECTION, 0)

# Обновление игры
def update_game():
    if not hasattr(update_game, "stop") or not update_game.stop:
        update_enemies()
        for bullet in bullets:
            canvas.move(bullet, 0, -BULLET_SPEED)
            if canvas.coords(bullet)[1] < 0:
                canvas.delete(bullet)
                bullets.remove(bullet)

        check_collisions()

        root.after(100, update_game)

# Обработка нажатий клавиш
root.bind("<Left>", move_player)
root.bind("<Right>", move_player)
root.bind("<space>", move_player)

# Начало игрового цикла
update_game()

# Запуск Tkinter
root.mainloop()
