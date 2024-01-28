import pygame
pygame.init()
w_width=900
w_height=600
screen=pygame.display.set_mode((w_width,w_height))
screen.fill("white")
pygame.display.set_caption("projectiles")

clock=pygame.time.Clock()

bg_img= pygame.image.load("img/backrou.jpeg")
bg_img=pygame.transform.scale(bg_img,(w_width,w_height))

walkright=[pygame.image.load(f'sprites/male/{i}.png')for i in range(1,10)]
walkleft=[pygame.image.load(f'sprites/{i}.png')for i in range(1,10)]
char=pygame.image.load('sprites/0.png')
moveright=[pygame.image.load(f'sprites/female/{i}.png') for i in range(1,10)]
moveleft=[pygame.image.load(f'sprites/male/{i}.png') for i in range(1,10)]

class player():
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=5
        self.is_jump=False
        self.jump_count=10
        self.left=False
        self.right=False
        self.walkcount=0
        self.standing=True
    def draw(self,screen):
            if self.walkcount +1>=27:
                self.walkcount=0
            if not(self.standing):
                if self.left:
                    screen.blit(walkleft[self.walkcount//3],(self.x,self.y))
                    self.walkcount +=1
                
                elif self.right:
                    screen.blit(walkright[self.walkcount//3],(self.x,self.y))
                    self.walkcount +=1
            else:
                if self.right:
                    screen.blit(walkright[0],(self.x,self.y))
                else:
                    screen.blit(walkleft[0],(self.x,self.y))
class projectile():
    def __init__(self,x,y,radius,color,direction):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.direction=direction
        self.vel=8*direction
    def draw(self,screen):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)

class enemy():


    def __init__(self,x,y,width,height,end):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.walkcount=0
        self.vel=3
        self.path=[x,end]
    def draw(self,screen):
        self.move()
        if self.walkcount +1>=27:
                self.walkcount=0
        if self.vel>0:
            screen.blit(moveright[self.walkcount//3],(self.x,self.y))
            self.walkcount +=1
        else:
            screen.blit(moveleft[self.walkcount//3],(self.x,self.y))
            self.walkcount +=1      
    def move(self):
        if self.vel>0:
            if self.x<self.path[1]-self.width:
                self.x+=self.vel
            else:
                self.vel=self.vel*-1
                self.x+=self.vel
                self.walkcount=0
        else:
            if self.x>self.path[0]:
                self.x+=self.vel
            else:
                self.vel=self.vel*-1
                self.x+=self.vel
                self.walkcount=0

def drawingameloop():
    screen.blit(bg_img,(0,0))
    clock.tick(25)
    for bullet in bullets:
        bullet.draw(screen)
    soldier.draw(screen) 
    enemy.draw(screen)
    pygame.display.flip()


bullets=[]
shoot=0
soldier=player(50,45,64,64)
enemy=enemy(0,45,6,6,w_width)
done=True
while done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=False
    if shoot>0:
        shoot+=1
    if shoot>3:
        shoot=0
        
    for bullet in bullets:
        if bullet.x<500 and bullet.x>0:
            bullet.x+=bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    keys =  pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and shoot==0:
        if soldier.left:
            direction=-1
        else:
            direction=1
        if len(bullets)<5:
            bullets.append(projectile((soldier.x+soldier.width//2),(soldier.y+soldier.height//2),6,"blue",direction))
        shoot=1
    if keys[pygame.K_LEFT]and soldier.x>0:
        soldier.x-=soldier.vel
        soldier.left=True
        soldier.right=False
        soldier.standing=False
    elif keys[pygame.K_RIGHT] and soldier.x<w_width-soldier.width:
        soldier.x+=soldier.vel
        soldier.right=True
        soldier.left=False
        soldier.standing=False
    else:
        soldier.standing=True
        soldier.walkcount=0
        
    if not (soldier.is_jump):
        if keys[pygame.K_UP] and soldier.y>0:
            soldier.is_jump=True
            soldier.right=False
            soldier.left=False
        if keys[pygame.K_DOWN]and soldier.y<w_height-soldier.height:
            soldier.y+=soldier.vel
    else:
        if soldier.is_jump:
            if soldier.jump_count>=10:
                neg=1
                if soldier.jump_count<0:
                    neg=-1
                soldier.y-=(soldier.jump_count**2)*neg*0.5
                soldier.jump_count-=1
            else:
                soldier.jump_count=10
                soldier.is_jump=False
            
        
        
    drawingameloop()