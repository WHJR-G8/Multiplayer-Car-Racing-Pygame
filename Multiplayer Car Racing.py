import pygame, sys, random

pygame.init()

clock=pygame.time.Clock()
width=500
height=360
screen = pygame.display.set_mode((width,height))

score = "Game Finished"
score_font = pygame.font.Font("freesansbold.ttf", 16)
  
#load the images in dict
images={}
images["bg"] = pygame.image.load("bg.png").convert_alpha()
images["car1"] = pygame.image.load("car1.png").convert_alpha()
images["car2"] = pygame.image.load("car2.png").convert_alpha()
pit = pygame.image.load("pit.png")
fuel = pygame.image.load("fuel.png")
groundx=0

pit_rect = pygame.Rect(random.randint(10,300),random.randint(10,300),1,30)
fuel_rect = pygame.Rect(random.randint(10,300),random.randint(10,300),30,30)

class Vehicle1:
    def __init__(self,x,y):
      self.rect1= pygame.Rect(x,y,30,52)
   
    def display(self,img):
      screen.blit(img,self.rect1)
                
    def moveLeft(self):
      self.rect1.y=self.rect1.y-100
        
    def moveRight(self):
      self.rect1.y=self.rect1.y+100

car1=Vehicle1(15,10)
car2=Vehicle1(20,100)

while True:    
    screen.fill((50,150,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                car1.moveLeft()
            elif event.key == pygame.K_a:
                car2.moveLeft()
            elif event.key == pygame.K_RIGHT:
                car1.moveRight()
            elif event.key == pygame.K_d:
                car2.moveRight()

    if car1.rect1.colliderect(fuel_rect):
        car1.rect1.x = car1.rect1.x + 100
        fuel_rect.x = 600
        fuel_rect.y = random.randint(10,300)

    if car2.rect1.colliderect(fuel_rect):
        car2.rect1.x = car2.rect1.x + 100
        fuel_rect.x = 600
        fuel_rect.y = random.randint(10,300)

    if car1.rect1.colliderect(pit_rect):
        car1.rect1.x = car1.rect1.x - 5
        pit_rect.x = 600
        pit_rect.y = random.randint(10,300)

    if car2.rect1.colliderect(pit_rect):
        car2.rect1.x = car2.rect1.x - 5
        pit_rect.y = random.randint(10,300)

    groundx = groundx-1
    if(groundx < -190):
        groundx=0

    pit_rect.x = pit_rect.x - 1
    if pit_rect.x <= -30:
        pit_rect.x = 700
        pit_rect.y = random.randint(10,300)

    fuel_rect.x =fuel_rect.x - 1
    if fuel_rect.x <= -30:
        fuel_rect.x = 700
        fuel_rect.y = random.randint(10,300)

    screen.blit(images["bg"],[groundx,0]) 
    car1.display(images["car1"])
    car2.display(images["car2"])
    screen.blit(pit,pit_rect)
    screen.blit(fuel,fuel_rect)

    if car1.rect1.x >= 450:
        score_show = score_font.render("Car 1 Wins " + str(score) , True, (250,250,250))
        screen.blit(score_show, (50, 50))
        crash = pygame.mixer.Sound("crash.wav")
        crash.play()
        pygame.display.update()
        pygame.time.delay(5000)
        pygame.quit()   
    
    if car2.rect1.x >= 450:
        score_show = score_font.render("Car 2 Wins " + str(score) , True, (250,250,250))
        screen.blit(score_show, (50, 50))
        pygame.display.update()
        pygame.time.delay(5000)
        pygame.quit()

    pygame.display.update()
    clock.tick(500)