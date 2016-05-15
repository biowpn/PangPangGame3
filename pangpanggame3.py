import pygame
import time

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
light_red = (255,0,0)
yellow = (230,220,0)
light_yellow = (255,255,0)
green = (34,177,76)
light_green = (0,255,0)
blue = (0,0,255)
chi1 = (0,205,0)
chi2 = (0,155,0)
chi3 = (0,105,0)
chi4 = (0,55,0)


#
# Game Parameters Setup#
#

display_width = 1280
display_height = 720
gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('Pang Pang Game V3.0')

icon = pygame.image.load('bin/icon/icon128.ico')
pygame.display.set_icon(icon)

p1_attdef = []
p1_wt = 0
p2_attdef = []
p2_wt = 0
skill_dur = 3

clock = pygame.time.Clock()
FPS = 50

## Images

welcomeSuf = pygame.image.load('bin/images/welcomesurface.png')
controlsSuf = pygame.image.load('bin/images/controlssurface.png')
p1_selectSuf = pygame.image.load('bin/images/p1_selectsurface.png')
p2_selectSuf = pygame.image.load('bin/images/p2_selectsurface.png')


stage = pygame.image.load('bin/images/battlestage.png')
stage_width = 1000
stage_height = 500
stage_x = (display_width-stage_width)/2
stage_y = (display_height-stage_height)/2

river = pygame.image.load('bin/images/river.png')
river_width = 200
river_x = (display_width-river_width)/2
river_y = (display_height-stage_height)/2

ch1_game = pygame.image.load('bin/images/ch1_game.png')
ch1_large = pygame.image.load('bin/images/ch1_large.png')
ch1_d = pygame.image.load('bin/images/ch1_dscrp.png')
ch2_game = pygame.image.load('bin/images/ch2_game.png')
ch2_large = pygame.image.load('bin/images/ch2_large.png')
ch2_d = pygame.image.load('bin/images/ch2_dscrp.png')
ch3_game = pygame.image.load('bin/images/ch3_game.png')
ch3_large = pygame.image.load('bin/images/ch3_large.png')
ch3_d = pygame.image.load('bin/images/ch3_dscrp.png')

player_width = 40
player_height = 80

chi_ring = pygame.image.load('bin/images/chi_ring.png')

chi_ruler = pygame.image.load('bin/images/chi_ruler.png')

atk1_height = 40
atk1_width = 40
atk1_speed = 750
atk1_damage = 2
Ratk1 = pygame.image.load('bin/images/atk1_toright.png')
Latk1 = pygame.image.load('bin/images/atk1_toleft.png')

atk2_height = 100
atk2_width = 40
atk2_speed = 1000
atk2_damage = 4
Ratk2 = pygame.image.load('bin/images/atk2_toright.png')
Latk2 = pygame.image.load('bin/images/atk2_toleft.png')

atk3_height = 220
atk3_width = 40
atk3_speed = 1200
atk3_damage = 14
Ratk3 = pygame.image.load('bin/images/atk3_toright.png')
Latk3 = pygame.image.load('bin/images/atk3_toleft.png')

atk5_core = pygame.image.load('bin/images/atk5_core.png')
atk5 = pygame.image.load('bin/images/atk5.png')

p1_shield = pygame.image.load('bin/images/p1_shield.png')
p2_shield = pygame.image.load('bin/images/p2_shield.png')
shield_width = player_width/2
shield_height = player_height

rebound = pygame.image.load('bin/images/rebound.png')
rebound_width = player_width/2
rebound_height = player_height

supershield = pygame.image.load('bin/images/supershield.png')

smallfont = pygame.font.Font('bin/fonts/LSANS.TTF', 22)
medfont = pygame.font.Font('bin/fonts/LSANS.TTF', 50)
largefont = pygame.font.Font('bin/fonts/LSANS.TTF', 80)
extralargefont = pygame.font.Font('bin/fonts/LSANS.TTF', 300)

pygame.Surface.convert(ch1_game)
pygame.Surface.convert(ch2_game)
pygame.Surface.convert(ch3_game)

## Sound & Music

def play(filename,t=0):
    fullfilename = "bin/soundtrack/"+filename
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.load(fullfilename)
    pygame.mixer.music.play(t)
def stop():
    pygame.mixer.music.stop()
    
tada = pygame.mixer.Sound('bin/sounds/tada.wav')
Sound_ready = pygame.mixer.Sound('bin/sounds/321.wav')
Sound_go = pygame.mixer.Sound('bin/sounds/go.wav')
Sound_p1_abs = pygame.mixer.Sound('bin/sounds/absorbing.wav')
Sound_p2_abs = pygame.mixer.Sound('bin/sounds/absorbing.wav')
Sound_atk1 = pygame.mixer.Sound('bin/sounds/atk1.wav')
Sound_atk2 = pygame.mixer.Sound('bin/sounds/atk2.wav')
Sound_atk3 = pygame.mixer.Sound('bin/sounds/atk3.wav')
Sound_barrage = pygame.mixer.Sound('bin/sounds/barrage.wav')
Sound_rebound = pygame.mixer.Sound('bin/sounds/rebounding.wav')
Sound_supershield = pygame.mixer.Sound('bin/sounds/supershielding.wav')
Sound_atkcol = pygame.mixer.Sound('bin/sounds/atkcollide.wav')
Sound_atkhit1 = pygame.mixer.Sound('bin/sounds/atkhit(withoutshield).wav')
Sound_atkhit2 = pygame.mixer.Sound('bin/sounds/atkhit(withshield).wav')
Sound_atk5s1 = pygame.mixer.Sound('bin/sounds/atk5_stage1.wav')
Sound_atk5s2 = pygame.mixer.Sound('bin/sounds/atk5_stage2.wav')
Sound_atk5s3 = pygame.mixer.Sound('bin/sounds/atk5_stage3.wav')



