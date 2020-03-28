import pygame
from pygame.transform import scale
import os
import sys
resource_folder = os.path.dirname( sys.argv[0] )
def load_image( fileName ):
    return pygame.image.load( os.path.join( resource_folder, fileName ) ).convert_alpha()

def load_anim():
  global anim
  anim = []
  for i in range(8):
      anim.append(scale( load_image( f"animation_player_run\\frame{i+1}.png" ), (60, 74) ))
  return anim
def load_anim_idle():
  anim2 = []
  for i in range(2):
      anim2.append(scale( load_image( f"animation_player_idle\\frame{i+1}.png" ), (60, 74) ))
  return anim2
def image():
    global Image
    Image = []
    Image.append(scale( load_image( "fon1.png" ), (1280, 720) ))
    Image.append(scale( load_image( "player.png" ), (60, 74) ))
    Image.append(scale( load_image( "пол.png" ), (1280, 50) ))
    Image.append(scale(load_image( "патрон.png" ), (40, 15) ))
    Image.append(load_image( "gun1.png" ))
    Image.append(load_image( "gun2.png" ) )
    Image.append(load_image( "gun3.png" ) )
    Image.append(scale( load_image( "bot1.png" ), (60, 60) ))
    Image.append( scale( load_image( "патрон2.png" ), (40, 15) ) )
    Image.append(scale( load_image( "bot2.png" ), (60, 60) ))
    Image.append(scale( load_image( "платформа.png" ), (176, 30) ))
    Image.append(scale(load_image('батарейка.png'),(30,35)))
    Image.append(scale(load_image('терминал2.png'), (47*2,60*2) ))
    Image.append( scale( load_image( "terminalfon.png" ), (1280, 720) ) )
    Image.append( scale( load_image( "start_first_episode_fon.png" ), (1280, 720) ) )
    Image.append( scale( load_image( "fon3.png" ), (1280, 670) ) )
    Image.append(scale( load_image( "fon.png" ), (1280, 720) ))
    Image.append( scale( load_image( "fon2.png" ), (1280, 670) ) )
    Image.append(scale(load_image('fon4.png'), (1280, 670)))
    Image.append( scale( load_image( 'fon5.png' ), (1280, 670) ) )
    Image.append(load_image( 'лифтclose.png' ))
    Image.append(load_image('лифтOpen.png'))
    Image.append( scale( load_image( "bot1_die.png" ), (80, 60) ) )
    Image.append( scale( load_image( "bot2_die.png" ), (60, 60) ) )
def return_image(index):
    global Image
    return Image[index]
pygame.font.init()
font = pygame.font.SysFont( 'Comic Sans MS', 60 )
screen = pygame.display.set_mode( (1280, 720) )
sky = scale( load_image( "fon.png" ), (1280, 720) )
screen.blit( sky, (0, 0) )
text = font.render( 'Загрузка...', False, (255, 0, 0) )
screen.blit( text, (460, 350) )
pygame.display.update()
image()
pygame.time.delay(500)