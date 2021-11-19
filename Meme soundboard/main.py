import pygame
import random
screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("random sound wowoowowwowo")
pygame.init()
font = pygame.font.Font("freesansbold.ttf",40)
welcome_text = font.render("Welcome To The Game",True,(255,255,255))
play_text = font.render("Play",True,(0,0,222))
click_me_text = font.render(str("Click Me"),True,(0,0,0))
sound = pygame.mixer.Sound('Anime_wow_sound_effect(256k).mp3')
icon = pygame.image.load("wow.png")
pygame.display.set_icon(icon)
sound2 = pygame.mixer.Sound('DUN DUN DUUUUN Sound Effect.mp3')
sound3 = pygame.mixer.Sound('FAIL.mp3')


button = pygame.draw.rect(screen, (0, 255, 255), pygame.Rect(350, 400, 125, 75))

def start_screen():
    screen.fill((100, 100, 100))
    screen.blit(welcome_text,(175,100))
    button = pygame.draw.rect(screen, (0, 255, 255), pygame.Rect(350, 400, 125, 75))
    screen.blit(play_text,(371,415))

button_to_click_x = 369
button_to_click_y = 400



running = True
start_screen()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button.collidepoint(mouse_pos):
                screen.fill((255,255,255))
                button_to_click = pygame.draw.rect(screen,(255,0,0),pygame.Rect(button_to_click_x,button_to_click_y,100,100))
                screen.blit(click_me_text,(333,150))

                if button_to_click.collidepoint(mouse_pos):
                    random_int = random.randint(1, 4)
                    if random_int == 1:
                        sound.play()
                    if random_int == 2:
                        sound2.play()
                    if random_int == 3:
                        sound3.play()

                    print("button_to_click has been clicked")


    pygame.display.flip()


