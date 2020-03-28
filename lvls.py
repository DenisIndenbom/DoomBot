import pygame
import os
import sys
import loder

from pygame.transform import scale

resource_folder = os.path.dirname( sys.argv[0] )


def load_image( fileName ):
  return pygame.image.load( os.path.join( resource_folder, fileName ) )
class Terminal(pygame.sprite.Sprite):
    def __init__( self, x, y ):
        pygame.sprite.Sprite.__init__( self )
        self.rect = pygame.Rect( x, y, 47*2, 60*2 )
        self.image = loder.return_image( 12 )
    def draw( self, screen ):
        self.rect.x -= player.xcamera
        if player.rect.colliderect( self.rect ):
            txt = pygame.font.SysFont( 'Comic Sans MS', 20 )
            text = txt.render( 'e - прочитать.', False, (255, 255, 255) )
            screen.blit( text,( self.rect.x, self.rect.y - 60 ) )
        screen.blit( self.image, (self.rect.x, self.rect.y) )
class Lift(pygame.sprite.Sprite):
    def __init__( self, x, y ):
        pygame.sprite.Sprite.__init__( self )
        self.rect = pygame.Rect( x, y, 200, 250 )
        self.image = loder.return_image(20)
    def draw( self, screen, open=False ):
        self.rect.x -= player.xcamera
        if open:
            self.image = loder.return_image(21)
        else:
            self.image = loder.return_image(20)
        if player.rect.colliderect( self.rect ):
            txt = pygame.font.SysFont( 'Comic Sans MS', 20 )
            text = txt.render( 'e - выйти с уровня', False, (255, 255, 255) )
            screen.blit( text,( self.rect.x, self.rect.y - 60 ) )
        screen.blit( self.image, (self.rect.x, self.rect.y) )
class Fon(pygame.sprite.Sprite):
    def __init__( self, x, y ):
        pygame.sprite.Sprite.__init__( self )
        self.Rect = pygame.Rect( x, y, 1280, 720 )
        self.image = loder.return_image(0)

    def draw( self, screen ):
        self.Rect.x -= player.xcamera
        screen.blit( self.image, (self.Rect.x, self.Rect.y) )
class Fon2(pygame.sprite.Sprite):
    def __init__( self, x, y ):
        pygame.sprite.Sprite.__init__( self )
        self.Rect = pygame.Rect( x, y, 1280, 720 )
        self.image = loder.return_image(15)

    def draw( self, screen ):
        self.Rect.x -= player.xcamera
        screen.blit( self.image, (self.Rect.x, self.Rect.y) )
class Fon3(pygame.sprite.Sprite):
    def __init__( self, x, y ):
        pygame.sprite.Sprite.__init__( self )
        self.Rect = pygame.Rect( x, y, 1280, 720 )
        self.image = loder.return_image(17)

    def draw( self, screen ):
        self.Rect.x -= player.xcamera
        screen.blit( self.image, (self.Rect.x, self.Rect.y) )
class Fon4(pygame.sprite.Sprite):
    def __init__( self, x, y ):
        pygame.sprite.Sprite.__init__( self )
        self.Rect = pygame.Rect( x, y, 1280, 720 )
        self.image = loder.return_image(18)

    def draw( self, screen ):
        self.Rect.x -= player.xcamera
        screen.blit( self.image, (self.Rect.x, self.Rect.y) )
class Fon5(pygame.sprite.Sprite):
    def __init__( self, x, y, text='' ):
        pygame.sprite.Sprite.__init__( self )
        self.Rect = pygame.Rect( x, y, 1280, 720 )
        self.image = loder.return_image(19)
        txt = pygame.font.SysFont( 'Comic Sans MS', 100 )
        self.text = txt.render( text, False, (200, 200, 200) )

    def draw( self, screen ):
        self.Rect.x -= player.xcamera
        screen.blit( self.image, (self.Rect.x, self.Rect.y) )
        screen.blit( self.text, (self.Rect.x+400, self.Rect.y+250) )
class Life(pygame.sprite.Sprite):
    def __init__( self, x, y ):
        pygame.sprite.Sprite.__init__( self )
        self.Rect = pygame.Rect( x, y, 30, 35 )
        self.image = loder.return_image( 11 )
        self.f = 0

    def fall( self ):
        self.Rect.y += (1 * 9.8) / 3 - 2
    def draw( self, screen ):
        try:
            stay = 0
            for i in range( len( platforms ) ):
                if self.Rect.colliderect( platforms[i].Rect ):
                    stay = 1
                    self.f = 1
            if stay == 1:
                self.f = 1
            else:
                self.f = 0
        except:
            self.f = 0
        try:
            for i in range( len( object1 ) ):
                if self.Rect.colliderect( object1[i].Rect ):
                    self.f = 1
                # else:
                #     self.f = 0
        except:
            self.f = 0
        if self.f == 0:
            self.fall()
        self.Rect.x -= player.xcamera
        screen.blit( self.image, (self.Rect.x, self.Rect.y) )
class PLatform(pygame.sprite.Sprite):
    def __init__( self, x, y ):
        pygame.sprite.Sprite.__init__( self )
        self.Rect = pygame.Rect( x, y, 176, 10 )
        self.image = loder.return_image( 10 )

    def draw( self, screen ):
        self.Rect.x -= player.xcamera
        screen.blit( self.image, (self.Rect.x, self.Rect.y) )
