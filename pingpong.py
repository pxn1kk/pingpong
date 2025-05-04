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
   

w_w = 1000
w_h = 1000
window = display.set_mode((w_w, w_h))
display.set_caption("Ping Pong")
bg = (0,0,0)
window.fill(bg)
clock = time.Clock()
fps = 60

player_r = Player("rightracket.png", 770, 0, 5, 200, 200)
player_l = Player("leftracket.png", 70, 0, 5, 200, 200)


game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(bg)
        player_l.reset()
        player_r.reset()
        player_r.redate_r()
        player_l.redate_l()
        
    display.update()
    clock.tick(fps)