#
#Functional Menu#
#


def text_objects(text, color, size):
    if size == 'small':
        textSurface = smallfont.render(text, True, color)
    elif size == 'medium':
        textSurface = medfont.render(text, True, color)
    elif size == 'large':
        textSurface = largefont.render(text, True, color)
    elif size == 'extralarge':
        textSurface = extralargefont.render(text, True, color)        
    return textSurface, textSurface.get_rect()            
def message_to_screen(msg,color, x_displace=0, y_displace=0, size='small'):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width/2)+x_displace, (display_height/2)+y_displace
    gameDisplay.blit(textSurf, textRect)

def text_to_button(msg,color,btnx,btny,btnw,btnh,size='small'):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (btnx+btnw/2, btny+btnh/2)
    gameDisplay.blit(textSurf, textRect)

def button(text,x,y,w,h,inactive_color,active_color, action = None):
    
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > cur[0] > x and y + h > cur[1] > y:            
        pygame.draw.rect(gameDisplay, active_color, (x,y,w,h))
        if click[0] == 1 and action != None:
            if action == 'quit':
                pygame.quit()
                quit()
            elif action == 'controls':
                return (game_controls())
            elif action == 'select_ch':
                return (select_character())
            elif action == 'play':
                return (gameLoop())

    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x,y,w,h))
    text_to_button(text,black,x,y,w,h)
def game_welcome():
    play('town.mid')
    welcome = True
    gameDisplay.blit(welcomeSuf,(0,0))
    message_to_screen('This program is written by MENG Yuan(ymengad@ust.hk)',
                          black,330,-340,'small')
    while welcome:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()        
        
        button("Play",display_width/2-250,600,100,50,green,light_green,'select_ch')
        button("Controls",display_width/2-50,600,100,50,yellow,light_yellow,'controls')
        button("Quit",display_width/2+150,600,100,50,red,light_red, 'quit')
        
        pygame.display.update()
        clock.tick(FPS)
    welcome = False

def game_controls():
    controls = True
    gameDisplay.blit(controlsSuf,(0,0))
    while controls:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()        
        
        button("Play",display_width/2-200,600,100,50,green,light_green,'select_ch')
        button("Quit",display_width/2+100,600,100,50,red,light_red, 'quit')
        
        pygame.display.update()
        clock.tick(FPS)
    controls = False


def select_character():
    global p1_attdef, p2_attdef
    time.sleep(0.5) 
    p1_attdef = character(1)
    time.sleep(0.5) 
    p2_attdef = character(2)
    time.sleep(0.5) 
    return (gameLoop())


def character(playercode):
    select = True
    x,y,w,h=display_width/2-180,180,360,450                 
    if playercode == 1:
        gameDisplay.blit(p1_selectSuf,(0,0))
    elif playercode == 2:
        gameDisplay.blit(p2_selectSuf,(0,0))

    while select:        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("",x-420,y,w,h,black,white,None)
        gameDisplay.blit(ch1_large,(x-415,y+5))
        gameDisplay.blit(ch1_d,(x-450,y+455))
        
        button("",x,y,w,h,black,white,None)
        gameDisplay.blit(ch2_large,(x+5,y+5))
        gameDisplay.blit(ch2_d,(x+15,y+455))
        
        button("",x+420,y,w,h,black,white,None)
        gameDisplay.blit(ch3_large,(x+425,y+5))
        gameDisplay.blit(ch3_d,(x+370,y+455))
        
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        # defatt = [character, speed,absorbing_rate,atkchi_discount,DFI,special_skill]
        
        if x-420 + w > cur[0] > x-420 and y + h > cur[1] > y:
            if click[0] == 1:
                return [ch1_game, 6.5, 1, 0.8, 0.9, 'barrage']
        if x + w > cur[0] > x and y + h > cur[1] > y:
            if click[0] == 1:
                return [ch2_game, 6, 1, 1, 1, 'rebound']
        if x+420 + w > cur[0] > x+420 and y + h > cur[1] > y:
            if click[0] == 1:
                return [ch3_game, 5.5, 1.1, 1, 1.3, 'supershield']
        
        pygame.display.update()
        clock.tick(FPS)
    select = False
   

##def pause():
##    paused = True
##    while paused:
##        for event in pygame.event.get():
##            if event.type == pygame.QUIT:
##                pygame.quit()
##                quit()
##            if event.type == pygame.KEYDOWN:
##                if event.key == pygame.K_p:
##                    paused = False
##
##        gameDisplay.fill(white)
##        message_to_screen("Pause",
##                          black,0,-100,'large')
##        message_to_screen("Press P to resume",
##                          black,0,250,'small')
##        pygame.display.update()
##        clock.tick(FPS)

