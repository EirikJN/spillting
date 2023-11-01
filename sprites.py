import pygame as pg
import random
 
player_image = pg.image.load("images/player.png")
enemy_image = pg.image.load("images/enemy.png")
enemy_image = pg.transform.scale(enemy_image, (100,100))
 
ranged_image = pg.image.load("images/ranged_img.png")
ranged_imageimage = pg.transform.scale(ranged_image, (30,30))
 
class Player(pg.sprite.Sprite):
    def __init__(self, all_sprites): # denne funksjonen kjører når vi lager player
        pg.sprite.Sprite.__init__(self)
        self.image = player_image
        self.rect = self.image.get_rect()
        self.pos_x = 50
        self.pos_y = 400
        self.speed = 5
        self.hp = 100
        self.all_sprites = all_sprites
 
    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.kill()
 
    def attack(self):
        projectile = Ranged_attack(self.pos_x, self.pos_y)
        print("attacked")
        projectile.add(self.all_sprites)
 
    def update(self):
        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y
 
        if self.pos_x > 900:
            self.kill()
 
        # player input
        keys = pg.key.get_pressed()
        if keys[pg.K_w]: # oppover
            self.pos_y -= self.speed
        if keys[pg.K_s]: # nedover
            self.pos_y += self.speed
        if keys[pg.K_a]: # venstre
            self.pos_x -= self.speed
        if keys[pg.K_d]: # høyre
            self.pos_x += self.speed 
 
        if keys[pg.K_SPACE]:
            self.attack()
 
class Enemy(pg.sprite.Sprite):
    def __init__(self): # denne funksjonen kjører når vi lager player
        pg.sprite.Sprite.__init__(self)
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.pos_x = 900
        self.pos_y = random.randint(0,600)
        self.speed = random.randint(1,10)
 
    def update(self):
        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y
 
        self.pos_x -= self.speed
 
        if self.pos_x < -100:
            self.kill()
 
class Ranged_attack(pg.sprite.Sprite):
    def __init__(self, x, y): # denne funksjonen kjører når vi lager player
        pg.sprite.Sprite.__init__(self)
        self.image = ranged_image
        self.rect = self.image.get_rect()
        self.image.set_colorkey((255,255,255))
 
        self.pos_x = x
        self.pos_y = y
        self.speed = 10
 
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
 
    def update(self):
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
 
        self.pos_x += self.speed # beveger til høyre