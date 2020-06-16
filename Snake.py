import pygame
import time
import random
x=pygame.init()
print (x)

FPS=50


direction="right"
display_width=1000
display_height=600

gameDisplay=pygame.display.set_mode((display_width,display_height))

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)   
orange=(255,128,0)
green=(0,155,0)

img=pygame.image.load("snakehead.png")              #should be in the same directory where the file is 
apple=pygame.image.load("apple.png")
icon=pygame.image.load("icon.png")


pygame.display.set_caption('Snake')         
pygame.display.set_icon(icon)

clock=pygame.time.Clock()

block_size=20
Applethickness=30

smallfont=pygame.font.SysFont('Times New Roman',25)              
medfont=pygame.font.SysFont('Times New Roman',50)
largefont=pygame.font.SysFont('Times New Roman',75)


def pause():
    paused=True
    while paused:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    paused=False

                if event.key==pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen("Paused",red,0,-40,"med")
        message_to_screen("Press C to continue or Q to quit",black)
        pygame.display.update()
        clock.tick(15)
        
def score(score):
    
    text=smallfont.render(" "+ str(score),True,black)
    
    gameDisplay.blit(text,(0,0));

def randAppleGen():
    randAppleX=round(random.randrange(0,display_width-Applethickness))      
    randAppleY=round(random.randrange(0,display_height-Applethickness))

    return randAppleX,randAppleY

randAppleX,randAppleY=randAppleGen()

def snake(block_size,snakelist):
    if direction=="right":
        head=pygame.transform.rotate(img,270)

    if direction=="left":
        head=pygame.transform.rotate(img,90)

    if direction=="up":
        head=img

    if direction=="down":
        head=pygame.transform.rotate(img,180)
    
    gameDisplay.blit(head,(snakelist[-1][0],snakelist[-1][1]))
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay,green,[XnY[0],XnY[1],block_size,block_size])
        
def text_objects(text,color,size='small'):
    if size=='small':
        textSurf=smallfont.render(text,True,color)
    elif size=='med':
        textSurf=medfont.render(text,True,color)
    elif size=='large':
        textSurf=largefont.render(text,True,color)
    return textSurf,textSurf.get_rect()
    
def message_to_screen(msg,color,x_displace=0,y_displace=0,size="small"):
    textSurf,textRect=text_objects(msg,color,size)         
    textRect.center=(display_width/2)+x_displace,(display_height/2)+y_displace          #for the arrangement of the displayed message 
    gameDisplay.blit(textSurf,textRect)

def game_intro():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key==pygame.K_c:
                    gameLoop()
    
        gameDisplay.fill(white)
        message_to_screen('Welcome to Snake',green,0,-100,"large")
        message_to_screen('*The objective of the Game is to eat the red apples ',black,0,30)
        message_to_screen('*The more apples you eat the longer you get ',black,0,70)
        message_to_screen("*If you run into the edges or yourself you'll die!",black,0,110)
        message_to_screen('*Press C to Start the Game,Q to Quit and P to Pause   ',black,0,150)
        message_to_screen('*Controls- Arrow Keys   ',black,0,190)
        message_to_screen('~by Priyansh Agarwal    ',black,280,280)
        
                
        pygame.display.update()
        clock.tick(15)
        
gameExit=False

def gameLoop():
    
    
    global direction
    gameExit=False
    gameOver=False
    
    lead_x=display_width/2                           
    lead_y=display_height/2
    
    lead_x_change=0
    lead_y_change=0

    randAppleX,randAppleY=randAppleGen()

    snakelist=[]
    snakelength=1
    while not gameExit:
        while gameOver==True:    
            gameDisplay.fill(white)
            message_to_screen("Game over",red,0,-80,size='large')
            message_to_screen("Press C to play again or Q to quit",black)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        gameExit=True
                        gameOver=False

                    if event.key==pygame.K_c:
                        gameLoop()
        
        for event in pygame.event.get():                           
            if event.type==pygame.QUIT:
                gameOver=False
                gameExit=True                              
      
            if event.type==pygame.KEYDOWN:                                 
                if event.key==pygame.K_LEFT:
                    lead_y_change=0
                    lead_x_change=-block_size
                    direction="left"
                elif event.key==pygame.K_RIGHT:
                    lead_y_change=0
                    lead_x_change=block_size
                    direction="right"
                elif event.key==pygame.K_UP:
                    lead_x_change=0
                    lead_y_change=-block_size
                    direction="up"
                elif event.key==pygame.K_DOWN:
                    lead_x_change=0
                    lead_y_change=block_size
                    direction="down"
                elif event.key==pygame.K_p:
                    pause()
        if lead_x>=display_width or lead_x<=0 or lead_y>=display_height or lead_y<=0:                
            gameOver=True

        lead_x+=lead_x_change
        lead_y+=lead_y_change
        
        gameDisplay.fill(orange)            

        
        #pygame.draw.rect(gameDisplay,red,[randAppleX,randAppleY,Applethickness,Applethickness])
        gameDisplay.blit(apple,(randAppleX,randAppleY))
        snakehead=[]
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)
        
        
        
        if len(snakelist)>snakelength:
            del snakelist[0]


        for eachsegment in snakelist[:-1]:
            if eachsegment==snakehead:              
                gameOver=True
            
        snake(block_size,snakelist)
        score(snakelength-1)
        
        pygame.display.update()
        
        if lead_x>randAppleX and lead_x<randAppleX+Applethickness or lead_x+block_size>randAppleX and lead_x+block_size<randAppleX+Applethickness:
                  if lead_y>randAppleY and lead_y<randAppleY+Applethickness or lead_y+block_size>randAppleY and lead_y+block_size<randAppleY+Applethickness:
                      randAppleX,randAppleY=randAppleGen()
                      snakelength+=1
        clock.tick(FPS)
        
    pygame.quit()                              
    quit()                                              

#----------------------------------------------------------------#
game_intro()



