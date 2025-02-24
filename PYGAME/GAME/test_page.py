import pygame
import threading
import time
import random

pygame.init()

# Переменные для управления облачками
second_bubble_displayed = False
third_bubble_displayed = False
input_text = ""
input_active = False
second_bubble_shown_once = False
third_bubble_shown_once = False
guessing_game_active = False
correct_number = random.randint(1, 5)


def draw_white_circle(screen, center, radius): #туловище снеговика
    white = (255, 255, 255)
    pygame.draw.circle(screen, white, center, radius)


def draw_black_circle(screen, center, radius): #глаза
    black = (0, 0, 0)
    pygame.draw.circle(screen, black, center, radius)


def draw_square(screen, size, position):  #цилиндр на голове
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


def draw_speech_bubble(screen, position, text, font, text_color, bg_color):  #облачко с приветствием
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


def show_second_bubble():
    global second_bubble_displayed, input_active, second_bubble_shown_once
    second_bubble_displayed = True
    input_active = True
    second_bubble_shown_once = True  # Устанавливаем флаг, что облачко уже было показано
    # threading.Timer(5.0, hide_second_bubble).start()  # Таймер для скрытия облачка через 5 секунд


def hide_second_bubble():
    global second_bubble_displayed, input_active, input_text, third_bubble_appear_time
    second_bubble_displayed = False
    input_active = False
    input_text = ""  # Сбрасываем введенный текст
    # third_bubble_appear_time = time.time() + 3  # Задаем время появления третьего облачка через 2 секунды


def show_third_bubble():
    global third_bubble_displayed, input_active, third_bubble_shown_once
    third_bubble_displayed = True
    input_active = True  # Отключаем ввод текста пользователем
    third_bubble_shown_once = True  # Устанавливаем флаг, что облачко уже было показано
    # threading.Timer(4.0, hide_third_bubble).start()  # Таймер для скрытия облачка через 2 секунды


def hide_third_bubble():
    global third_bubble_displayed, input_active, input_text, guess_number_bubble_appear_time
    third_bubble_displayed = False
    input_active = False
    input_text = ""  # Сбрасываем введенный текст
    # guess_number_bubble_appear_time = time.time() + 4  # Пауза перед началом игры "Угадай число"


def show_guess_number_bubble():
    global guess_number_bubble_displayed, input_active
    guess_number_bubble_displayed = True
    input_active = True


def hide_guess_number_bubble():
    global guess_number_bubble_displayed, input_active, input_text
    guess_number_bubble_displayed = False
    input_active = False
    input_text = ""  # Сбрасываем введенный текст


# def check_guess():
#     global guess_number_bubble_displayed, input_active, input_text
#     if input_text.isdigit():
#         if int(input_text) == correct_number:
#             hide_guess_number_bubble()
#             draw_speech_bubble(screen, (350, 200), "Вы победили! Продолжить?", font, (0, 0, 0), (255, 255, 255))
#         else:
#             hide_guess_number_bubble()
#             draw_speech_bubble(screen, (350, 200), "Ответ неверный, продолжить игру?", font, (0, 0, 0), (255, 255, 255))


def check_guess(correct):
    global guess_number_bubble_displayed, input_active, input_text
    if correct:
        guess_number_bubble_displayed = False
        input_active = False
        input_text = ""
        draw_speech_bubble(screen, (350, 200), "Вы победили! Продолжить?", font, (0, 0, 0), (255, 255, 255))
    else:
        guess_number_bubble_displayed = False
        input_active = False
        input_text = ""
        draw_speech_bubble(screen, (350, 200), "Ответ неверный, продолжить игру?", font, (0, 0, 0), (255, 255, 255))


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
font = pygame.font.Font(None, 45)

show_bubble = False
bubble_displayed = False
bubble_interval = 3.72
bubble_display_duration = 2  # Длительность отображения облачка в секундах
bubble_appear_time = time.time() + bubble_interval
bubble_disappear_time = None

second_bubble_appear_time = None
third_bubble_appear_time = float('inf')  # Инициализируем значение
guess_number_bubble_appear_time = float('inf')  # Инициализируем значение

stop_movement = False
# number_to_guess = 3  # Загаданное число

guess_number_bubble_displayed = False  #Переменная для управления облачком угадывания числа


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if input_active:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode
                if guess_number_bubble_displayed and event.key == pygame.K_RETURN:
                    input_active = False
                    threading.Timer(2.0, check_guess).start()  # Пауза перед проверкой числа

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

    if show_bubble:
        draw_speech_bubble(screen, (475, 185), "Привет", font, (0, 0, 0), (255, 255, 255))
        if current_time >= bubble_disappear_time:
            show_bubble = False
            second_bubble_appear_time = current_time + 1  # Задаем время появления второго облачка через 1 секунду

    if second_bubble_appear_time and current_time >= second_bubble_appear_time and not second_bubble_shown_once:
        show_second_bubble()  # Показ второго облачка и установка таймера

    if second_bubble_displayed:
        draw_speech_bubble(screen, (190, 520), "Введите приветствие: " + input_text, font, (0, 0, 0), (255, 255, 255))
        if input_text.lower() == "привет":
            input_text = ""
            second_bubble_displayed = False
            input_active = False
            show_third_bubble()
        elif input_text.lower() == "нет":
            running = False

    if third_bubble_appear_time and current_time >= third_bubble_appear_time and not third_bubble_shown_once:
        show_third_bubble()  # Показ третьего облачка и установка таймера

    if third_bubble_displayed:
        draw_speech_bubble(screen, (100, 520), "Хотите сыграть в игру 'Угадай число'?: " + input_text, font, (0, 0, 0), (255, 255, 255))
        if input_text.lower() == "да":
            input_text = ""
            third_bubble_displayed = False
            input_active = False  # Активируем ввод текста пользователем
            show_guess_number_bubble()
        elif input_text.lower() == "нет":
            running = False

    if guess_number_bubble_displayed:
        draw_speech_bubble(screen, (190, 520), "Угадайте число: " + input_text, font, (0, 0, 0), (255, 255, 255))
        if input_text.isdigit():
            if int(input_text) == correct_number:
                threading.Timer(2.0, lambda: check_guess(True)).start()
            else:
                threading.Timer(2.0, lambda: check_guess(False)).start()

    pygame.display.flip()

pygame.quit()
