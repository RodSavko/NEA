import pygame as pg

from classes import Character


pg.init()
screen = pg.display.set_mode((800,800))
fps = pg.time.Clock()


#process
#get player input - done
#inputs can get added every frame - done
#remove moves after a certain time or if they have been done - done
#every frame need to check if the queue if moves can be done -

#check for moves:
#have the input string - may need to reformat it
#make movement first - left/right then do a jump
#make an attack then

#moves
#1 jump
#2 basic attack
#3 crouch
#4 normal attacks
#5 grab
#6 command normals
#7 specials
#8 supers

#need to make the arena
# camera focus
# coordinates
# camera move


movement = ("w","a","s","d")
queue = []
used = set()

black = (0,0,0)

camera_length = 800

frame = 1

player = Character()
player2 = Character(550,400,pg.K_u,pg.K_o)

while True:

    player.add_input(frame)
    player.remove_input(frame)
    player.format_input()
    player.do_move(player.read_inputs())
    player.fall()

    player2.add_input(frame)
    player2.remove_input(frame)
    player2.format_input()
    player2.do_move(player2.read_inputs())
    player2.fall()



    focus = (player.x + (player2.x + player2.size_x))//2
    if focus < -1000:
        focus = -1000
    if focus > 1000:
        focus = 1000
    camera_x = focus - 400






    player.update_hitbox(camera_x)
    player2.update_hitbox(camera_x)





    screen.fill(black)
    pg.draw.rect(screen,(255,0,0),player.hitbox)
    pg.draw.rect(screen, (0, 0, 255), player2.hitbox)

    frame +=1
    pg.display.update()
    fps.tick(60)






