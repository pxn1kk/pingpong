from pygame import *
from time import time as timer

class GameSprite(sprite.Sprite):
    def __init__(self, player_img, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_img), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def redate_l(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        movement = key.get_pressed()
        if movement[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if movement[K_DOWN] and self.rect.y < w_w - 80:
            self.rect.y += self.speed
    def redate_r(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        movement = key.get_pressed()
        if movement[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if movement[K_s] and self.rect.y < w_w - 80:
            self.rect.y += self.speed
   

w_w = 700
w_h = 700
window = display.set_mode((w_w, w_h))
display.set_caption("Ping Pong")
bg = (0,0,0)
window.fill(bg)
clock = time.Clock()
fps = 60

player_r = Player("rightracket.png", 600, 0, 10, 100, 100)
player_l = Player("leftracket.png", 1, 0, 10, 100, 100)
ball = GameSprite("ball.png", 300, 280, 5, 100, 100)

speed_x = ball.speed
speed_y = ball.speed

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(bg)

        ball.rect.x -= speed_x
        ball.rect.y += speed_y
        
        player_r.redate_r()
        player_l.redate_l()

        if ball.rect.y > w_h - 50 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x > w_w - 50 or ball.rect.x < 0:
            speed_x *= -1
        if sprite.collide_rect(player_l, ball) or sprite.collide_rect(player_r, ball):
            speed_x *= -1
        ball.reset()
        player_l.reset()
        player_r.reset()
      
    display.update()
    clock.tick(fps)
