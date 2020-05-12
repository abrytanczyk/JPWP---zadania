import pygame

pygame.init()

window = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption(" :-) ")
bg = pygame.image.load("background.png")
bg = pygame.transform.scale(bg, (800, 600))

window.blit(bg, (0, 0))
pygame.draw.circle(window, (255, 0, 0), (200, 300), 15)
pygame.draw.circle(window, (255, 255, 255), (400, 500), 10)
pygame.display.update()

x, y = 200, 300

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        window.blit(bg, (0, 0))
        y -= 1
        pygame.draw.circle(window, (255, 0, 0), (x, y), 15)

    if keys[pygame.K_DOWN]:
        window.blit(bg, (0, 0))
        y += 1
        pygame.draw.circle(window, (255, 0, 0), (x, y), 15)

    if keys[pygame.K_RIGHT]:
        window.blit(bg, (0, 0))
        x += 1
        pygame.draw.circle(window, (255, 0, 0), (x, y), 15)

    if keys[pygame.K_LEFT]:
        window.blit(bg, (0, 0))
        x -= 1
        pygame.draw.circle(window, (255, 0, 0), (x, y), 15)

    if 385 <= x <= 415 and 485 <= y <= 515:
        pygame.draw.circle(window, (255, 0, 0), (400, 500), 10)
    else:
        pygame.draw.circle(window, (255, 255, 255), (400, 500), 10)

    pygame.display.update()

pygame.quit()