# class PLatform2(pygame.sprite.Sprite):
#     def __init__( self, x, y, minx=0, maxx=0 ):
#         pygame.sprite.Sprite.__init__( self )
#         self.Rect = pygame.Rect( x, y, 176, 10 )
#         self.image = loder.return_image( 10 )
#         self.minx = minx
#         self.maxx = maxx
#         self.on = True
#         self.state = 1
#         self.xvel = 0
#     def draw( self, screen,on=True ):
#         self.xvel = 0
#         player.xvelp = 0
#         if self.on:
#             self.xvel += 5 * self.state
#         self.maxx -= player.xcamera
#         self.minx -= player.xcamera
#         if self.on:
#             if self.Rect.x > self.maxx:
#                 self.state = -1
#             elif self.Rect.x < self.minx:
#                 self.state = 1
#         if player.leg_rect.colliderect( self.Rect ):
#             player.xcamera += self.xvel
#         else:
#             self.Rect.x += self.xvel
#             self.Rect.x -= player.xcamera
#         screen.blit( self.image, (self.Rect.x, self.Rect.y) )
class object( pygame.sprite.Sprite ):
  def __init__( self, x, y ):
    pygame.sprite.Sprite.__init__( self )
    self.Rect = pygame.Rect( x, y, 1280, 50 )
    self.image = loder.return_image(2)

  def draw( self, screen ):
    self.Rect.x -= player.xcamera
    screen.blit( self.image, (self.Rect.x, self.Rect.y) )

class potronbot(pygame.sprite.Sprite):
    def __init__(self,x,y,state,damage):
        pygame.sprite.Sprite.__init__( self )
        self.state = 1
        self.image = loder.return_image(8)
        self.rect = pygame.Rect( x, y, 40, 15 )
        self.xvel = 0
        self.state = state
        self.damage = damage

    def draw( self, screen ):
        screen.blit( self.image, (self.rect.x, self.rect.y) )

    def fire(self):
        if self.rect.x < 0 or self.rect.x > 1280:
            self.kill()
        if self.state == -1:
            self.image = pygame.transform.flip( loder.return_image( 8 ), 1, 0 )
        else:
            self.image = loder.return_image( 8 )
        self.xvel = 10 * self.state
        self.rect.x += self.xvel
        self.rect.x -= player.xcamera
class potron(pygame.sprite.Sprite):
    def __init__(self,x,y,state,damage):
        pygame.sprite.Sprite.__init__( self )
        self.state = 1
        self.image = loder.return_image(3)
        self.rect = pygame.Rect( x, y, 40, 15 )
        self.xvel = 0
        self.state = state
        self.damage = damage

    def draw( self, screen ):
        screen.blit( self.image, (self.rect.x, self.rect.y) )

    def fire(self):
        if self.rect.x < 0 or self.rect.x > 1280:
            self.kill()
        if self.state == -1:
            self.image = pygame.transform.flip( loder.return_image( 3 ), 1, 0 )
        else:
            self.image = loder.return_image( 3 )
        self.xvel = 10 * self.state
        self.rect.x += self.xvel
        self.rect.x -= player.xcamera

class potron2(pygame.sprite.Sprite):
    def __init__(self,x,y,state,spread,damage):
        pygame.sprite.Sprite.__init__( self )
        self.state = 1
        self.image = loder.return_image(3)
        self.rect = pygame.Rect(x, y, 40, 15)
        self.xvel = 0
        self.yvel = 0
        self.spread = spread
        self.state = state
        self.damage = damage
    def draw( self, screen ):
        screen.blit( self.image, (self.rect.x, self.rect.y) )

    def fire(self):
        self.yvel = 0
        if self.rect.x < 0 or self.rect.x > 1280:
            self.kill()
        if self.state == -1:
            self.image = pygame.transform.flip( loder.return_image( 3 ), 1, 0 )
        else:
            self.image = loder.return_image( 3 )
        self.xvel = 10 * self.state
        self.yvel += self.spread
        self.rect.x += self.xvel
        self.rect.x -= player.xcamera
        self.rect.y += self.yvel
class bot2(pygame.sprite.Sprite):
    def __init__(self, x ,y):
        pygame.sprite.Sprite.__init__( self )
        self.image = loder.return_image( 7 )
        self.rect = pygame.Rect( x, y, 60, 63 )
        self.time = 0
        self.state = 1
        self.potron = []
        self.xvel = 0
        self.yvel = 0
        self.life = 40
        self.on = 0
        self.death = False
        self.f = 0
        self.Del = False
        self.Deltime = 300
    def draw( self, screen ):
        screen.blit( self.image, (self.rect.x, self.rect.y) )

    def fall( self ):
        self.yvel += (3 * 9.8) / 3 - 2
    def update(self):
        self.xvel = 0
        self.yvel = 0
        if player.rect.x > self.rect.x - 300 and player.rect.x < self.rect.x + 300 or self.life < 40:
                self.on = True
        else:
                self.on = False
        if self.life <= 0:
            self.death = True
            self.image = loder.return_image( 22 )
            self.on = False
        if self.death:
            self.Deltime -= 1
        if self.Deltime <= 0:
            self.Del = True
        try:
            stay = 0
            for i in range(len(platforms)):
                if self.rect.colliderect(platforms[i].Rect):
                    stay = 1
                    self.f = 1
            if stay == 1:
                self.f = 1
            else:
                self.f = 0
        except:
            self.f = 0
        try:
            for i in range( len( object1 ) ):
                if self.rect.colliderect( object1[i].Rect ):
                    self.f = 1
                # else:
                #     self.f = 0
        except:
            self.f = 0
        if self.on:
            if player.rect.x > self.rect.x:
                self.state = -1
                if self.rect.x < player.rect.x - 60 or self.rect.x > player.rect.x + 60:
                    self.xvel += 4
            else:
                self.state = 1
                if self.rect.x < player.rect.x - 60 or self.rect.x > player.rect.x + 60:
                    self.xvel -= 4
            if self.rect.y == player.rect.y or self.rect.y - player.rect.y > 0 and self.rect.y - player.rect.y < 60 and not self.death:
                if self.time <= 0:
                        if self.state == 1:
                            l = -20
                        else:
                            l = 60
                        self.potron.append( potronbot( self.rect.x + l, self.rect.y + 25, self.state * -1, 10 ) )
                        self.time = 20
                else:
                    self.time -= 1
            if self.state == -1:
                self.image = pygame.transform.flip( loder.return_image( 7 ), 1, 0 )
            else:
                self.image = loder.return_image( 7 )
            for i in range( len( bots ) ):
                if self.rect.x > bots[i].rect.x - 60 and self.rect.x < bots[i].rect.x + 60 and not bots[i].death:
                    if self.rect.x == bots[i].rect.x:
                        pass
                    elif self.rect.x > bots[i].rect.x:
                        self.xvel += 4
                    else:
                        self.xvel -= 4
        if self.f == 0:
            self.fall()
        if self.death == False:
            self.rect.x += self.xvel
        self.rect.x -= player.xcamera
        self.rect.y += self.yvel
