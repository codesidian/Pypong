import pygame,random

pygame.init()
paddleA_y=50
paddleB_y=50
run=1
player1ypos=760
player1xpos=300
player2ypos=10
player2xpos=300
#####################Colours#####################
white = (255,255,255)
grey = (170,170,170)
black = (0,0,0)
cyan=(0,255,255)
red = (255,0,0)
green = (0,255,0)
darkGreen = (0,155,0)
blue = (0,0,255)
#####################Display Variables#####################
display_width=800
display_height=600
gameDisplay = pygame.display.set_mode((display_width,display_height),0,32)
gameDisplay.fill((70, 70, 70))
font = pygame.font.Font("./fonts/editundo.ttf", 75)
#####################Sound Variables#####################
pygame.mixer.init()
pygame.mixer.set_num_channels(8)
soundChan = pygame.mixer.Channel(5)
score=pygame.mixer.Sound("score.wav")
hit=pygame.mixer.Sound("hit.wav")
wall=pygame.mixer.Sound("wall.wav")





class Player(object):
    def __init__(self):
        self.rect = pygame.rect.Rect((15, 300, 30, 150))
        self.paddlespeed=7

    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            if self.rect.y-self.paddlespeed>0:
                self.rect.move_ip(0, -self.paddlespeed)
        if key[pygame.K_s]:
            if self.rect.y+self.paddlespeed+150<600:
                self.rect.move_ip(0, self.paddlespeed)

    def draw(self, surface):
        pygame.draw.rect(gameDisplay, white, self.rect)
        
    def posx(self):
        return self.rect.x
        
    def posy(self):
        return self.rect.y
      
        

        
class Player2(object):
    def __init__(self):
        self.rect = pygame.rect.Rect((760, 300, 30, 150))
        self.paddlespeed=7

    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            if self.rect.y-self.paddlespeed>0:
                self.rect.move_ip(0, -self.paddlespeed)
        if key[pygame.K_DOWN]:
            if self.rect.y+self.paddlespeed+150<600:
                self.rect.move_ip(0, self.paddlespeed)

    def draw(self, surface):
        pygame.draw.rect(gameDisplay, white, self.rect)

    def posx(self):
        return self.rect.x
        
    def posy(self):
        return self.rect.y
        

class Ball(object):
    def __init__(self):
        self.x=400
        self.y=300    
        self.circ = pygame.draw.circle(gameDisplay,white,(300,300),10)
        self.player1_score=0
        self.player2_score=0
        self.speedx=0
        self.speedy=0
       
        
    def move(self,player1xpos,player1ypos,player2xpos,player2ypos):
        key = pygame.key.get_pressed()
        self.x+=self.speedx
        self.y+=self.speedy
        ballboundary=pygame.Rect(self.x-15,self.y-15,30,30)
        p2boundary=pygame.Rect(player1xpos, player1ypos, 30, 150)
        p1boundary=pygame.Rect(player2xpos, player2ypos, 30, 150)

        self.player1score = font.render(str(self.player1_score), True, white)
        self.player1scoreshad = font.render(str(self.player1_score), True, black)
        
        self.player2score = font.render(str(self.player2_score), True, white)
        self.player2scoreshad = font.render(str(self.player2_score), True, black)

        gameDisplay.blit(self.player1score,(60, 30))
        gameDisplay.blit(self.player1scoreshad,(58, 28))
        gameDisplay.blit(self.player1score,(56, 26))

        
        gameDisplay.blit(self.player2score,(710, 30))
        gameDisplay.blit(self.player2scoreshad,(708, 28))
        gameDisplay.blit(self.player2score,(706, 26))


       
        
        if ballboundary.colliderect(p2boundary):
            soundChan.play(hit)
            self.speedx=random.randint(-15,-1)
            self.speedy=random.randint(-15,15)
            self.x+=self.speedx
            self.y+=self.speedy

        if ballboundary.colliderect(p1boundary):
            soundChan.play(hit)
            self.speedx=random.randint(1,15)
            self.speedy=random.randint(-15,15)
            self.x+=self.speedx
            self.y+=self.speedy
            
            
            
            

        if self.x-self.speedx<20:
            soundChan.play(score)
            
            self.speedx=random.randint(-15,15)
            self.speedy=random.randint(-15,15)
            self.x=400
            self.y=300
            self.player2_score+=1


            
        if self.x+self.speedx>830:
            soundChan.play(score)
            self.speedx=random.randint(-15,15)
            self.speedy=random.randint(-15,15)
            self.x=400
            self.y=300
            
            self.player1_score+=1


            
            

        if self.y+self.speedy<15:
            soundChan.play(wall)                
            self.speedy=random.randint(1,15)
            self.x+=self.speedx
            self.y+=self.speedy
        if self.y-self.speedy>590:
            soundChan.play(wall)
            self.speedy=random.randint(-15,-1)
            self.x+=self.speedx
            self.y+=self.speedy
            
        if key[pygame.K_SPACE]:
            self.speedx=random.randint(-15,15)
            self.speedy=random.randint(-15,15)
            self.x+=self.speedx
            self.y+=self.speedy           
            
        
    def draw(self, surface):
        
        pygame.draw.rect(gameDisplay, black, ((player1xpos, player1ypos, 40, 160)))
        pygame.draw.rect(gameDisplay, black, (self.x-15,self.y-15,30,30))
        pygame.draw.circle(gameDisplay,red,(self.x,self.y),15)

        

        


def main(paddleA_y,paddleB_y):
    player = Player()
    player2 = Player2()
    ball=Ball()
    FPS=24
    clock = pygame.time.Clock()
    pygame.mixer.init()
    pygame.mixer.set_num_channels(8)

    musicChan = pygame.mixer.Channel(5) 
    gameExit=True
    num=0
    while gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
                gameExit=False
        gameDisplay.fill(black)

        key = pygame.key.get_pressed()
        if key[pygame.K_p]:
            gameExit=False
        
        player.draw(gameDisplay)
        player.handle_keys()
        
        player2.draw(gameDisplay)
        player2.handle_keys()
        
        player1xpos=player2.posx()
        player1ypos=player2.posy()
        player2ypos=player.posy()
        player2xpos=player.posx()

##        print("x pos "+str(player1xpos))
##        print("y pos "+str(player1ypos))
       
        
        ball.move(player1xpos,player1ypos,player2xpos,player2ypos)
        ball.draw(gameDisplay)
        
        pygame.display.update()
        clock.tick(FPS)
           
        


main(paddleA_y,paddleB_y)
