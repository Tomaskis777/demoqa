import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Моя первая игра")
pygame.draw.circle(screen, (255, 0, 0), (400, 300), 50, 3)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            pygame.display.flip()

pygame.quit()


for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            running = False


color = (255, 0, 0)
pygame.draw.rect(screen, color, (50, 50, 100, 100))


clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

screen.fill((0, 0, 0))
pygame.draw.rect(screen, color, (50, 50, 100, 100))

pygame.display.flip()
clock.tick(60)

pygame.quit()

pygame.draw.line(screen, (255, 255, 255), (0, 0), (100, 100), 5)

