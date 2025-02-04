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


def draw_hand(surface, position, skin_color):
    pygame.draw.rect(surface, skin_color, (*position, 50, 100))

    finger_positions = [
        (position[0] + 5, position[1] - 20, 10, 40),
        (position[0] + 20, position[1] - 30, 10, 50),
        (position[0] + 35, position[1] - 20, 10, 40),
        (position[0] + 45, position[1] - 10, 10, 30),
        (position[0] + 5, position[1] + 100, 10, 30)
    ]

    for finger in finger_positions:
        pygame.draw.rect(surface, skin_color, finger)


def update_position(objects, min_x, max_x, min_y, max_y):
    for obj in objects:
        obj['center'][0] += obj['speed_x']
        obj['center'][1] += obj['speed_y']

        if obj['center'][0] > max_x - obj["radius"] or obj['center'][0] < min_x + obj["radius"]:
            obj["speed_x"] = -obj["speed_x"]
        if obj['center'][1] > max_y - obj["radius"] or obj["center"][1] < min_y + obj["radius"]:
            obj["speed_y"] = -obj["speed_y"]


# min_x, max_x = 20, 700
# min_y, max_y = 50, 550

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

hand_position = [25, 50]
skin_color = (255, 255, 255)
hand_surface = pygame.Surface((100, 150), pygame.SRCALPHA)
draw_hand(hand_surface, hand_position, skin_color)


angle = 0
angle_speed = 0.050  # Скорость поворота
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
    if angle >= 90 or angle <= 0:
        angle_speed = -angle_speed

    rotated_hand_surface = pygame.transform.rotate(hand_surface, angle)
    rotated_hand_rect = rotated_hand_surface.get_rect(midbottom=(340, 360))

    # rotated_hand_rect.topright = [175, 140]
    screen.blit(rotated_hand_surface, rotated_hand_rect)

    pygame.display.flip()

pygame.quit()