def game_Over():
    pygame.mixer.Sound.stop(Sound_p1_abs)
    pygame.mixer.Sound.stop(Sound_p2_abs)
    pygame.mixer.Sound.stop(Sound_barrage)

    pygame.mixer.Sound.play(tada)    
    time.sleep(1.5)
    play('town.mid')
    gameOver = True
    while gameOver:
        gameDisplay.fill(white)
        message_to_screen("Game over", red, 0,-200, 'large')
        if p1_chi>0:
            message_to_screen("P1 won the game!", blue, 0,-80, 'large')
        elif p2_chi>0:
            message_to_screen("P2 won the game!", blue, 0,-80, 'large')
        else:
            message_to_screen("Draw", red, 0,10, 'large')

        message_to_screen("Accumulated Game Score", black, 0,20, 'medium')
        message_to_screen("P1 V.S. P2", black, 0,100, 'medium')
        message_to_screen(str(p1_wt)+" : "+str(p2_wt), black, 0,180, 'medium')
        button("Replay",display_width/2-200,600,100,50,green,light_green,'play')
        button("ReSelect",display_width/2+100,600,100,50,yellow,light_yellow, 'select_ch')
    
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        clock.tick(FPS)
    gameOver = False

def countdown():
    pygame.mixer.music.fadeout(2000)    
    time.sleep(1.5)
    stop()
    gameDisplay.fill(black)
    pygame.mixer.Sound.play(Sound_ready)
    message_to_screen("3", white, 0,0, 'extralarge')
    pygame.display.update()
    time.sleep(1)
    gameDisplay.fill(white)
    pygame.mixer.Sound.play(Sound_ready)
    message_to_screen("2", black, 0,0, 'extralarge')
    pygame.display.update()
    time.sleep(1)
    gameDisplay.fill(black)
    pygame.mixer.Sound.play(Sound_ready)
    message_to_screen("1", white, 0,0, 'extralarge')
    pygame.display.update()
    time.sleep(1)
    gameDisplay.fill(white)
    pygame.mixer.Sound.play(Sound_go)
    message_to_screen("GO", black, 0,0, 'extralarge')   
    pygame.display.update()
    time.sleep(1)



#
#Main Game Loop#
#

def gameLoop():
    global p1_chi, p2_chi, p1_atk_list, p2_atk_list, p1_wt, p2_wt        
    gameOver = False

    gameDisplay.fill(white)
           
    player1,p1_SPEED,p1_absR,p1_chidsct,p1_DFI,p1_skill = p1_attdef[0],p1_attdef[1],p1_attdef[2],p1_attdef[3],p1_attdef[4],p1_attdef[5]
    player2,p2_SPEED,p2_absR,p2_chidsct,p2_DFI,p2_skill = p2_attdef[0],p2_attdef[1],p2_attdef[2],p2_attdef[3],p2_attdef[4],p2_attdef[5]        
        
    
    p1_x = stage_x
    p1_y = (display_height-player_height)/2
    p1_control = True
    p1_mobility = True
    p1_left,p1_right,p1_up,p1_down = 0,0,0,0
    p1_speed = p1_SPEED
    
    p1_chi = 0.5
    p1_absorb = False
    p1_ri = 0

    p1_atk_list = []

    p1_defend = False

    p1_barrage,p1_rebound,p1_supershield,p1_atk5 = False,False,False,False
    p1_CTS = 1

    p1_closeup,p1_atk5s1,p1_atk5s3 = False,False,False
    p1_code = []
    p1_admmode = False
        
    p2_x = (display_width+stage_width)/2 + player_width
    p2_y =  (display_height-player_height)/2
    p2_control = True
    p2_mobility = True
    p2_left,p2_right,p2_up,p2_down = 0,0,0,0
    p2_speed = p2_SPEED

    p2_chi = 0.5
    p2_absorb = False
    p2_ri = 0

    p2_atk_list = []

    p2_defend = False

    p2_barrage,p2_rebound,p2_supershield,p2_atk5 = False,False,False,False
    p2_CTS = 1

    p2_closeup,p2_atk5s1,p2_atk5s3= False,False,False
    p2_code = []
    p2_admmode = False
    
    countdown()
    play('Funk 2.mid',-1)
                 
    while not gameOver:
        gameDisplay.fill(light_yellow) 
        gameDisplay.blit(stage,(stage_x,stage_y))
        gameDisplay.blit(river,(river_x,river_y))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
