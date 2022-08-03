from pygame import* 
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
    def __init__(self,x,y,width,height,filename,speed):
        super().__init__()
        self.image =transform.scale(image.load(filename), (width, height))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed = speed
    def draw(self):
        draw.rect(window,self.color,self.rect)
class Player_1():
    def update(self):
        keys = key.get.pressed()
        if keys[K_UP] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
scr_width = 600
scr_height = 400
 
display.set_caption('Pong')
icon = image.load('icon.png')
display.set_icon(icon)

window = display.set_mode((scr_width,scr_height))
background = transform.scale(image.load("white.png"), (scr_width, scr_height))
ball = GameSprite(350, 250,10,10,"ball.png",5)

paddle_1 = GameSprite(10, 200, 10, 50, "paddle.png", 3)
paddle_2 = GameSprite(580, 200, 10, 50, "paddle.png", 3)

run = True
finish = False
while run:
    window.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish != True:
        window.blit(background,(0, 0))
        paddle_1.update()
        paddle_2.update()
        ball.update()
        
        paddle_1.draw()
        paddle_2.draw()
        ball.draw()
    display.update()