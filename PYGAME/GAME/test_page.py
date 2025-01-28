import pygame
import sys

def draw_hand(screen, position):
    # Цвета
    skin_color = (255, 224, 189)
    black = (0, 0, 0)

    # Ладонь
    pygame.draw.rect(screen, skin_color, (*position, 50, 100))

    # Пальцы
    finger_positions = [
        (position[0] + 5, position[1] - 20, 10, 40),
        (position[0] + 20, position[1] - 30, 10, 50),
        (position[0] + 35, position[1] - 20, 10, 40),
        (position[0] + 45, position[1] - 10, 10, 30),
        (position[0] + 5, position[1] + 100, 10, 30)
    ]
    for finger in finger_positions:
        pygame.draw.rect(screen, skin_color, finger)

    # Черные контуры для пальцев
    for finger in finger_positions:
        pygame.draw.rect(screen, black, finger, 1)

    # Контур ладони
    pygame.draw.rect(screen, black, (*position, 50, 100), 1)

def update_position(position, speed, screen_size):
    position[0] += speed[0]
    position[1] += speed[1]

    # Проверка столкновений с краями экрана
    if position[0] < 0 or position[0] + 50 > screen_size[0]:
        speed[0] = -speed[0]
    if position[1] < 0 or position[1] + 100 > screen_size[1]:
        speed[1] = -speed[1]

    return position, speed

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Анимация руки")

position = [200, 200]
speed = [2, 2]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 255))

    # Обновление позиции руки
    position, speed = update_position(position, speed, screen.get_size())

    # Рисование руки
    draw_hand(screen, position)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
