import pygame
from random import randint

def instructions():
    print("instructions are as follows")
    print("press play to start and try to get ")
    print("as many points as you can!")
instructions()
score = 0
pygame.init()
bigger_font = pygame.font.Font("milky_nice\MilkyNice.ttf",42)
font = pygame.font.Font("milky_nice\MilkyNice.ttf",34)
pygame.display.set_caption("Reaction Game!")
screen = pygame.display.set_mode((800,600))
def play_text(x,y):
    play_text = font.render(str("Play --->"),True,(255,255,255))
    screen.blit(play_text,(x,y))


x = 369
y = 300
def show_score(x,y):
    score_text = font.render(str(score),True,(255,255,255))
    screen.blit(score_text,(x,y))
def show_welcome_text(x,y):
    welcome_text = bigger_font.render("Welcome to the Game!",True,(255,255,255))
    screen.blit(welcome_text,(x,y))
play_text(600,3)
def show_quit_text(x,y):
    quit_text = font.render("<--- Quit",True,(255,255,255))
    screen.blit(quit_text,(x,y))
button = pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(760, 10, 30,30))
show_welcome_text(160,255)

running = True
clock = pygame.time.Clock()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(60)

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()




        '''GAME START'''
        if button.collidepoint(mouse_pos):
            screen.fill((100, 100, 100))
            button_to_click = pygame.draw.rect(screen,(200,0,0),pygame.Rect(x,y,50,50))
            print("start")
            quit_button = pygame.draw.rect(screen,(0,255,255),pygame.Rect(10,565,25,25))
            show_quit_text(50,555)
        if quit_button.collidepoint(mouse_pos):
            running = False
        if button_to_click.collidepoint(mouse_pos):
            x = randint(100,500)
            y = randint(100,500)
            score += 1
            screen.fill((100, 100, 100))
            button_to_click = pygame.draw.rect(screen, (200, 0, 0), pygame.Rect(x, y, 50, 50))
            show_score(10,5)
            quit_button = pygame.draw.rect(screen, (0, 255, 255), pygame.Rect(10, 565, 25, 25))
            show_quit_text(50,555)
    pygame.display.flip()

