import pygame
import sys
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


def update_position(objects):
    for obj in objects:
        obj['center'][0] += obj['speed_x']
        obj['center'][1] += obj['speed_y']

        if obj['center'][0] > 500 - obj["radius"] or obj['center'][0] < obj["radius"]:
            obj["speed_x"] = -obj["speed_x"]
        if obj['center'][1] > 50 - obj["radius"] or obj["center"][1] < obj["radius"]:
            obj["speed_y"] = -obj["speed_y"]


circles = [
    {"center": (400, 200), "radius": 50},
    {"center": (400, 300), "radius": 70},
    {"center": (400, 420), "radius": 90}
]

circles2 = [
     {"center": [379, 200], "radius": 10, "speed_x": 1, "speed_y": 0},
     {"center": [420, 200], "radius": 10, "speed_x": 1, "speed_y": 0}
]

squares = [
    {"position": (60, 85), "size": (370, 75)},
]

pygame.init()

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

    for circle in circles2:
        draw_black_circle(screen, circle["center"], circle["radius"])

    update_position(circles2)

    for rect in squares:
        draw_square(screen, rect["position"], rect["size"])

    pygame.display.flip()

pygame.quit()




