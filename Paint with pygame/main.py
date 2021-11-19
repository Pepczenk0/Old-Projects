import pygame




pygame.init()


def technical():
    pygame.display.set_caption("Drawlie")
    icon = pygame.image.load("color-wheel.png")
    pygame.display.set_icon(icon)
def text_for_panel():
    font = pygame.font.Font("BebasNeue-Regular.ttf", 50)
    text = font.render("Colors",True,(255,255,255))
    display.blit(text,(22,10))
def panel():
    panel = pygame.draw.rect(display,(0,0,0),pygame.Rect(0,0,150,600))
def panel_for_bottem():
    panel = pygame.draw.rect(display,(0,0,0),pygame.Rect(150,475,700,600))

def white_screen():
    display.fill((255,255,255))
def reset_text():
    font = pygame.font.Font("BebasNeue-Regular.ttf", 45)
    text = font.render("Reset",True,(186,85,211))
    display.blit(text,(37,512))
def text_for_change_to_circle():
    font = pygame.font.Font("BebasNeue-Regular.ttf", 40)
    text = font.render("Circle",True,(0,255,127))
    display.blit(text,(670,515))
def text_for_change_to_square():
    font = pygame.font.Font("BebasNeue-Regular.ttf", 40)
    text = font.render("Square",True,(0, 0, 128))
    display.blit(text,(525,515))
def start_screen():
    display.fill((70,130,180))
    font = pygame.font.Font("Scratch Boys.ttf", 65)
    font2 = pygame.font.Font("Scratch Boys.ttf", 90)
    text = font2.render("Welcome to Drawlie!",True,(210,105,30))
    text2 = font.render("Press -> to Quit",True,(220,20,60))
    text4 = font.render("Play",True,(255,255,255))
    play_button = pygame.draw.rect(display, (0, 0, 0), pygame.Rect(200, 400, 400, 100))
    display.blit(text,(50,50))
    display.blit(text2,(200,500))
    display.blit(text4,(350,410))
def text_for_change_buttons():
    font = pygame.font.Font("BebasNeue-Regular.ttf",50)
    text = font.render("Buttons For Size",True,(255,255,255))
    display.blit(text,(190,550))


display = pygame.display.set_mode((800,600))
technical()











white_screen()
play_button = pygame.draw.rect(display,(0,0,0),pygame.Rect(200,400,400,100))


