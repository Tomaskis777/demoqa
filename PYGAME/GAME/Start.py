import pygame
import time

pygame.init()


def draw_white_circle(screen, center, radius): #туловище снеговика
    white = (255, 255, 255)
    pygame.draw.circle(screen, white, center, radius)


def draw_black_circle(screen, center, radius): #глаза
    black = (0, 0, 0)
    pygame.draw.circle(screen, black, center, radius)


def draw_square(screen, size, position): #цилиндр на голове
    black = (0, 0, 0)
    pygame.draw.rect(screen, black, (position, size))


def draw_hand(surface, position, width, height, skin_color): #рука
    pygame.draw.rect(surface, skin_color, (*position, width, height,))

    finger_positions = [
        (position[0] + -1, position[1] - 15, 5, 40),  # мизинец
        (position[0] + 8, position[1] - 20, 7, 50),  # безымянный
        (position[0] + 19, position[1] - 32, 8, 40),  # средний
        (position[0] + 41, position[1] - 10, 8, 30),  # большой
        (position[0] + 30, position[1] - 24, 8, 30)    # указательный
    ]

    for finger in finger_positions:
        pygame.draw.rect(surface, skin_color, finger)


def draw_speech_bubble(screen, position, text, font, text_color, bg_color): #облачко с приветствием
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect()
    bubble_rect = pygame.Rect(position[0], position[1], text_rect.width + 55, text_rect.height + 30)
    pygame.draw.rect(screen, bg_color, bubble_rect, border_radius=18)
    screen.blit(text_surface, (bubble_rect.x + 30, bubble_rect.y + 17))


def update_position(objects, min_x, max_x, min_y, max_y):
    for obj in objects:
        obj['center'][0] += obj['speed_x']
        obj['center'][1] += obj['speed_y']

        if obj['center'][0] > max_x - obj["radius"] or obj['center'][0] < min_x + obj["radius"]:
            obj["speed_x"] = -obj["speed_x"]
        if obj['center'][1] > max_y - obj["radius"] or obj['center'][1] < min_y + obj["radius"]:
            obj["speed_y"] = -obj["speed_y"]


circles = [
    {"center": (400, 200), "radius": 50},
    {"center": (400, 300), "radius": 70},
    {"center": (400, 420), "radius": 90}
]

left_circles = [
     {"center": [379, 200], "radius": 10, "speed_x": 0.01, "speed_y": 0},
]

right_circles = [
     {"center": [415, 200], "radius": 10, "speed_x": 0.01, "speed_y": 0},
]

squares = [
    {"position": (60, 85), "size": (370, 75)},
]

hand_width = 42
hand_height = 240

hand_position = [25, 50]
skin_color = (255, 255, 255)
hand_surface = pygame.Surface((100, 240), pygame.SRCALPHA)
draw_hand(hand_surface, hand_position, hand_width, hand_height, skin_color)

angle = 40  # Угол начала движения руки
angle_speed = 0.04  # Скорость поворота
center_position = [550, 400]

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Моя первая игра")

# Настройка шрифта для облачка
font = pygame.font.Font(None, 45)  # Вы можете изменить размер шрифта по необходимости

show_bubble = False
bubble_displayed = False
second_bubble_displayed = False  # Флаг для отслеживания второго облачка
bubble_interval = 3.72
bubble_display_duration = 2  # Длительность отображения облачка в секундах
bubble_appear_time = time.time() + bubble_interval
bubble_disappear_time = None

second_bubble_display_duration = 3  # Длительность отображения второго облачка в секундах
second_bubble_appear_time = None
second_bubble_disappear_time = None
stop_movement = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 255))

    for circle in circles:
        draw_white_circle(screen, circle["center"], circle["radius"])

    for circle in left_circles:
        draw_black_circle(screen, circle["center"], circle["radius"])

    update_position(left_circles, 369, 400, 150, 300)

    for circle in right_circles:
        draw_black_circle(screen, circle["center"], circle["radius"])

    update_position(right_circles, 405, 436, 150, 300)

    for rect in squares:
        draw_square(screen, rect["position"], rect["size"])

    if not stop_movement:
        update_position(left_circles, 369, 400, 150, 300)
        update_position(right_circles, 405, 436, 150, 300)

        angle += angle_speed
        if angle >= 80 or angle <= 38:
            angle_speed = -angle_speed

        rotated_hand_surface = pygame.transform.rotate(hand_surface, angle)
        rotated_hand_rect = rotated_hand_surface.get_rect(midbottom=(335, 370))

        screen.blit(rotated_hand_surface, rotated_hand_rect)

    else:
        rotated_hand_surface = pygame.transform.rotate(hand_surface, angle)
        rotated_hand_rect = rotated_hand_surface.get_rect(midbottom=(335, 445))
        screen.blit(rotated_hand_surface, rotated_hand_rect)
        angle = 120

    current_time = time.time()
    if current_time >= bubble_appear_time and not bubble_displayed:
        show_bubble = True
        stop_movement = True
        bubble_displayed = True
        bubble_disappear_time = current_time + bubble_display_duration
        for circle in left_circles:
            circle['speed_x'] = 0
            circle['speed_y'] = 0
        for circle in right_circles:
            circle['speed_x'] = 0
            circle['speed_y'] = 0
        last_bubble_time = current_time

    if show_bubble:
        draw_speech_bubble(screen, (475, 185), "'Привет!'", font, (0, 0, 0), (255, 255, 255))
        if current_time >= bubble_disappear_time:
            show_bubble = False
            second_bubble_appear_time = current_time + 1  # Задаем время появления второго облачка через 1 секунду

    # Проверка времени появления второго облачка
    if second_bubble_appear_time and current_time >= second_bubble_appear_time and not second_bubble_displayed:
        second_bubble_displayed = True
        second_bubble_disappear_time = current_time + second_bubble_display_duration

    # Отрисовка второго облачка с текстом "HELLO" для ответа
    if second_bubble_displayed:
        draw_speech_bubble(screen, (475, 185), "' '", font, (0, 0, 0), (255, 255, 255))
        if current_time >= second_bubble_disappear_time:
            second_bubble_displayed = False

    pygame.display.flip()

pygame.quit()
