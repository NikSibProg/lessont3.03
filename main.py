import pygame
import random

pygame.init()

# Параметры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра тир")
icon = pygame.image.load("img/maxresdefault.jpg")
pygame.display.set_icon(icon)

# Загрузка изображений
target_img = pygame.image.load("img/target.png")
target_width = 50
target_height = 50
cursor_img = pygame.image.load("img/cursor.png")  # Добавляем изображение курсора

# Инициализация переменных для цели
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
target_speed_x = random.choice([-3, 3])  # Скорость по x
target_speed_y = random.choice([-3, 3])  # Скорость по y

# Цвет фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Шрифт для вывода текста (счет очков)
font = pygame.font.SysFont('Arial', 36)
score = 0  # Переменная для подсчета очков

# Основной игровой цикл
running = True
while running:
    screen.fill(color)

    # Обрабатываем события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Исправлено
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Исправлено условие проверки попадания по цели
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                score += 1  # Увеличиваем счет при попадании по цели
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                target_speed_x = random.choice([-1, 1])  # Перемещаем цель случайно
                target_speed_y = random.choice([-1, 1])

    # Двигаем цель
    target_x += target_speed_x
    target_y += target_speed_y

    # Проверяем столкновение с границами экрана
    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        target_speed_x = -target_speed_x
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        target_speed_y = -target_speed_y

    # Отображаем цель
    screen.blit(target_img, (target_x, target_y))

    # Отображаем курсор мыши
    mouse_x, mouse_y = pygame.mouse.get_pos()
    screen.blit(cursor_img, (mouse_x - cursor_img.get_width() // 2, mouse_y - cursor_img.get_height() // 2))

    # Выводим счет на экран
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
