import pygame
pygame.init()


def draw_white_circle(screen, center, radius):
    white = (255, 255, 255)
    pygame.draw.circle(screen, white, center, radius)


def draw_black_circle(screen, center, radius):
    black = (0, 0, 0)
    pygame.draw.circle(screen, black, center, radius)


def draw_square(screen, size, position):
    black = (0, 0, 0)
    pygame.draw.rect(screen, black, (position, size))


def draw_hand(surface, position, width, height, skin_color):
    pygame.draw.rect(surface, skin_color, (*position, width, height))


def draw_fingers(surface, position, skin_color):
    finger_positions = [
        (position[0] + 5, position[1] - 50, 10, 50),  # Палец 1
        (position[0] + 20, position[1] - 70, 10, 70),  # Палец 2
        (position[0] + 35, position[1] - 50, 10, 50),  # Палец 3
        (position[0] + 45, position[1] - 40, 10, 40),  # Палец 4
        (position[0] + 5, position[1] + 150, 10, 30)  # Большой палец
    ]

    for finger in finger_positions:
        pygame.draw.rect(surface, skin_color, finger)
        pygame.draw.rect(surface, (0, 0, 0), finger, 1)  # Черная обводка


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

# Изменение длины и ширины руки
hand_width = 50
hand_height = 150
skin_color = (255, 255, 255)

hand_surface = pygame.Surface((hand_width, hand_height), pygame.SRCALPHA)
fingers_surface = pygame.Surface((hand_width, hand_height), pygame.SRCALPHA)

hand_position = [0, 0]
fingers_position = [0, -50]  # Сдвигаем пальцы вверх, чтобы они располагались выше ладони

draw_hand(hand_surface, hand_position, hand_width, hand_height, skin_color)
draw_fingers(fingers_surface, fingers_position, skin_color)

angle = 0
angle_speed = 2  # Скорость поворота
center_position = [550, 400]

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Моя первая игра")

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

    angle += angle_speed
    if angle >= 95 or angle <= 0:
        angle_speed = -angle_speed

    rotated_hand_surface = pygame.transform.rotate(hand_surface, angle)
    rotated_hand_rect = rotated_hand_surface.get_rect(center=(310, 370))

    rotated_fingers_surface = pygame.transform.rotate(fingers_surface, angle)
    rotated_fingers_rect = rotated_fingers_surface.get_rect(center=(310, 370))

    screen.blit(rotated_hand_surface, rotated_hand_rect)
    screen.blit(rotated_fingers_surface, rotated_fingers_rect)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
