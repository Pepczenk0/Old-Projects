import pygame
from random import randint
import time
blue = (0,0,255)
black = (0, 0, 0)
screen = pygame.display.set_mode((800,600))
pygame.init()
title = pygame.display.set_caption("Number Generator")

icon_load = pygame.image.load("mouse.png")
icon = pygame.display.set_icon(icon_load)
screen.fill((255, 255, 255))
rect = pygame.draw.rect(screen, blue, pygame.Rect(360, 375, 60, 60))
running = True
font = pygame.font.Font('Freshman.ttf', 40)
new_font = pygame.font.Font('Freshman.ttf', 100)
random_Integer = 0

textX_one = 120
textY_one = 200
textX_two = 10
textY_two = 10
textX_three = 100
textY_three = 100


def show_text(x,y):
    text_one = font.render("Random number Generator!",True,black)
    screen.blit(text_one,(x,y))
def show_text_random_number(x,y):
    text_two = font.render(str(random_Integer),True,black)
    screen.blit(text_two,(x,y))
def button_text():
    text_three = new_font.render("Click me",True,black)
    screen.blit(text_three,(255,255))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_POSITION = pygame.mouse.get_pos()

        if rect.collidepoint(mouse_POSITION):
            random_Integer = randint(0,1000)
            time.sleep(0.3)

            screen.fill((255, 255, 255))
            rect = pygame.draw.rect(screen, blue, pygame.Rect(360, 375, 60, 60))
            show_text(textX_one, textY_one)
            show_text_random_number(textX_two, textY_two)
            button_text()
    pygame.display.flip()

    pygame.display.update()

    show_text(textX_one,textY_one)
    show_text_random_number(textX_two,textY_two)
    button_text()