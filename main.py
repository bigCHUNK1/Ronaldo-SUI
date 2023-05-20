import pygame, sys, time, random
from pygame.locals import QUIT

pygame.init()
winWidth = 1000
winHeight = 600
window = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption('i am a bad website')

class Character:
    def __init__(self):
        self.x = winWidth/2
        self.y = winHeight/2
        self.i =0
        self.sprite = [pygame.transform.scale(pygame.image.load("sprite.png"),(100,100)),pygame.transform.scale(pygame.image.load("pixil-frame-0.png"),(100,100))]
    def move(self, userinput):
        self.i = 0
        if userinput[pygame.K_w]:
            self.y-=1
        elif  userinput[pygame.K_s]:
            self.y +=1
        elif  userinput[pygame.K_a]:
            self.x -=1
        elif  userinput[pygame.K_d]:
            self.x +=1
        if userinput[pygame.K_SPACE]:
            self.attack()
    def attack(self):
        self.i = 1
    def draw(self):
        window.blit(self.sprite[self.i],(self.x,self.y))


class Pig:
    def __init__(self):
        self.x = winWidth / 2
        self.y = winHeight / 2
        self.i = 0
        self.alive = True
        self.sprite = [pygame.transform.scale(pygame.image.load("redpig.png"), (100, 100)),pygame.transform.scale(pygame.image.load("deth1.png"), (100, 100)),
                       pygame.transform.scale(pygame.image.load("deth2.png"), (100, 100))]

    def move(self):
        direction = random.randint(0,3)
        if direction == 0:
            for i in range(0,10):
                self.x-=1
                self.hit()
        elif direction == 1:
            for i in range(0, 10):
                self.x += 1
                self.hit()
        elif direction == 2:
            for i in range(0,10):
                self.y-=1
                self.hit()
        elif direction == 3:
            for i in range(0, 10):
                self.y += 1
                self.hit()


    def hit(self):
        if player.x <= self.x <= player.x+100 and self.alive == True:
            if player.y <= self.y <= player.y + 100:
                if player.i == 1:
                    self.alive = False
    def draw(self):
        if self.alive == True:
            if self.i < 3:
                self.move()
                window.blit(self.sprite[self.i], (self.x, self.y))
        elif self.alive== False and self.i>2:
            self.i+=1
            window.blit(self.sprite[self.i], (self.x, self.y))

def draw():
    window.fill((255,255,255))
    player.draw()
    for pig in pigs:
        pig.draw()
    pygame.display.flip()

score = 0
#scoreText = pygame.font.SysFont('corbel',35).render(score,True,(0,0,0))
player = Character()
pigs = []
for i in range(0,500):
    pigs.append(Pig())
while True:

    draw()
    userinput = pygame.key.get_pressed()
    player.move(userinput)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    print("hello")