class bot1(pygame.sprite.Sprite):
    def __init__(self, x ,y):
        pygame.sprite.Sprite.__init__( self )
        self.image = loder.return_image( 9 )
        self.rect = pygame.Rect( x, y, 60, 65 )
        self.leg_rect = pygame.Rect( x, y, 30, 8 )
        self.f = 0
        self.jump = 30
        self.isjump = False
        self.time = 0
        self.state = 1
        self.potron = []
        self.xvel = 0
        self.yvel = 0
        self.life = 30
        self.on = False
        self.jumpwas = False
        self.death = False
        self.Del = False
        self.Deltime = 300
    def draw( self, screen ):
        screen.blit( self.image, (self.rect.x, self.rect.y) )

    def fall( self ):
        self.yvel += 3
    def update(self):
        self.xvel = 0
        self.yvel = 0
        if player.rect.x > self.rect.x - 300 and player.rect.x < self.rect.x + 300 or self.life < 30:
                self.on = True
        else:
                self.on = False
        if self.life <= 0:
            self.death = True
            self.image = loder.return_image(23)
            self.on = False
        if self.death:
            self.Deltime -= 1
        if self.Deltime <= 0:
            self.Del = True
        if self.on:
            if player.rect.x > self.rect.x:
                self.state = -1
                if self.rect.x < player.rect.x - 60 or self.rect.x > player.rect.x + 60:
                    self.xvel += 5
            else:
                self.state = 1
                if self.rect.x < player.rect.x - 60 or self.rect.x > player.rect.x + 60:
                    self.xvel -= 5
            if self.rect.y == player.rect.y or self.rect.y - player.rect.y > 0 and self.rect.y - player.rect.y < 60 and not self.death:
                if self.time <= 0:
                        if self.state == 1:
                            l = -20
                        else:
                            l = 60
                        self.potron.append( potronbot( self.rect.x + l, self.rect.y + 25, self.state * -1, 10 ) )
                        self.time = 30
                else:
                        self.time -= 1
            if self.state == 1:
                self.image = pygame.transform.flip( loder.return_image( 9 ), 1, 0 )
            else:
                self.image = loder.return_image( 9 )
        try:
            stay = 0
            for i in range(len(platforms)):
                if self.leg_rect.colliderect(platforms[i].Rect) and not self.isjump:
                    stay = 1
                    self.f = 1
            if stay == 1:
                self.f = 1
            else:
                self.f = 0
        except:
            self.f = 0
        try:
            for i in range( len( object1 ) ):
                if self.leg_rect.colliderect( object1[i].Rect ):
                    self.f = 1
                # else:
                #     self.f = 0
        except:
            self.f = 0
        if self.on:
            if self.rect.y - player.rect.y > 100:
                if self.f == 1:
                    if self.jumpwas == False:
                        self.isjump = True
            for i in range(len(bots)):
                if self.rect.x > bots[i].rect.x - 60 and self.rect.x < bots[i].rect.x + 60 and not bots[i].death:
                    if self.rect.x == bots[i].rect.x:
                        pass
                    elif self.rect.x > bots[i].rect.x:
                        self.xvel += 5
                    else:
                        self.xvel -= 5

        if self.death:
            self.jumpwas = False
        if not self.death:
            if self.isjump:
                if int(self.jump) >= 0:
                    self.yvel -= (self.jump ** 2) / 70
                    self.jump -= 1
                    self.f = 1
                    self.jumpwas = True
                else:
                    self.jumpwas = False
                    self.isjump = False
                    self.jump = 30
                    self.f = 0
        # else:
        #     self.f = 0

        if self.f == 0:
            self.fall()
        if self.death == False:
            self.rect.x += self.xvel
        self.rect.x -= player.xcamera
        if self.death == False:
            self.leg_rect.x += self.xvel
        self.leg_rect.x -= player.xcamera
        self.rect.y += self.yvel
        self.leg_rect.y = self.rect.y + 50
class Gun1( pygame.sprite.Sprite ):
    def __init__( self, x, y, taken ):
        pygame.sprite.Sprite.__init__( self )
        self.image = loder.return_image( 4 )
        self.rect = pygame.Rect( x, y, 30, 30 )
        self.time = 0
        self.state = 1
        self.potron = []
        self.taken = taken
        self.taken_init()

    def taken_init( self ):
        if self.taken:
            player.gun.append( self )

    def draw( self, screen ):
        screen.blit( self.image, (self.rect.x, self.rect.y) )

    def fire( self, state) :
        if self.taken:
            self.state = state
            if self.time <= 0:
                sound_gun1.play()
                if self.state == -1:
                    l = -20
                else:
                    l = 100
                self.potron.append( potron( self.rect.x + l, self.rect.y + 5, self.state, 15 ) )
                self.time = 15
            else:
                self.time -= 1

    def update( self, state):
        self.state = state
        if not self.taken:
            if self.rect.colliderect( player.rect ):
                self.taken = True
                player.gun.append(self)
        if self.taken:
            if self.state == 1:
                self.rect.x = player.rect.x + 10
            else:
                self.rect.x = player.rect.x - 60
            self.rect.y = player.rect.y + 30
        if self.taken:
            if self.state == -1:
                self.image = pygame.transform.flip( loder.return_image( 4 ), 1, 0 )
            else:
                self.image = loder.return_image( 4 )
        self.rect.x -= player.xcamera