##                if event.key == pygame.K_p:
##                    pause()

                if p1_control:                  
                    if event.key == pygame.K_w:
                        p1_up = 1
                        p1_code.append('w')
                    elif event.key == pygame.K_s:
                        p1_down = 1
                        p1_code.append('s')
                    elif event.key == pygame.K_a:
                        p1_left = 1
                        p1_code.append('a')
                    elif event.key == pygame.K_d:
                        p1_right = 1
                        p1_code.append('d')
                        
                    if event.key == pygame.K_SPACE:
                        p1_code.append('+')
                        p1_speed = p1_speed/3
                        p1_absorb = True
                        p1_ri = 80 + round(4*p1_chi)*10
                        pygame.mixer.Sound.play(Sound_p1_abs)
                            

                    elif event.key == pygame.K_n and p1_chi > 0.25:
                        p1_chi -= 0.25*p1_chidsct
                        atk = [True]
                        atk.append(p1_x + player_width)
                        atk.append(p1_y + (player_height-atk1_height)/2)
                        atk.append(atk1_width)
                        atk.append(atk1_height)                        
                        p1_atk_list.append(atk)
                        pygame.mixer.Sound.play(Sound_atk1)
                    elif event.key == pygame.K_m and p1_chi > 1:
                        p1_chi -= 1*p1_chidsct
                        atk = [True]
                        atk.append(p1_x + player_width)
                        atk.append(p1_y + (player_height-atk2_height)/2)
                        atk.append(atk2_width)
                        atk.append(atk2_height)                        
                        p1_atk_list.append(atk)
                        pygame.mixer.Sound.play(Sound_atk2)
                    elif event.key == pygame.K_k and p1_chi > 2.5:
                        p1_chi -= 2.5*p1_chidsct
                        atk = [True]
                        atk.append(p1_x + player_width)
                        atk.append(p1_y + (player_height-atk3_height)/2)
                        atk.append(atk3_width)
                        atk.append(atk3_height)                        
                        p1_atk_list.append(atk)
                        pygame.mixer.Sound.play(Sound_atk3)

                    elif event.key == pygame.K_b:
                        if p1_admmode:
                            p2_control = bool(1-p2_control)
                        if not p1_supershield:
                            p1_speed = p1_speed/2
                            p1_defend = True

                    elif event.key == pygame.K_q and p1_CTS >= 1:
                        if not p1_admmode:
                            p1_CTS -= 1
                        p1_skl_t = skill_dur
                        if p1_skill == 'barrage':
                            pygame.mixer.Sound.play(Sound_barrage)
                            p1_barrage = True
                        elif p1_skill == 'rebound':
                            pygame.mixer.Sound.play(Sound_rebound)
                            p1_rebound = True
                        elif p1_skill == 'supershield':
                            pygame.mixer.Sound.play(Sound_supershield)
                            p1_supershield = True
                
                        
                if p2_control:    
                    if event.key == pygame.K_UP:
                        p2_code.append('up')
                        p2_up = 1
                    elif event.key == pygame.K_DOWN:
                        p2_code.append('down')
                        p2_down = 1
                    elif event.key == pygame.K_LEFT:
                        p2_code.append('left')
                        p2_left = 1
                    elif event.key == pygame.K_RIGHT:
                        p2_code.append('right')
                        p2_right = 1

                    if event.key == pygame.K_KP_PLUS:
                        p2_code.append('+')
                        p2_speed = p2_speed/3
                        p2_absorb = True
                        p2_ri = 80 + round(4*p2_chi)*10
                        pygame.mixer.Sound.play(Sound_p2_abs)

                    elif event.key == pygame.K_KP4 and p2_chi > 0.25:
                        p2_chi -= 0.25*p2_chidsct
                        atk = [True]
                        atk.append(p2_x - atk1_width)
                        atk.append(p2_y + (player_height-atk1_height)/2)
                        atk.append(atk1_width)
                        atk.append(atk1_height)                                                
                        p2_atk_list.append(atk)
                        pygame.mixer.Sound.play(Sound_atk1)
                    elif event.key == pygame.K_KP5 and p2_chi > 1:
                        p2_chi -= 1*p2_chidsct
                        atk = [True]
                        atk.append(p2_x - atk2_width)
                        atk.append(p2_y + (player_height-atk2_height)/2)
                        atk.append(atk2_width)
                        atk.append(atk2_height)                                                
                        p2_atk_list.append(atk)
                        pygame.mixer.Sound.play(Sound_atk2)
                    elif event.key == pygame.K_KP8 and p2_chi > 2.5:
                        p2_chi -= 2.5*p2_chidsct
                        atk = [True]
                        atk.append(p2_x - atk3_width)
                        atk.append(p2_y + (player_height-atk3_height)/2)
                        atk.append(atk3_width)
                        atk.append(atk3_height)                                                
                        p2_atk_list.append(atk)
                        pygame.mixer.Sound.play(Sound_atk3)

                    elif event.key == pygame.K_KP6:
                        if p2_admmode:
                            p1_control = bool(1-p1_control)
                        if not p2_supershield:
                            p2_speed = p2_speed/2
                            p2_defend = True

                    elif event.key == pygame.K_KP0 and p2_CTS >=1 :
                        if not p2_admmode:
                            p2_CTS -= 1
                        p2_skl_t = skill_dur
                        if p2_skill == 'barrage':
                            pygame.mixer.Sound.play(Sound_barrage)
                            p2_barrage = True
                        elif p2_skill == 'rebound':
                            pygame.mixer.Sound.play(Sound_rebound)
                            p2_rebound = True
                        elif p2_skill == 'supershield':
                            pygame.mixer.Sound.play(Sound_supershield)
                            p2_supershield = True

                   
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w: 
                    p1_up = 0
                elif event.key == pygame.K_s:
                    p1_down = 0
                elif event.key == pygame.K_a:
                    p1_left = 0
                elif event.key == pygame.K_d:
                    p1_right = 0
                    
                if event.key == pygame.K_SPACE:
                    if p1_absorb:
                        p1_absorb = False
                        p1_speed = p1_speed * 3
                        pygame.mixer.Sound.stop(Sound_p1_abs)
                        

                elif event.key == pygame.K_b:
                    if p1_defend:
                        p1_defend = False
                        p1_speed = p1_speed * 2
                    
                if event.key == pygame.K_UP:
                    p2_up = 0
                elif event.key == pygame.K_DOWN:
                    p2_down = 0
                elif event.key == pygame.K_LEFT:
                    p2_left = 0
                elif event.key == pygame.K_RIGHT:
                    p2_right = 0

                if event.key == pygame.K_KP_PLUS:
                    if p2_absorb:
                        p2_absorb = False
                        p2_speed = p2_speed * 3
                        pygame.mixer.Sound.stop(Sound_p2_abs)
                    
                elif event.key == pygame.K_KP6:
                    if p2_defend:
                        p2_defend = False
                        p2_speed = p2_speed * 2

        while len(p1_code)>9:
            p1_code.remove(p1_code[0])
        if p1_code == ['a','+','+','d','+','+','w','s','w']:
            p1_code = ['w','w','s','s','a','a','d','d','+']
            p1_admmode = bool(1-p1_admmode)
        elif p1_code == ['w','w','s','s','a','a','d','d','+']:
            p1_code = []
            pygame.mixer.Sound.play(tada)
            p1_chi = 4.8
            p1_CTS += 3
        
        while len(p2_code)>9:
            p2_code.remove(p2_code[0])
        if p2_code == ['left','+','+','right','+','+','up','down','up']:
            p2_code = ['up','up','down','down','left','left','right','right','+']
            p2_admmode = bool(1-p2_admmode)
        elif p2_code == ['up','up','down','down','left','left','right','right','+']:
            p2_code = []
            pygame.mixer.Sound.play(tada)
            p2_chi = 4.8
            p2_CTS += 3
        

        if p1_admmode:
            p1_chidsct = 0
            p1_DFI = 100
        if p2_admmode:
            p2_chidsct = 0
            p2_DFI = 100
            
            
        if not p1_control:           
            p1_mobility,p1_absorb,p1_barrage,p1_rebound,p1_supershield = False,False,False,False,False
        elif p1_control:
            p1_mobility = True
        if not p2_control:           
            p2_mobility,p2_absorb,p2_barrage,p2_rebound,p2_supershield = False,False,False,False,False
        elif p2_control:
            p2_mobility = True

        if p1_defend:
            if not p1_supershield:
                gameDisplay.blit(p1_shield,(p1_x+player_width,p1_y))
                p1_dfi = p1_DFI * 4
        else:
            p1_dfi = p1_DFI
        
        if p2_defend:
            if not p2_supershield:
                gameDisplay.blit(p2_shield,(p2_x-shield_width,p2_y))
                p2_dfi = p2_DFI * 4
        else:
            p2_dfi = p2_DFI


        if p1_barrage:
            if p1_skl_t < 0:
                p1_barrage = False
            else:
                if (round(5*FPS*p1_skl_t))% FPS == 0:
                    atk = [True,p1_x + player_width,p1_y + (player_height-atk1_height)/2,atk1_width,atk1_height]                       
                    p1_atk_list.append(atk)
            p1_skl_t -= 1/FPS
        elif p1_rebound:                
            if p1_skl_t < 0:
                p1_rebound = False
            p1_skl_t -= 1/FPS
        elif p1_supershield:
            if p1_skl_t < 0:
                p1_supershield = False
                p1_speed = p1_speed * 5
                p1_dfi = p1_DFI
            else:
                p1_defend = False
                p1_dfi = 12 * p1_DFI
                p1_chi += 0.25/FPS
                p1_speed = p1_SPEED/5
            p1_skl_t -= 1/FPS
                        
        if p2_barrage:
            if p2_skl_t < 0:
                p2_barrage = False
            else:
                if (round(5*FPS*p2_skl_t))% FPS == 0:
                    atk = [True,p2_x - atk1_width,p2_y + (player_height-atk1_height)/2,atk1_width,atk1_height]                       
                    p2_atk_list.append(atk)
            p2_skl_t -= 1/FPS
        elif p2_rebound:
            if p2_skl_t < 0:
                p2_rebound = False
            p2_skl_t -= 1/FPS
        elif p2_supershield:
            if p2_skl_t < 0:
                p2_supershield = False
                p2_speed = p2_speed * 5
                p2_dfi = p2_DFI
            else:
                p2_defend = False
                p2_dfi = 12 * p2_DFI
                p2_chi += 0.25/FPS
                p2_speed = p2_SPEED/5
            p2_skl_t -= 1/FPS
            
        
        if p1_mobility:
            p1_x += (p1_right - p1_left)*p1_speed
            p1_y += (p1_down - p1_up)*p1_speed
            if not p1_admmode:
                p1_x = boundary(p1_x,(display_width-stage_width)/2,(display_width-river_width)/2 - player_width)
                p1_y = boundary(p1_y,(display_height-stage_height)/2,(display_height+stage_height)/2-player_height)                
        if p2_mobility:
            p2_x += (p2_right - p2_left)*p2_speed
            p2_y += (p2_down - p2_up)*p2_speed
            if not p2_admmode:
                p2_x = boundary(p2_x,(display_width+river_width)/2,(display_width-stage_width)/2 + stage_width - player_width)
                p2_y = boundary(p2_y,(display_height-stage_height)/2,(display_height+stage_height)/2-player_height)
            
           
        if p1_absorb:
            p1_chi += absorb(p1_chi)*p1_absR
        if p2_absorb:
            p2_chi += absorb(p2_chi)*p2_absR


        p1_attack(p2_x, p2_y, p2_dfi, p2_rebound)
        p2_attack(p1_x, p1_y, p1_dfi, p1_rebound)
        collide_attack()

        gameDisplay.blit(player1,(p1_x,p1_y))
        gameDisplay.blit(player2,(p2_x,p2_y))

        if p1_chi <= 0 or p2_chi <= 0 :
            pygame.mixer.music.stop()
            time.sleep(0.5)            
            if p1_chi>0:
                p1_wt += 1
            elif p2_chi>0:
                p2_wt += 1
            gameOver = True
            return(game_Over())

        
        elif p1_chi >= 5 and (not p2_atk5):
            pygame.mixer.Sound.stop(Sound_p1_abs)
            pygame.mixer.Sound.stop(Sound_p2_abs)
            pygame.mixer.Sound.stop(Sound_barrage)          
            if not p1_atk5s1:
                pygame.mixer.music.stop()
                play('atk5.mid')
                p1_atk5s1 = True
            p1_atk5 = True
            p1_control = False
            d = round((p2_y - p1_y)/FPS)
            gameDisplay.fill(black)
            gameDisplay.blit(player1,(p1_x,p1_y))
            if p2_chi > 0.01:
                gameDisplay.blit(player2,(p2_x,p2_y))
            if p1_ri < 4000:
                pygame.mixer.Sound.play(Sound_atk5s1)
                p1_ri += 60
                p1_ci = 0
                p1_ring = pygame.transform.scale(chi_ring,(p1_ri,p1_ri))
                p1_ringX, p1_ringY = p1_x+(player_width-p1_ri)/2,p1_y+(player_height-p1_ri)/2
                gameDisplay.blit(p1_ring,(p1_ringX, p1_ringY))
                if RectOverlap(p2_x,p2_y,player_width,player_height,p1_ringX,p1_ringY,p1_ri,p1_ri):
                    if not p2_admmode:
                        p2_control = False
                for atk in p2_atk_list:
                    if RectOverlap(p1_ringX,p1_ringY,p1_ri,p1_ri,atk[1],atk[2],atk[3],atk[4]):
                        atk[0] = False
            else:
                if not p1_closeup:
                    closeup(player1,1)
                    p1_closeup = True
                p1_coreX, p1_coreY = p1_x+(player_width)/2,p1_y+(player_height)/2
                if p1_ci <= 500:
                    pygame.mixer.Sound.play(Sound_atk5s2)
                    p1_ci += 150/FPS
                    p1_lightX, p1_lightY = p1_x+player_width/2,p1_y+player_height/2                    
                    draw_atk5_core(p1_coreX, p1_coreY,p1_ci)            
                    p1_y += d
                    p1_ci2 = p1_ci
                elif p1_lightX - (p1_ci-p1_ci2)/2 < display_width:
                    pygame.mixer.Sound.stop(Sound_atk5s2)
                    if not p1_atk5s3:
                        pygame.mixer.Sound.play(Sound_atk5s3)
                        p1_atk5s3 = True
                    draw_atk5_core(p1_coreX, p1_coreY,p1_ci2)
                    p1_ci2 -= 500/FPS
                    draw_atk5(p1_lightX,p1_lightY,(p1_ci-p1_ci2)/2)                  
                    if RectOverlap(p2_x,p2_y,player_width,player_height,p1_lightX-(p1_ci-p1_ci2)/4,p1_lightY-(p1_ci-p1_ci2)/4,(p1_ci-p1_ci2)/2,(p1_ci-p1_ci2)/2):
                        p2_chi = 0.001
                        pygame.mixer.Sound.stop(Sound_atk5s3)
                        pygame.mixer.Sound.play(Sound_atkhit1)
                    if p1_lightX < 80:
                        p1_lightX = 80
                    p1_lightX += p1_lightX * 0.02
                else:
                    p1_chi = 1
                    if not p2_admmode:
                        p2_chi = 0
                    p1_atk5,p1_closeup,p1_atk5s3 = False,False,False
                    p1_control = True


        elif p2_chi >= 5 and (not p1_atk5):
            pygame.mixer.Sound.stop(Sound_p1_abs)
            pygame.mixer.Sound.stop(Sound_p2_abs)
            pygame.mixer.Sound.stop(Sound_barrage)   
            if not p2_atk5s1:
                pygame.mixer.music.stop()
                play('atk5.mid')
                p2_atk5s1 = True
            p2_atk5 = True
            p2_control = False
            d = round((p1_y - p2_y)/FPS)
            gameDisplay.fill(black)
            if p1_chi > 0.01:
                gameDisplay.blit(player1,(p1_x,p1_y))
            gameDisplay.blit(player2,(p2_x,p2_y))
            if p2_ri < 4000:
                pygame.mixer.Sound.play(Sound_atk5s1)
                p2_ri += 60
                p2_ci = 0
                p2_ring = pygame.transform.scale(chi_ring,(p2_ri,p2_ri))
                p2_ringX, p2_ringY = p2_x+(player_width-p2_ri)/2,p2_y+(player_height-p2_ri)/2
                gameDisplay.blit(p2_ring,(p2_ringX, p2_ringY))
                if RectOverlap(p1_x,p1_y,player_width,player_height,p2_ringX,p2_ringY,p2_ri,p2_ri):
                    if not p1_admmode:
                        p1_control = False
                for atk in p1_atk_list:
                    if RectOverlap(p2_ringX,p2_ringY,p2_ri,p2_ri,atk[1],atk[2],atk[3],atk[4]):
                        atk[0] = False
            else:
                if not p2_closeup:
                    closeup(player2,2)
                    p2_closeup = True
                p2_coreX, p2_coreY = p2_x+(player_width)/2,p2_y+(player_height)/2
                if p2_ci <= 500:
                    pygame.mixer.Sound.play(Sound_atk5s2)
                    p2_ci += 150/FPS
                    p2_lightX, p2_lightY = p2_x+player_width/2,p2_y+player_height/2                    
                    draw_atk5_core(p2_coreX, p2_coreY,p2_ci)            
                    p2_y += d
                    p2_ci2 = p2_ci
                elif p2_lightX + (p2_ci-p2_ci2)/2 > 0:
                    pygame.mixer.Sound.stop(Sound_atk5s2)
                    if not p2_atk5s3:
                        pygame.mixer.Sound.play(Sound_atk5s3)
                        p2_atk5s3 = True
                    draw_atk5_core(p2_coreX, p2_coreY,p2_ci2)
                    p2_ci2 -= 500/FPS
                    draw_atk5(p2_lightX,p2_lightY,(p2_ci-p2_ci2)/2)                  
                    if RectOverlap(p1_x,p1_y,player_width,player_height,p2_lightX-(p2_ci-p2_ci2)/4,p2_lightY-(p2_ci-p2_ci2)/4,(p2_ci-p2_ci2)/2,(p2_ci-p2_ci2)/2):
                        p1_chi = 0.001
                        pygame.mixer.Sound.stop(Sound_atk5s3)
                        pygame.mixer.Sound.play(Sound_atkhit1)
                    if p2_lightX > 1200:
                        p2_lightX = 1200
                    p2_lightX -= (1280-p2_lightX) * 0.02
                else:
                    p2_chi = 1
                    if not p1_admmode:
                        p1_chi = 0
                    p2_atk5,p2_closeup,p2_atk5s3 = False,False,False
                    p2_control = True



        if p1_absorb:
            p1_ri = p1_ri - round(8*p1_absR)
            if p1_ri < 30:
                p1_ri = 80 + round(4*p1_chi)*10
            p1_ring = pygame.transform.scale(chi_ring,(p1_ri,p1_ri))
            gameDisplay.blit(p1_ring,(p1_x+(player_width-p1_ri)/2,p1_y+(player_height-p1_ri)/2))

        if p2_absorb:
            p2_ri = p2_ri - round(8*p2_absR)
            if p2_ri < 30:
                p2_ri = 80 + round(4*p2_chi)*10
            p2_ring = pygame.transform.scale(chi_ring,(p2_ri,p2_ri))
            gameDisplay.blit(p2_ring,(p2_x+(player_width-p2_ri)/2,p2_y+(player_height-p2_ri)/2))

        draw_chibar(p1_chi,60)
        draw_chibar(p2_chi,920)
                                   
        if p1_rebound:
            gameDisplay.blit(rebound,(p1_x+player_width,p1_y))
        elif p1_supershield:              
            gameDisplay.blit(supershield,(p1_x+player_width,p1_y))                         
            
        if p2_rebound:
            gameDisplay.blit(rebound,(p2_x-shield_width,p2_y))               
        elif p2_supershield:
            gameDisplay.blit(supershield,(p2_x-shield_width,p2_y))
        
        pygame.display.update()
        clock.tick(FPS)



