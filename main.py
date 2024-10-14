import time
import pygame
import random

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/Яблоко.png")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/Яблоко.png")
target_width = 150
target_height = 158

score = 0

target_x = random.randint(0, screen_width - target_width)
target_y = random.randint(0, screen_height - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running = True
while running:
    screen.fill(color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                score = score + 1
                target_x = random.randint(0, screen_width - target_width)
                target_y = random.randint(0, screen_height - target_height)
    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()


pygame.display.set_caption(f"Вы попали: {score} раз")
time.sleep(5)
pygame.quit()

#Удаляем последний commit