class Gun2(pygame.sprite.Sprite):
    def __init__( self, x, y, taken ):
        pygame.sprite.Sprite.__init__( self )
        self.image = loder.return_image( 5 )
        self.rect = pygame.Rect( x, y, 30, 30 )
        self.time = 0
        self.state = 1
        self.potron = []
        self.taken = taken
        self.taken_init()

    def taken_init( self ):
        if self.taken:
            player.gun.append( self )
    def draw( self, screen ):
        screen.blit( self.image, (self.rect.x, self.rect.y) )

    def fire( self, state):
        if self.taken:

            self.state = state
            if self.time <= 0:
                sound_gun2.play()
                if self.state == -1:
                    l = -20
                else:
                    l = 100
                self.potron.append(potron2( self.rect.x + l, self.rect.y + 5, self.state, 2 , 10))
                self.potron.append( potron2( self.rect.x + l, self.rect.y + 5, self.state, -2, 10 ))
                self.potron.append( potron2( self.rect.x + l, self.rect.y + 5, self.state, 4, 10 ) )
                self.potron.append( potron2( self.rect.x + l, self.rect.y + 5, self.state, -4, 10 ) )
                self.potron.append( potron2( self.rect.x + l, self.rect.y + 5, self.state, 0, 10 ) )
                self.time = 30
            else:
                self.time -= 1
    def update( self, state):
        self.state = state
        if self.taken == False:
            if self.rect.colliderect( player.rect ):
                self.taken = True
                player.gun.append(self)
        if self.taken:
            if self.state == 1:
                self.rect.x = player.rect.x + 10
            else:
                self.rect.x = player.rect.x - 60
            self.rect.y = player.rect.y + 30
        if self.taken:
            if self.state == -1:
                self.image = pygame.transform.flip( loder.return_image( 5 ), 1, 0 )
            else:
                self.image = loder.return_image( 5 )
        self.rect.x -= player.xcamera
class Gun3( pygame.sprite.Sprite ):
    def __init__( self, x, y, taken ):
        pygame.sprite.Sprite.__init__( self )
        self.image = loder.return_image( 6 )
        self.rect = pygame.Rect( x, y, 30, 30 )
        self.time = 0
        self.state = 1
        self.potron = []
        self.taken = taken
        self.taken_init()
    def taken_init( self ):
        if self.taken:
            player.gun.append(self)
    def draw( self, screen ):
        screen.blit( self.image, (self.rect.x, self.rect.y) )

    def fire( self, state) :
        if self.taken:
            self.state = state
            if self.time <= 0:
                sound_gun3.play()
                if self.state == -1:
                    l = -20
                else:
                    l = 30
                self.potron.append( potron( self.rect.x + l, self.rect.y, self.state, 10 ) )
                self.time = 30
            else:
                self.time -= 1

    def update( self, state):
        self.state = state
        if not self.taken:
            if self.rect.colliderect( player.rect ):
                self.taken = True
                player.gun.append(self)
        if self.taken:
            if self.state == 1:
                self.rect.x = player.rect.x + 20
            else:
                self.rect.x = player.rect.x - 20
            self.rect.y = player.rect.y + 30
        if self.taken:
            if self.state == -1:
                self.image = pygame.transform.flip( loder.return_image( 6 ), 1, 0 )
            else:
                self.image = loder.return_image( 6 )
        self.rect.x -= player.xcamera
