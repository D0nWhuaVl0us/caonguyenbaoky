from pygame import* 
from random import*
class GameSprite(sprite.Sprite):
    def __init__(self,x,y,width,height,filename,speed):
        super().__init__()
        self.image =transform.scale(image.load(filename), (width, height))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed = speed
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player():
    def __init__(self,x,y,width,height,filename,Color,speed):
        super().__init__()
        self.image =transform.scale(image.load(filename), (width, height))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed = speed
        self.color = Color
    def draw(self):
        draw.rect(window,self.color,self.rect)
class Player_1(Player):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y <= 400:
            self.rect.y += self.speed
class Player_2(Player):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <= 400:
            self.rect.y += self.speed
class Ball():
    def __init__(self, filename, x, y, Color, width, height, speed):
        super().__init__()
        self.image =transform.scale(image.load(filename), (width, height))
        self.velocity = [randint(4,8),randint(-8,8)]
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.speed_x = speed
        self.speed_y = speed
        self.color = Color
    def update(self):
        global finish
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.x < 0 or self.rect.x >600:
            finish = True
        if self.rect.y < 0 or self.rect.y > 400:
            self.speed_y *= -1
    def draw(self):
        draw.rect(window,self.color, self.rect)
scr_width = 600
scr_height = 400
 
display.set_caption('Pong')
icon = image.load('icon.png')
display.set_icon(icon)

window = display.set_mode((scr_width,scr_height))
background = transform.scale(image.load("white.png"), (scr_width, scr_height))

ball = Ball('ball.png',300,200, (0,0,0), 10, 10, 1)
paddle_1 = Player_1(10, 200, 10, 50, "paddle.png", (0,0,0), 3)
paddle_2 = Player_2(580, 200, 10, 50, "paddle.png", (0,0,0), 3)

font.init()
font1 = font.Font(None, 50)
score_1 = 0
score1_txt = font1.render(f"Score : {score_1}", True, (81,17,17))
score_2 = 0
score2_txt = font1.render(f"Score : {score_2}", True, (81,17,17))
clock = time.Clock
run = True
finish = False
while run:
    window.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.blit(background,(0, 0))
        window.blit(score1_txt, (100,15))
        window.blit(score2_txt, (450,15))

        paddle_1.update()
        paddle_2.update()
        ball.update()
        
        paddle_1.draw()
        paddle_2.draw()
        ball.draw()
    if sprite.collide_rect(paddle_1, ball):
        ball.speed_x *= -1
        score_1 += 1
    if sprite.collide_rect(paddle_2, ball):
        ball.speed_x *= -1
        score_2 += 1
    display.update()