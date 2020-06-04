# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 16:25:55 2018

@author: james
"""

import pygame,random,time,sqlite3
 
db = sqlite3.connect('Highscores.db')
                    
Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)

pygame.font.init()
myFont = pygame.font.SysFont("Comic Sans MS",20)
myFont2 = pygame.font.SysFont("Comic Sans MS",30)
myFont3 = pygame.font.SysFont("Comic Sans MS",50)
pygame.init()

screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width,screen_height])

clock = pygame.time.Clock()
clock.tick(60)

time_limit = 10        
        
def main_menu(time_limit):
    def button_check(button_pressed,pressed):
        pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if click[0] == True:
            if pos[0]>250 and pos[0]<410 and pos[1]>150 and pos[1]<210:
                button_pressed = True
                pressed = "play"
            elif pos[0]>250 and pos[0]<410 and pos[1]>250 and pos[1]<310:
                button_pressed = True
                pressed = "options"
            elif pos[0]>250 and pos[0]<410 and pos[1]>350 and pos[1]<410:
                button_pressed = True
                pressed = "highscores"
            elif (pos[0]>(screen_width-130) and pos[0]<(screen_width-30) and pos[1]>(screen_height-85) and pos[1]<(screen_height-35)):
                button_pressed = True
                pressed = "Quit"
            else:
                pressed = None
                button_pressed = False
        else:
            button_pressed = False
            pressed = None
 
        return button_pressed,pressed
 
    
    screen.fill(White)
    
    game_text = myFont3.render("Collect the Ellipsoidz!",False,Red)
    screen.blit(game_text,(100,50))
    
    quit_button = pygame.draw.rect(screen,Black,(screen_width-130,screen_height-85,100,50))
    quit_text = myFont2.render("Quit",False,White)
    screen.blit(quit_text,(screen_width-110,screen_height-85))
    
    play_button = pygame.draw.rect(screen,Black,(250,150,160,60))
    play_text = myFont2.render("Play!",False,White)
    screen.blit(play_text,(300,160))
 
    options_button = pygame.draw.rect(screen,Black,(250,250,160,60))
    options_text = myFont2.render("Options",False,White)
    screen.blit(options_text,(275,260))
 
    highscores_button = pygame.draw.rect(screen,Black,(250,350,160,60))
    highscores_text = myFont2.render("Highscores",False,White)
    screen.blit(highscores_text,(250,360))
    
    pygame.display.flip()
    
    button_pressed = False
    pressed = None
    
    while not button_pressed:
        for event in pygame.event.get():
            button_pressed,pressed = button_check(button_pressed,pressed)
 
    if pressed == "play":
        game(time_limit)
    elif pressed == "options":
        time_limit = options_screen(time_limit)
    elif pressed == "highscores":
        highscores_screen()
    elif pressed == "Quit":
        pygame.quit()
 
def options_screen(time_limit):
    def button_check(button_pressed,pressed):
        pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if click[0] == True:
            if (pos[0]>10 and pos[0]<110 and pos[1]<(screen_height-35) and pos[1]>(screen_height-85)):
                button_pressed = True
                pressed = "Back"
            elif (pos[0]>180 and pos[0]<240 and pos[1]<130 and pos[1]>70):
                  pressed = "Down"
                  return button_pressed,pressed
            elif (pos[0]>460 and pos[0]<520 and pos[1]<130 and pos[1]>70):
                pressed = "Up"
                return button_pressed,pressed
            else:
                button_pressed = False
                pressed = None
        else:
            pressed = None
            button_pressed = False
        return button_pressed,pressed
 
    def display(time_limit):
        screen.fill(White)
        
        back_rect = pygame.draw.rect(screen,White,(10,screen_height-85,100,50))
        back_text = myFont2.render("<- Back",False,Black)
        screen.blit(back_text,(10,screen_height-85))
 
        time_text = myFont2.render("Time Limit:",False,Black)
        time_limit_text = myFont2.render(str(time_limit)+" seconds",False,Black)
        time_rect = pygame.draw.rect(screen,Black,(250,50,200,100),2)
        screen.blit(time_text,(280,60))
        screen.blit(time_limit_text,(280,90))
 
        right_triangle = pygame.draw.polygon(screen,Green,((460,70),(520,100),(460,130)),0)
        left_triangle = pygame.draw.polygon(screen,Red,((240,70),(180,100),(240,130)),0)
        
        pygame.display.flip()
 
    display(time_limit)
 
    time_limits = [1,10,30,60]
    
    button_pressed = False
    pressed = None
    while not button_pressed:
        pos = pygame.mouse.get_pos()
        if (pos[0]>10 and pos[0]<110 and pos[1]<(screen_height-35) and pos[1]>(screen_height-85)):
            pygame.draw.rect(screen,Black,(10,screen_height-85,100,50),1)
            pygame.display.flip()
        else:
            pygame.draw.rect(screen,White,(10,screen_height-85,100,50),1)
            pygame.display.flip()
        for event in pygame.event.get():
            button_pressed,pressed = button_check(button_pressed,pressed)
        if pressed == "Up":
            time.sleep(0.1)
            time_limit = time_limits[time_limits.index(time_limit)-(len(time_limits)-1)]
            display(time_limit)
        if pressed == "Down":
            time.sleep(0.1)
            time_limit = time_limits[time_limits.index(time_limit)-1]
            display(time_limit)
    if pressed == "Back":
        main_menu(time_limit)
 
    return time_limit
 
def highscores_screen():
    def button_check_hs(button_pressed,pressed):
        pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if click[0] == True:
            if (pos[0]>10 and pos[0]<110 and pos[1]<(screen_height-35) and pos[1]>(screen_height-85)):
                button_pressed = True
                pressed = "Back"
            else:
                button_pressed = False
                pressed = None
        else:
            pressed = None
            button_pressed = False
        return button_pressed,pressed
    
    def highscores_display():
        screen.fill(White)
        
        position_text = myFont.render("Position",False,Black)
        screen.blit(position_text,(10,50))
        
        name_text_screen = myFont.render("Name",False,Black)
        screen.blit(name_text_screen,(100,50))
        
        score_text_screen = myFont.render("Score per minute",False,Black)
        screen.blit(score_text_screen,(screen_width-180,50))
        
        back_rect = pygame.draw.rect(screen,White,(10,screen_height-85,100,50))
        back_text = myFont2.render("<- Back",False,Black)
        screen.blit(back_text,(10,screen_height-85))
        
        db = sqlite3.connect('Highscores.db')
        c = db.cursor()
        
        x = 0
        for row in c.execute('SELECT * FROM highscores ORDER BY score DESC'):
            x+=1
            name_bit = row[0]
            score_bit = row[1]
            locals()["name_"+str(x)] = myFont2.render(str(x)+".          "+name_bit,False,Black)
            locals()["score_"+str(x)] = myFont2.render(str(score_bit),False,Black)
            if x == 5:
                break
        
        db.close()
        
        for j in range (1,x+1):
            screen.blit(locals()["name_"+str(j)],(10,100+j*40))
            screen.blit(locals()["score_"+str(j)],(screen_width-100,100+j*40))
        
        pygame.display.flip()
    
    highscores_display()
    
    button_pressed = False
    pressed = None
    while not button_pressed:
        pos = pygame.mouse.get_pos()
        if (pos[0]>10 and pos[0]<110 and pos[1]<(screen_height-35) and pos[1]>(screen_height-85)):
            pygame.draw.rect(screen,Black,(10,screen_height-85,100,50),1)
            pygame.display.flip()
        else:
            pygame.draw.rect(screen,White,(10,screen_height-85,100,50),1)
            pygame.display.flip()
        for event in pygame.event.get():
            button_pressed,pressed = button_check_hs(button_pressed,pressed)
    if pressed == "Back":
        main_menu(time_limit)

def input_name(time_limit,score):

    def gm_display(time_limit,score,name):
        screen.fill(White)
        textSurface2 = myFont3.render("Game Over",False,Red)
        textSurfaceFinal = myFont2.render("Score per minute: "+str(round((score/(time_limit/60)),0)),False,Black)
        screen.blit(textSurface2,(0.5*screen_width-130,0.5*screen_height-180))
        screen.blit(textSurfaceFinal,(0.5*screen_width-170,0.5*screen_height-50))
        back_rect = pygame.draw.rect(screen,Black,(10,screen_height-85,100,50))
        back_text = myFont2.render("<- Back",False,White)
        quit_rect = pygame.draw.rect(screen,Black,(screen_width-130,screen_height-85,100,50))
        quit_text = myFont2.render("Quit",False,White)
        screen.blit(back_text,(10,screen_height-85))
        screen.blit(quit_text,(screen_width-110,screen_height-85))
        input_name_text = myFont2.render("Input name:",False,Black)
        screen.blit(input_name_text,(0.5*screen_width-110,0.5*screen_height+30))
        name_text = myFont2.render("".join(name),False,Black)
        screen.blit(name_text,(0.5*screen_width-110,0.5*screen_height+70))
        pygame.display.flip()
        
    key_pressed = ""
    name = []
    gm_display(time_limit,score,name)
    while key_pressed != "Enter":
        key_pressed = ""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    key_pressed = "Enter"
                    db = sqlite3.connect('Highscores.db')
                    c = db.cursor()
                    c.execute("INSERT INTO highscores VALUES (?,?)",("".join(name),int(round((score/(time_limit/60)),0))))
                    db.commit()
                    db.close()
                    return name
                elif event.key == pygame.K_BACKSPACE:
                    del name[-1]
                    gm_display(time_limit,score,name)
                elif event.unicode.isalpha():
                    name.append(event.unicode)
                    gm_display(time_limit,score,name)
                    
                    
    
def game(time_limit):
    ####################
    class Block(pygame.sprite.Sprite):
        def __init__(self,colour,width,height):
            super(Block,self).__init__()
            self.image = pygame.Surface([width,height])
            self.image.fill(White)
            self.image.set_colorkey(White)
            
            pygame.draw.ellipse(self.image,colour,[0,0,width,height])
            self.rect = self.image.get_rect()
        def update(self):
            self.rect.y += 1
            if self.rect.y>screen_height:
                Block.reset_pos(self)
        def reset_pos(self):
            self.rect.x = random.randint(0,screen_width)
            self.rect.y = random.randint(0,screen_height)
    class Player(Block):
        def update(self):
            pos = pygame.mouse.get_pos()
            self.rect.x = pos[0]
            self.rect.y = pos[1]
    
    def gm_buttons(button_pressed,pressed):
        pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if click[0] == True:
            if (pos[0]>10 and pos[0]<110 and pos[1]<(screen_height-35) and pos[1]>(screen_height-85)):
                button_pressed = True
                pressed = "Back"
            elif (pos[0]>(screen_width-130) and pos[0]<(screen_width-30) and pos[1]>(screen_height-85) and pos[1]<(screen_height-35)):
                button_pressed = True
                pressed = "Quit"
            else:
                button_pressed = False
                pressed = None
        else:
            pressed = None
            button_pressed = False
        return button_pressed,pressed
        
    pygame.init()
 
    screen.fill(White)
    block_list = pygame.sprite.Group()
    all_sprites_list = pygame.sprite.Group()
 
    score = 0
 
    for i in range(50):
        block = Block(Black,20,15)  
        block.rect.x = random.randint(0,screen_width)
        block.rect.y = random.randint(0,screen_height)
        block_list.add(block)
        all_sprites_list.add(block)
    player = Player(Red,20,15)
    all_sprites_list.add(player)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    #####################
    start_time = time.time()
    #####################
    while True:
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        blocks_hit_list = pygame.sprite.spritecollide(player,block_list,True)
        for block in blocks_hit_list:
            score+=1
            block = Block(Black,20,15)
            Block.reset_pos(block)
            block_list.add(block)
            all_sprites_list.add(block)
        screen.fill(White)
        timeRemaining = myFont.render("Time left: "+str(round((time_limit-(time.time()-start_time)),1)),False,Black)
        textSurface = myFont.render("Score: "+str(score),False,Black)
        screen.blit(timeRemaining,(0,0))
        screen.blit(textSurface,(screen_width-150,0))
        all_sprites_list.update()
        all_sprites_list.draw(screen)
        pygame.display.flip()
    ###################
        if int(time.time()-start_time) == int(time_limit):
            button_pressed = False
            pressed = None
            name = input_name(time_limit,score)
            while not button_pressed:
                for event in pygame.event.get():
                    button_pressed,pressed = gm_buttons(button_pressed,pressed)
            if pressed == "Quit":
                pygame.quit()
            elif pressed == "Back":
                main_menu(time_limit)
 
main_menu(time_limit)