def main():
    global size
    global color
    global choice
    size = 15
    color = (255,255,255)
    choice = 0
    main_menu = True
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    running = False


            if main_menu != True:
                panel()
                panel_for_bottem()
                text_for_panel()
                text_for_change_buttons()
                size_change_button_1 = pygame.draw.rect(display,(255,255,255),pygame.Rect(150,500,25,50))
                size_change_button = pygame.draw.rect(display,(255,255,255),pygame.Rect(190,500,25,50))
                size_change_button2 = pygame.draw.rect(display,(255,255,255),pygame.Rect(230,500,25,50))
                size_change_button3 = pygame.draw.rect(display,(255,255,255),pygame.Rect(270,500,25,50))
                size_change_button4 = pygame.draw.rect(display,(255,255,255),pygame.Rect(310,500,25,50))
                size_change_button5 = pygame.draw.rect(display,(255,255,255),pygame.Rect(350,500,25,50))
                size_change_button6 = pygame.draw.rect(display,(255,255,255),pygame.Rect(390,500,25,50))
                size_change_button7 = pygame.draw.rect(display,(255,255,255),pygame.Rect(430,500,25,50))
                size_change_button8 = pygame.draw.rect(display,(255,255,255),pygame.Rect(470,500,25,50))

                change_shape_for_square = pygame.draw.rect(display,(0,206,209),pygame.Rect(510,500,125,75))
                change_shape_for_circle = pygame.draw.rect(display, (25,25,112), pygame.Rect(650, 500, 125, 75))
                change_cyan_button = pygame.draw.rect(display,(0,255,255),pygame.Rect(40,445,75,40))
                change_yellow_button = pygame.draw.rect(display,(255,255,0),pygame.Rect(40,300,75,40))
                change_erase_white = pygame.draw.rect(display, (255, 255, 255), pygame.Rect(40, 150, 75, 40))
                change_blue_button = pygame.draw.rect(display, (0, 0, 255), pygame.Rect(40, 75, 75, 40))
                change_green_button = pygame.draw.rect(display, (100, 255, 0), pygame.Rect(40, 225, 75, 40))
                change_red_button = pygame.draw.rect(display, (233, 0, 0), pygame.Rect(40, 375, 75, 40))
                reset_button = pygame.draw.rect(display, (255, 255, 255), (25, 500, 105, 75))
                reset_text()
                text_for_change_to_circle()
                text_for_change_to_square()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    mouse_x = mouse_pos[0]
                    mouse_y = mouse_pos[1]
                    if mouse_x < 150 and mouse_y < 480:
                        pass
                    elif mouse_x > 150 and mouse_y < 475 and choice == 1:
                        circle = pygame.draw.circle(display, color, (mouse_x, mouse_y), size, size)
                    elif mouse_x > 150 and mouse_y < 475 and choice == 2:
                        rect = pygame.draw.rect(display, color, pygame.Rect(mouse_x, mouse_y, size, size))


                    if reset_button.collidepoint(mouse_pos):
                        white_screen()
                        panel()
                        text_for_panel()
                        panel_for_bottem()
                        size_change_button_1 = pygame.draw.rect(display, (255, 255, 255), pygame.Rect(150, 500, 25, 50))
                        size_change_button = pygame.draw.rect(display, (255, 255, 255), pygame.Rect(190, 500, 25, 50))
                        size_change_button2 = pygame.draw.rect(display, (255, 255, 255), pygame.Rect(230, 500, 25, 50))
                        size_change_button3 = pygame.draw.rect(display, (255, 255, 255), pygame.Rect(270, 500, 25, 50))
                        size_change_button4 = pygame.draw.rect(display, (255, 255, 255), pygame.Rect(310, 500, 25, 50))
                        size_change_button5 = pygame.draw.rect(display, (255, 255, 255), pygame.Rect(350, 500, 25, 50))
                        size_change_button6 = pygame.draw.rect(display, (255, 255, 255), pygame.Rect(390, 500, 25, 50))
                        size_change_button7 = pygame.draw.rect(display, (255, 255, 255), pygame.Rect(430, 500, 25, 50))
                        size_change_button8 = pygame.draw.rect(display, (255, 255, 255), pygame.Rect(470, 500, 25, 50))




                        change_shape_for_square = pygame.draw.rect(display, (0, 206, 209), pygame.Rect(510, 500, 125, 75))
                        change_shape_for_circle = pygame.draw.rect(display, (25, 25, 112), pygame.Rect(650, 500, 125, 75))
                        change_yellow_button = pygame.draw.rect(display, (255, 255, 0),pygame.Rect(40, 300, 75, 40))
                        change_cyan_button = pygame.draw.rect(display, (0, 255, 255),pygame.Rect(40, 445, 75, 40))
                        change_erase_white = pygame.draw.rect(display, (255, 255, 255), pygame.Rect(40, 150, 75, 40))
                        change_blue_button = pygame.draw.rect(display, (0, 0, 255), pygame.Rect(40, 75, 75, 40))
                        change_green_button = pygame.draw.rect(display, (100, 255, 0), pygame.Rect(40, 225, 75, 40))
                        change_red_button = pygame.draw.rect(display, (233, 0, 0), pygame.Rect(40, 375, 75, 40))
                        reset_button = pygame.draw.rect(display, (255, 255, 255), (25, 500, 105, 75))
                        reset_text()
                        text_for_change_to_circle()
                        text_for_change_to_square()
                    if size_change_button8.collidepoint(mouse_pos):
                        print("size 8")
                        size = 80

                    if size_change_button7.collidepoint(mouse_pos):
                        print("size 7")
                        size = 70

                    if size_change_button6.collidepoint(mouse_pos):
                        print("size 6")
                        size = 60

                    if size_change_button5.collidepoint(mouse_pos):
                        print("size 5")

                        size = 50

                    if size_change_button4.collidepoint(mouse_pos):
                        print("size 4")
                        size = 40

                    if size_change_button3.collidepoint(mouse_pos):
                        print("size 3")
                        size = 30


                    if size_change_button2.collidepoint(mouse_pos):
                        print("size 2")
                        size = 20


                    if size_change_button.collidepoint(mouse_pos):
                        print("size 1")
                        size = 10
                    if size_change_button_1.collidepoint(mouse_pos):
                        print("size -1")
                        size = 5


                    if change_shape_for_square.collidepoint(mouse_pos):
                        choice = 2
                        print("change for square")


                    if change_shape_for_circle.collidepoint(mouse_pos):
                        print("change for circle")
                        choice = 1

                    if change_cyan_button.collidepoint(mouse_pos):
                        color = (0,255,255)
                        print("4,cyan")
                        reset_text()
                    if change_yellow_button.collidepoint(mouse_pos):
                        color = (255,255,0)
                        print("-1,yellow")
                    if change_erase_white.collidepoint(mouse_pos):
                        color = (255,255,255)
                        print("0,white(erase)")
                    if change_blue_button.collidepoint(mouse_pos):
                        color = (0,0,255)
                        print("1,blue")
                    if change_green_button.collidepoint(mouse_pos):
                        print("2,green")
                        color = (0, 222, 0)

                    if change_red_button.collidepoint(mouse_pos):
                        print("3,red")
                        color = (255, 0, 0)

            else:


                        start_screen()

                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_pos = pygame.mouse.get_pos()
                            if play_button.collidepoint(mouse_pos):
                                main_menu = False
                                white_screen()

            pygame.display.flip()


main()