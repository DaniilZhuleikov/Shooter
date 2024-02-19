from pygame import *
from time import sleep


win_height = 500
win_width = 700
window = display.set_mode((win_width,win_height))
display.set_caption("Лабиринт")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, width, height, wall_x, wall_y, angle, wall_image):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = width
        self.height = height
        self.angle = angle
        self.image = Surface((self.width, self.height))
        self.image = transform.scale(image.load(wall_image), (self.width, self.height))
        self.rect = self.image.get_rect()
        self.image = transform.rotate(self.image, self.angle)
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, hight):
        super().__init__()
        self.width = width
        self.hight = hight
        self.image = transform.scale(image.load(player_image),(self.width, self.hight))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height-40:
            self.rect.y += self.speed
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < win_width-40:
            self.rect.x += self.speed



class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
        if self.rect.x <= 450:
            self.direction = "right"
        if self.rect.x >= 590:
            self.direction = "left"
class Enemy2(GameSprite):
    direction = "left"
    def update(self):
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
        if self.rect.x <= 50:
            self.direction = "right"
        if self.rect.x >= 300:
            self.direction = "left"

clock = time.Clock()
FPS = 60

player = Player("hero.png", 5, win_height-80, 3, 65, 65)
enemy = Enemy("cyborg.png", win_width-80, 280, 2, 100, 70)
enemy2 = Enemy2("cyborg.png", 100, 80, 3, 100, 70)
treasure = GameSprite("treasure.png", win_width-120, win_height-80, 0, 65, 65)
wall1 = Wall(0, 149, 70, 10, 310, 200,100,0, 'bebada99aaa9847746eea59472544575_XL.jpg')
wall2 = Wall(0, 149, 70, 10, 450, 110,80, 0, 'bebada99aaa9847746eea59472544575_XL.jpg')
wall3 = Wall(0, 149, 70, 10, 450, 300,80, 0, 'bebada99aaa9847746eea59472544575_XL.jpg')
wall4 = Wall(0, 149, 70, 15, 50, 200,10, 0, 'bebada99aaa9847746eea59472544575_XL.jpg')
wall5 = Wall(0, 149, 70, 40, 350, 400,80, 0, 'bebada99aaa9847746eea59472544575_XL.jpg')
wall6 = Wall(0, 149, 70, 15, 230, 380,400, 90, 'bebada99aaa9847746eea59472544575_XL.jpg')
wall7 = Wall(0, 149, 70, 15, 30, 400,450, 0, 'bebada99aaa9847746eea59472544575_XL.jpg')

mixer.init()
font.init()
font = font.Font(None, 70)
mixer.music.load("jungles.ogg")
mixer.music.play()
kick = mixer.Sound("kick.ogg")
money = mixer.Sound("money.ogg")
game = True
finish = False
one_sound = True
second_level = False
while game:
    clock.tick(FPS)
    if not second_level and not finish:
        if sprite.collide_rect(player, treasure):
            finish = True
            win = font.render("YOU WIN!", True, (255, 215, 0))
            window.blit(win, (200, 200))
            if one_sound:
                money.play()
                one_sound = False
            keys_pressed = key.get_pressed()
            if keys_pressed[K_r]:
                player.rect.x = 5
                player.rect.y = win_height - 80
                finish = False
            if keys_pressed[K_l]:
                player.rect.x = 600
                player.rect.y = win_height - 500
                finish = False
        if sprite.collide_rect(player, enemy) or sprite.collide_rect(player, enemy2) or sprite.collide_rect(player,
                                                                                                            wall1) or sprite.collide_rect(
                player, wall2) or sprite.collide_rect(player, wall3) or sprite.collide_rect(player,
                                                                                            wall4) or sprite.collide_rect(
                player, wall5) or sprite.collide_rect(player, wall6) or sprite.collide_rect(player, wall7):
            finish = True
            loose = font.render("YOU LOST!", True, (180, 0, 0))
            window.blit(loose, (200, 200))
            if one_sound:
                kick.play()
                one_sound = False
            if keys_pressed[K_r]:
                player.rect.x = 5
                player.rect.y = win_height - 80
                finish = False
        window.blit(background, (0, 0))
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()
        wall7.draw_wall()
        player.reset()
        enemy.reset()
        treasure.reset()
        player.update()
        enemy.update()

    for e in event.get():
        if e.type == QUIT:
            game = False
    keys_pressed = key.get_pressed()
    if keys_pressed[K_n]:
        second_level = True
        enemy.kill()
        wall2.kill()
        wall3.kill()
        wall4.kill()
        wall5.kill()
        wall6.kill()
        wall7.kill()
        player.rect.x = 600
        player.rect.y = win_height - 500
        treasure.rect.x = 30
        treasure.rect.y = 430
    if second_level and not finish:
        window.blit(background, (0, 0))
        wall1.draw_wall()
        player.reset()
        treasure.reset()
        player.update()
        enemy2.reset()
        enemy2.update()
    display.update()