#
#In-Game-Function#
#

def boundary(var,lower,upper):
    if var < lower:
        return lower
    elif var > upper:
        return upper
    else:
        return var

def RectOverlap(x1,y1,w1,h1,x2,y2,w2,h2):
    if x1+w1>x2 and x1<x2+w2 and y1+h1>y2 and y1<y2+h2:
        return True
    else:
        return False
    
def absorb(p_chi):
    if p_chi <= 1:
        chi_change = 0.5/FPS
    elif p_chi <= 2:
        chi_change = 0.4/FPS
    elif p_chi <= 3:
        chi_change = 0.3/FPS
    elif p_chi <= 4:
        chi_change = 0.2/FPS
    elif p_chi <= 5:
        chi_change = 0.1/FPS
    else:
        chi_change = 0
    return chi_change

def p1_attack(p2_x, p2_y, p2_dfi, p2_rebound):
    global p1_atk_list, p2_atk_list, p2_chi    
    for atk in p1_atk_list:
        if atk[4] == atk1_height:
            atk[1] += atk1_speed/FPS
            gameDisplay.blit(Ratk1,(atk[1],atk[2]))
        elif atk[4] == atk2_height:
            atk[1] += atk2_speed/FPS
            gameDisplay.blit(Ratk2,(atk[1],atk[2]))
        elif atk[4] == atk3_height:
            atk[1] += atk3_speed/FPS
            gameDisplay.blit(Ratk3,(atk[1],atk[2]))

        if atk[1] > display_width: 
            atk[0] = False 
        if RectOverlap(atk[1],atk[2],atk[3],atk[4],p2_x+10,p2_y+5,player_width-20,player_height-10):
            atk[0] = False
            if p2_rebound:
                pygame.mixer.Sound.play(Sound_atkhit2)
                rbd_atk=[True,atk[1],atk[2],atk[3],atk[4]]
                p2_atk_list.append(rbd_atk)
            else:
                if p2_dfi < 2:
                    pygame.mixer.Sound.play(Sound_atkhit1)
                else:
                    pygame.mixer.Sound.play(Sound_atkhit2)
                if atk[4] == atk1_height:
                    p2_chi -= atk1_damage/p2_dfi
                elif atk[4] == atk2_height:
                    p2_chi -= atk2_damage/p2_dfi
                elif atk[4] == atk3_height:
                    p2_chi -= atk3_damage/p2_dfi
        for atk in p1_atk_list:
            if atk[0] == False:
                p1_atk_list.remove(atk)