class Player( pygame.sprite.Sprite ):
  def __init__( self, x, y, on_camera=False,xmin=0,xmax=0):
    pygame.sprite.Sprite.__init__( self )
    self.animFrame = 0
    self.idle = True
    self.isjump = False
    self.f = 0
    self.jump = 30
    self.xmin = xmin
    self.xmax = xmax
    self.rect = pygame.Rect( x, y, 65, 78 )
    self.leg_rect = pygame.Rect( x, y, 40, 8 )
    self.image = loder.return_image(1)
    self.xvel = 0
    self.yvel = 0
    self.time = 0
    self.state = 1
    self.gun = []
    self.anim = loder.load_anim()
    self.anim2 = loder.load_anim_idle()
    self.numGun = 0
    self.death = False
    self.on_camera = on_camera
    self.xcamera = 0
    self.xpcamera = self.rect.x
    self.xvelp = 0
    # добавим кораблю здоровье
    self.life = 100


  def draw( self, screen ):
    screen.blit( self.image, (self.rect.x, self.rect.y) )

  def fall( self ):
    self.yvel += (3 * 9.8) / 3 - 2
    #self.rect.y += self.yvel

  # добавим группу с астероидами в обновление координат корабля
  def update( self, left, right, up, fire, num ):
    self.xvel = 0
    self.yvel = 0
    self.xcamera = 0
    text = font.render( f'{self.life}hp', False, (255, 0, 0) )
    screen.blit( text, (20, 20) )

    if num - 1 < len(self.gun):
        self.numGun = num - 1
    # if botek.game_settings.state_object == 1:

    try:
        for i in range(len(life1)):
            if self.rect.colliderect( life1[i].Rect ):
                self.life += 30
        i = len( life1 )
        if i >= 1:
            while True:
                i -= 1
                if player.rect.colliderect( life1[i].Rect ):
                    life1.pop( i )
                if i == 0:
                    break
    except:
        pass
    if left and self.rect.x > 3:
      self.xvel = -6
      self.state = -1
    if right and self.rect.x < 1230:
      self.xvel = 6
      self.state = 1
    if fire:
        if len(self.gun) == 0:
            text = font.render( 'У тебя нет оружия!!', False, (255, 255, 255) )
            screen.blit( text, (500, 50) )
        else:
            self.gun[self.numGun].fire(self.state)
    if up:
      if self.f == 1:
        self.isjump = True
    if self.state == -1:
        self.image = pygame.transform.flip(loder.return_image(1), 1, 0)
    else:
        self.image = loder.return_image(1)
    try:
        stay = 0
        for i in range(len(platforms)):
            if self.leg_rect.colliderect(platforms[i].Rect) and not self.isjump:
                    stay = 1
                    self.f = 1
        if stay == 1:
            self.f = 1
        else:
            self.f = 0
    except:
        self.f = 0
    try:
        for i in range(len(object1)):
            if self.leg_rect.colliderect( object1[i].Rect ):
                    self.f = 1
    except:
        self.f = 0
    if self.isjump:
      if int( self.jump ) >= 0:
        self.yvel -= (self.jump ** 2) / 70
        self.jump -= 1
        self.f = 1
      else:
        self.isjump = False
        self.jump = 30
        self.f = 0
        # self.yvel = 0
    if not (left and right and up):
      self.idle = True

    else:
      self.idle = False
    if right:
        if self.animFrame == 60:
            self.animFrame = 0
            #self.image = scale( load_image( "player.png" ), (60, 74) )
            self.idle = True
        else:
            self.image = self.anim[self.animFrame // 9]
            self.animFrame += 1
            self.idle = False
    if left:
        if self.animFrame == 60:
            self.animFrame = 0
            #self.image = scale( load_image( "player.png" ), (60, 74) )
            self.idle = True
        else:
            self.image = pygame.transform.flip(self.anim[self.animFrame // 9], 1, 0)
            self.animFrame += 1
            self.idle = False
    if self.f == 0:
      self.fall()

    if self.life <= 0:
        self.death = True
    self.xpcamera += self.xvel
    if self.on_camera and self.xpcamera > self.xmin and self.xpcamera < self.xmax:
        if self.xvelp != 0:
            self.xcamera += self.xvelp
        else:
            self.xcamera += self.xvel


    else:
        self.rect.x += self.xvel
        self.leg_rect.x = self.rect.x
    self.rect.y += self.yvel
    self.leg_rect.y = self.rect.y + 70


pygame.init()
pygame.display.set_caption("DoomBot-Alpha")
sound_gun1 = pygame.mixer.Sound('gun1.wav')
sound_gun2 = pygame.mixer.Sound('gun2.wav')
sound_gun3 = pygame.mixer.Sound('gun3.wav')
screen = pygame.display.set_mode( (1280, 720)  ) #,pygame.FULLSCREEN
sky = loder.return_image( 16 )
pygame.font.init()
font = pygame.font.SysFont( 'Comic Sans MS', 40 )
name = pygame.font.SysFont('Comic Sans MS',100)
# game_settings = Game.game_settings(1,1,object1)
left = False
right = False
up = False
fire = False
num = 0
Win = False
def start_first_episode():
        pygame.mixer.music.stop()
        e = pygame.event.poll()
        if e.type == pygame.QUIT:
            raise SystemExit( "QUIT" )
        screen.blit( loder.return_image(14), (0, 0) )
        txt = pygame.font.SysFont( 'Comic Sans MS', 100 )
        text = txt.render( 'Start System', False, (255, 255, 255) )
        screen.blit( text, (300, 50) )
        pygame.display.update()
        pygame.time.delay(1000)
        txt = pygame.font.SysFont( 'Comic Sans MS', 30 )
        text = txt.render( 'Check HDD...', False, (255, 255, 255) )
        screen.blit( text, (100, 200) )
        pygame.display.update()
        pygame.time.delay(500)
        text = txt.render( 'ok', False, (255, 255, 255) )
        screen.blit( text, (300, 200) )
        pygame.display.update()
        pygame.time.delay( 1000 )
        text = txt.render( 'Check OS...', False, (255, 255, 255) )
        screen.blit( text, (100, 250) )
        pygame.display.update()
        pygame.time.delay( 500 )
        text = txt.render( 'ok', False, (255, 255, 255) )
        screen.blit( text, (300, 250) )
        pygame.display.update()
        pygame.time.delay( 1000 )
        text = txt.render( 'Основная цель: Уничтожить захватчиков и предвратить разрушения комплекса', False, (255, 255, 255) )
        screen.blit( text, (100, 300) )
        pygame.display.update()
        pygame.time.delay( 1000 )
        text = txt.render( 'DoomBot activate...', False, (255, 255, 255) )
        screen.blit( text, (100, 350) )
        pygame.display.update()
        pygame.time.delay( 1000 )
        text = txt.render( '[space - выйти]', False, (0, 255, 0) )
        screen.blit( text, (400, 500) )
def terminal_history():
    # pygame.mixer.music.stop()
    global left
    global right
    global up
    global fire
    global yes
    while True:
        e = pygame.event.poll()
        if e.type == pygame.QUIT:
            raise SystemExit( "QUIT" )
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            left = False
            right = False
            up = False
            fire = False
            yes = False
            break
        screen.blit( loder.return_image(13), (0, 0) )
        txt = pygame.font.SysFont( 'Comic Sans MS', 100 )
        text = txt.render( 'Внимание!', False, (0, 255, 0) )
        screen.blit( text, (300, 100) )
        txt = pygame.font.SysFont( 'Comic Sans MS', 30 )
        text = txt.render( 'info:Произошло заражение комплекса вирусом на 95%.', False, (0, 255, 0) )
        screen.blit( text, (100, 250) )
        text = txt.render( 'info:Источник зарожения не найден.', False, (0, 255, 0) )
        screen.blit( text, (100, 300) )
        text = txt.render( 'info:Комплекс переходит протоколу к "Security Protocol". ', False, (0, 255, 0) )
        screen.blit( text, (100, 350) )
        text = txt.render('Error: потерян контроль температуры плазменного реактора!', False, (0, 255, 0) )
        screen.blit( text, (100, 400) )
        text = txt.render( 'info: реактор через час достигнет  красной зоны', False, (0, 255, 0) )
        screen.blit( text, (100, 450) )
        text = txt.render( '[space - выйти]', False, (0, 255, 0) )
        screen.blit( text, (400, 500) )
        pygame.display.update()
    # pygame.mixer.music.play()
def lose():
    global num
    while True:
        e = pygame.event.poll()
        if e.type == pygame.QUIT:
            raise SystemExit("QUIT")
        if e.type == pygame.KEYDOWN and e.key == pygame.K_e:
            break
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            num = 0
            break
        screen.blit( sky, (0, 0) )
        txt = pygame.font.SysFont('Comic Sans MS', 100)
        text = txt.render('Ты умер', False, (255, 0, 0))
        screen.blit(text, (400, 100))
        txt = pygame.font.SysFont('Comic Sans MS', 40)
        text = txt.render('e-перезапустить уровень', False, (255, 255, 255))
        screen.blit(text,(450, 250))
        pygame.display.update()
def win():

    while True:
        e = pygame.event.poll()
        if e.type == pygame.QUIT:
            raise SystemExit("QUIT")
        if e.type == pygame.KEYDOWN and e.key == pygame.K_e:
            break
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            num = 0
            break
        screen.blit( sky, (0, 0) )
        txt = pygame.font.SysFont('Comic Sans MS', 100)
        text = txt.render('Этаж пройден!!!!', False, (255, 0, 0))
        screen.blit(text, (310, 100))
        txt = pygame.font.SysFont('Comic Sans MS', 40)
        text = txt.render('e-продолжить', False, (255, 255, 255))
        screen.blit(text,(450, 250))
        pygame.display.update()
def menu():
    global Win
    global num
    pygame.mixer.music.load( 'E1M10.mp3' )
    pygame.mixer.music.play()
    while True:
        num = 0
        e = pygame.event.poll()
        if e.type == pygame.KEYDOWN and e.key == pygame.K_e:
            while True:
                event = pygame.event.poll()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                    num = 1
                if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                    num = 2
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    break
                if event.type == pygame.QUIT:
                    raise SystemExit("QUIT")
                screen.blit(sky, (0, 0))
                text = name.render('DoomBot-Alpha', False, (255, 30, 0))
                screen.blit(text, (300, 150))
                text = font.render('1- Первый уровень', False, (255, 255, 255))
                screen.blit(text, (500, 300))
                text = font.render('2- Второе уровень', False, (255, 255, 255))
                screen.blit(text, (500, 400))
                pygame.display.update()
                if num == 1:
                    lvl1()
                    if Win:
                        pygame.mixer.music.load( 'E1M10.mp3' )
                        pygame.mixer.music.play()
                        win()
                        Win = False
                        num = 2
                    else:
                        pygame.mixer.music.load( 'E1M10.mp3' )
                        pygame.mixer.music.play()
                        lose()
                if num == 2:
                    lvl2()
                    if Win:
                        pygame.mixer.music.load( 'E1M10.mp3' )
                        pygame.mixer.music.play()
                        win()
                        Win = False
                    else:
                        pygame.mixer.music.load( 'E1M10.mp3' )
                        pygame.mixer.music.play()
                        num = 2
                        lose()

        if e.type == pygame.KEYDOWN and e.key == pygame.K_h:
            while True:
                event = pygame.event.poll()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    break
                screen.blit(sky, (0, 0))
                text = name.render('DoomBot-Alpha', False, (255, 30, 0))
                screen.blit(text, (300, 150))
                text = font.render('Перемещени-стрелки', False, (255, 255, 255))
                screen.blit(text, (500, 300))
                text = font.render('стрельба-space', False, (255, 255, 255))
                screen.blit(text, (500, 400))
                text = font.render('Менять оружие-цифры', False, (255, 255, 255))
                screen.blit(text, (500, 500))
                text = font.render('Выйти-esc', False, (255, 255, 255))
                screen.blit(text, (500, 600))
                pygame.display.update()
                if event.type == pygame.QUIT:
                    raise SystemExit( "QUIT" )
        # if num == 1:
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            break
        if e.type == pygame.QUIT:
            raise SystemExit("QUIT")
        screen.blit(sky, (0, 0))
        text = name.render('DoomBot-Alpha', False, (255, 30, 0))
        screen.blit(text, (300, 150))
        text = font.render('e-Новая игра', False, (255, 255, 255))
        screen.blit(text, (500, 300))
        text = font.render('h-Управление', False, (255, 255, 255))
        screen.blit(text, (500, 400))
        text = font.render('esc-Выход', False, (255, 255, 255))
        screen.blit(text, (500, 500))
        pygame.display.update()
def control():
    global left
    global right
    global up
    global fire
    global screen
    global num
    global yes
    e = pygame.event.poll()
    if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
        up = True
    if e.type == pygame.KEYUP and e.key == pygame.K_UP:
        up = False
    if e.type == pygame.KEYDOWN and e.key == pygame.K_e:
        yes = True
    if e.type == pygame.KEYUP and e.key == pygame.K_e:
        yes = False
    if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
        right = True
    if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
        right = False
    if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
        left = True
    if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
        left = False
    if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
        fire = True
    if e.type == pygame.KEYUP and e.key == pygame.K_SPACE:
        fire = False
    if e.type == pygame.KEYDOWN and e.key == pygame.K_1:
        num = 1
    if e.type == pygame.KEYDOWN and e.key == pygame.K_2:
        num = 2
    if e.type == pygame.KEYDOWN and e.key == pygame.K_3:
        num = 3
    if e.type == pygame.KEYDOWN and e.key == pygame.K_4:
        num = 4
    if e.type == pygame.QUIT:
        raise SystemExit( "QUIT" )



def lvl1():
   start_first_episode()
   pygame.mixer.music.load( 'E1M1.mp3' )
   pygame.mixer.music.play()
   global num
   global player
   global gun1
   global gun3
   global gun2
   global object1
   global Win
   global left
   global right
   global up
   global fire
   global platforms
   global life1
   global yes
   global bots
   clock = pygame.time.Clock()

   left = False
   right = False
   up = False
   fire = False
   yes = False
   num = 0
   final = False
   fon = [Fon5(0,0,'Sector-C'),Fon2(1280,0),Fon4(2560,0)]
   player = Player(0, 500, True,640,3194)
   bots = [bot1( 1000, 605 ),bot1( 1500, 605 ),bot1( 1600, 605 )]
   terminal = Terminal(1100,548)
   lift = Lift(3000,420)
   #platforms = [PLatform(1200,560)]
   life1 = [Life(200,600)]
   object1 = [object( 0, 670 ),object( 1280, 670 ),object( 2560, 670 )]
   # gun1 = Gun1( 300, 600, taken=False )
   # gun2 = Gun2( 600, 600, taken=False )
   gun3 = Gun3( 300, 600, taken=False )
   def damageUpdate():
       global life
       for i in range(len(bots)):
           if bots[i].Del:
               bots.pop( i )
               break
       for numbot in range( len( bots ) ):
           ng = len( player.gun )
           if ng >= 1:
               while True:
                   ng -= 1
                   i = len( player.gun[ng].potron )
                   if i >= 1:
                       while True:
                           i -= 1
                           if bots[numbot].rect.colliderect( player.gun[ng].potron[i].rect ) and not bots[numbot].death:
                               bots[numbot].life -= player.gun[ng].potron[i].damage
                               player.gun[ng].potron.pop( i )
                           if i == 0:
                               break
                   if ng == 0:
                       break
           i = len( bots[numbot].potron )
           if i >= 1:
               while True:
                   i -= 1
                   if player.rect.colliderect( bots[numbot].potron[i].rect ):
                       player.life -= bots[numbot].potron[i].damage
                       bots[numbot].potron.pop( i )
                   if i == 0:
                       break
           try:
               i = len( bots[numbot].potron )
               if i >= 1:
                   while True:
                       i -= 1
                       for g in range( len( platforms ) ):
                           if bots[numbot].potron[i].rect.colliderect( platforms[g].Rect ):
                               bots[numbot].potron.pop( i )
                       if i == 0:
                           break
           except:
               pass
       try:
           ng = len( player.gun )
           if ng >= 1:
               while True:
                   ng -= 1
                   i = len( player.gun[ng].potron )
                   if i >= 1:
                       while True:
                           i -= 1
                           for g in range( len( platforms ) ):
                               if player.gun[ng].potron[i].rect.colliderect( platforms[g].Rect ):
                                   player.gun[ng].potron.pop( i )
                           if i == 0:
                               break
                   if ng == 0:
                       break
       except:
           pass
   def gunupdate():
       # gun1.update( player.state )
       # gun2.update( player.state )
       gun3.update( player.state )

   def gundraw():
       try:
           for i in range( len( gun1.potron ) ):
            gun1.potron[i].fire()
            gun1.potron[i].draw( screen )
       except:
           pass
       try:
           for i in range( len( gun2.potron ) ):
             gun2.potron[i].fire()
             gun2.potron[i].draw( screen )
       except:
           pass
       try:
          for i in range( len( gun3.potron ) ):
            gun3.potron[i].fire()
            gun3.potron[i].draw( screen )
       except:
           pass
   while True:
        control()
        for i in range( len( fon ) ):
            fon[i].draw( screen )
        for i in range(len(object1)):
            object1[i].draw( screen )
        terminal.draw(screen)
        lift.draw(screen,final)
        player.update( left, right, up, fire, num)
        gunupdate()
        gundraw()
        try:
            for i in range(len(platforms)):
                platforms[i].draw(screen)
        except:
            pass
        for i in range(len(bots)):
            bots[i].update()
            bots[i].draw(screen)
        for i in range(len(life1)):
            life1[i].draw(screen)
        player.draw( screen )
        for numbot in range(len(bots)):
            for i in range(len(bots[numbot].potron)):
                bots[numbot].potron[i].fire()
                bots[numbot].potron[i].draw(screen)
        if len( player.gun ) == 0:
            pass
        else:
            player.gun[player.numGun].draw( screen )
        try:
            if not gun1.taken:
                gun1.draw( screen )
        except:
            pass
        try:
            if not gun2.taken:
                gun2.draw(screen)
        except:
            pass
        try:
            if not gun3.taken:
                gun3.draw(screen)
        except:
            pass
        damageUpdate()
        if player.rect.colliderect( terminal.rect ):
            if yes:
                terminal_history()

        for i in range(len(bots)):
             if bots[i].death:
                 final = True
             else:
                 final = False
                 break
        if final:
            if player.rect.colliderect(lift.rect):
                    if yes:
                        Win = True
                        break
        if player.death:
           Win = False
           break
        pygame.display.update()
        clock.tick(90)
def lvl2():
   pygame.mixer.music.load('E1M1.mp3')
   pygame.mixer.music.play()
   global num
   global player
   global gun1
   global gun3
   global gun2
   global object1
   global Win
   global left
   global right
   global up
   global fire
   global platforms
   global life1
   global yes
   global bots
   clock = pygame.time.Clock()
   left = False
   right = False
   up = False
   fire = False
   yes = False
   num = 0
   final = False
   fon = [Fon5(0,0,'Sector-B'),Fon2(1280,0),Fon5(2560,0,'Sector-B'),Fon2(3840,0),Fon4(5120,0)]
   player = Player(0, 500, True,640,5750)
   bots = [bot1( 1000, 605 ),bot1( 1200, 605 ),bot2( 1600, 605 ),bot2(1400,400),bot2(1400+176*6,250),bot2(1400+170*4,250),bot2(1400+176*7,250),bot2(1400+170*5,250),bot2(1400+170*14,250),bot2(1400+170*10,250),bot1(1400+170*6,500),bot1(1400+170*20,500),bot2(1400+176*25,250),bot1(1400+170*8,250),bot2(1400+176*23,250),bot2(1400+150*26,250)]
   # terminal = Terminal(1100,578)
   lift = Lift(5500,420)
   platforms = [PLatform(1250,560),PLatform(1400,460),PLatform(1400+176,315),PLatform(1400+176*2,315),PLatform(1400+176*3,315),PLatform(1400+176*4,315),PLatform(1400+176*5,315),PLatform(1400+176*6,315),PLatform(1400+176*7,315),PLatform(1400+176*15,510),PLatform(1400+176*16,230)]
   life1 = [Life(200,600),Life(1100,300),Life(1400+176,345),Life(1400+176*8.3,190),Life(1400+170*8,190),Life(1400+180*8,190),Life(1400+176*16,300),Life(1400+176*16 + 10,230),Life(1400+176*16 + 45,230),Life(1400+176*16 + 90,230)]
   object1 = [object( 0, 670 ),object( 1280, 670 ),object( 2560, 670 ),object( 3840, 670 ),object( 5120, 670 )]
   gun1 = Gun1( 1400, 600, taken=False )
   gun2 = Gun2( 1400+176*7,290, taken=False )
   gun3 = Gun3( 300, 600, taken=True )
   def damageUpdate():
       global life
       for i in range(len(bots)):
           if bots[i].Del:
               bots.pop(i)
               break
       for numbot in range( len( bots ) ):
           ng = len( player.gun )
           if ng >= 1:
               while True:
                   ng -= 1
                   i = len( player.gun[ng].potron )
                   if i >= 1:
                       while True:
                           i -= 1
                           if bots[numbot].rect.colliderect( player.gun[ng].potron[i].rect ) and not bots[numbot].death:
                               bots[numbot].life -= player.gun[ng].potron[i].damage
                               player.gun[ng].potron.pop( i )
                           if i == 0:
                               break
                   if ng == 0:
                       break
           i = len( bots[numbot].potron )
           if i >= 1:
               while True:
                   i -= 1
                   if player.rect.colliderect( bots[numbot].potron[i].rect ):
                       player.life -= bots[numbot].potron[i].damage
                       bots[numbot].potron.pop( i )
                   if i == 0:
                       break
           try:
               i = len( bots[numbot].potron )
               if i >= 1:
                   while True:
                       i -= 1
                       for g in range( len( platforms ) ):
                           if bots[numbot].potron[i].rect.colliderect( platforms[g].Rect ):
                               bots[numbot].potron.pop( i )
                       if i == 0:
                           break
           except:
               pass
       try:
           ng = len( player.gun )
           if ng >= 1:
               while True:
                   ng -= 1
                   i = len( player.gun[ng].potron )
                   if i >= 1:
                       while True:
                           i -= 1
                           for g in range( len( platforms ) ):
                               if player.gun[ng].potron[i].rect.colliderect( platforms[g].Rect ):
                                   player.gun[ng].potron.pop( i )
                           if i == 0:
                               break
                   if ng == 0:
                       break
       except:
           pass
   def gunupdate():
       gun1.update( player.state )
       gun2.update( player.state )
       gun3.update( player.state )

   def gundraw():
       try:
           for i in range( len( gun1.potron ) ):
            gun1.potron[i].fire()
            gun1.potron[i].draw( screen )
       except:
           pass
       try:
           for i in range( len( gun2.potron ) ):
             gun2.potron[i].fire()
             gun2.potron[i].draw( screen )
       except:
           pass
       try:
          for i in range( len( gun3.potron ) ):
            gun3.potron[i].fire()
            gun3.potron[i].draw( screen )
       except:
           pass
   while True:
        control()
        for i in range( len( fon ) ):
            fon[i].draw( screen )
        for i in range(len(object1)):
            object1[i].draw( screen )
        #terminal.draw(screen)
        lift.draw(screen,final)
        player.update( left, right, up, fire, num)
        gunupdate()
        gundraw()
        try:
            for i in range(len(platforms)):
                platforms[i].draw(screen)
        except:
            pass
        for i in range(len(bots)):
            bots[i].update()
            bots[i].draw(screen)
        for i in range(len(life1)):
            life1[i].draw(screen)
        player.draw( screen )
        for numbot in range(len(bots)):
            for i in range(len(bots[numbot].potron)):
                bots[numbot].potron[i].fire()
                bots[numbot].potron[i].draw(screen)
        if len( player.gun ) == 0:
            pass
        else:
            player.gun[player.numGun].draw( screen )
        try:
            if not gun1.taken:
                gun1.draw( screen )
        except:
            pass
        try:
            if not gun2.taken:
                gun2.draw(screen)
        except:
            pass
        try:
            if not gun3.taken:
                gun3.draw(screen)
        except:
            pass
        damageUpdate()
        # if player.rect.colliderect( terminal.rect ):
        #     if yes:
        #         terminal_history()
        for i in range( len( bots ) ):
            if bots[i].death:
                final = True
            else:
                final = False
                break
        if final:
            if player.rect.colliderect( lift.rect ):
                if yes:
                    Win = True
                    break
        if player.death:
           Win = False
           break
        pygame.display.update()
        clock.tick(90)
menu()