def p2_attack(p1_x, p1_y, p1_dfi, p1_rebound):
    global p1_atk_list, p2_atk_list, p1_chi    
    for atk in p2_atk_list:
        if atk[4] == atk1_height:
            atk[1] += - atk1_speed/FPS
            gameDisplay.blit(Latk1,(atk[1],atk[2]))
        elif atk[4] == atk2_height:
            atk[1] += - atk2_speed/FPS
            gameDisplay.blit(Latk2,(atk[1],atk[2]))
        elif atk[4] == atk3_height:
            atk[1] += - atk3_speed/FPS
            gameDisplay.blit(Latk3,(atk[1],atk[2]))

        if atk[1] < 0: 
            atk[0] = False 
        if RectOverlap(atk[1],atk[2],atk[3],atk[4],p1_x+10,p1_y+5,player_width-20,player_height-10):
            atk[0] = False
            if p1_rebound:
                pygame.mixer.Sound.play(Sound_atkhit2)
                rbd_atk=[True,atk[1],atk[2],atk[3],atk[4]]
                p1_atk_list.append(rbd_atk)
            else:
                if p1_dfi < 2:
                    pygame.mixer.Sound.play(Sound_atkhit1)
                else:
                    pygame.mixer.Sound.play(Sound_atkhit2)
                if atk[4] == atk1_height:
                    p1_chi -= atk1_damage/p1_dfi
                elif atk[4] == atk2_height:
                    p1_chi -= atk2_damage/p1_dfi
                elif atk[4] == atk3_height:
                    p1_chi -= atk3_damage/p1_dfi
        for atk in p2_atk_list:
            if atk[0] == False:
                p2_atk_list.remove(atk)




def collide_attack():
    global p1_atk_list, p2_atk_list
    for p1_atk in p1_atk_list:
        for p2_atk in p2_atk_list:
            if RectOverlap(p1_atk[1],p1_atk[2],p1_atk[3],p1_atk[4],p2_atk[1],p2_atk[2],p2_atk[3],p2_atk[4]):
                pygame.mixer.Sound.play(Sound_atkcol)
                if p1_atk[4] >= p2_atk[4]:
                    p2_atk[0] = False
                if p2_atk[4] >= p1_atk[4]:
                    p1_atk[0] = False
    for atk in p1_atk_list:
            if atk[0] == False:
                p1_atk_list.remove(atk)    
    for atk in p2_atk_list:
            if atk[0] == False:
                p2_atk_list.remove(atk)


def draw_chibar(p_chi,x,y=680,L=300,W=20):
    pygame.draw.rect(gameDisplay, white, [x,y,L,W])
    if p_chi <= 1:
        pygame.draw.rect(gameDisplay, red, [x,y,L*p_chi/5,W])
    elif p_chi <= 2:
        pygame.draw.rect(gameDisplay, chi1, [x,y,L*p_chi/5,W])
    elif p_chi <= 3:
        pygame.draw.rect(gameDisplay, chi2, [x,y,L*p_chi/5,W])
    elif p_chi <= 4:
        pygame.draw.rect(gameDisplay, chi3, [x,y,L*p_chi/5,W])
    else:
        pygame.draw.rect(gameDisplay, chi4, [x,y,L*p_chi/5,W])
    gameDisplay.blit(chi_ruler,(x-50,y-20))


def closeup(player,playercode):
    closingup = True
    stop = True
    if player == ch1_game:
        player_large = ch1_large
    elif player == ch2_game:
        player_large = ch2_large
    elif player == ch3_game:
        player_large = ch3_large

    if playercode == 1:
        X = -350
        k = 1
    elif playercode == 2:
        X = 1280
        k = -1
    Y = 360
    gameDisplay.fill(black)
    while closingup:
        gameDisplay.blit(player_large,(X,Y))
        pygame.display.update()
        X += round(1230/FPS)*k
        if stop and (-round(815/FPS) < X - 465 < round(815/FPS)):
            time.sleep(1.5)
            stop = False
        if X >1280 or X < -350:
            closingup = False
        clock.tick(FPS)


def draw_atk5_core(coreX,coreY,ci):
    if ci < 0:
        return None
    else:
        ci=round(ci)
        core = pygame.transform.scale(atk5_core,(ci,ci))
        gameDisplay.blit(core,(round(coreX-ci/2),round(coreY-ci/2)))

    
def draw_atk5(x,y,ci):
    ci = round(ci)
    satk5 = pygame.transform.scale(atk5,(ci,ci))
    gameDisplay.blit(satk5,(round(x-ci/2),round(y-ci/2)))


game_welcome()



