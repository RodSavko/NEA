import pygame as pg
from classes import Character, GameLoop

pg.init()
screen = pg.display.set_mode((800,800))
fps = pg.time.Clock()


#process
#get player input - done
#inputs can get added every frame - done
#remove moves after a certain time or if they have been done - done
#every frame need to check if the queue if moves can be done - done

#check for moves:
#have the input string - may need to reformat it
#make movement first - left/right then do a jump
#make an attack then

#moves
#1 jump
#2 basic attack
#3 crouch
# - make thew screen more normal - mayube basic fsm logic
#4 normal attacks
#5 grab
#6 command normals
#7 specials
#8 supers

#need to make the arena
# camera focus
# coordinates
# camera move

#should change how dashes work - instead of instant teleport make a velocity boost


#the plan for inputs - when getting the inmputs store them in two separate lists per player, one for click and other is hold down, remove the release for clicks, and have the movement be held down, so when reading inpujts, check teh click list for moves and only then the hold list for the movemnt directions, make it modular so it can do command normals type shit,
# i fuckin did it

#so the input handling is done for now

movement = ("w","a","s","d")
queue = []
used = set()

black = (0,0,0)

camera_length = 800

frame = 1

player = Character()
player2 = Character(550,400)

game = GameLoop()

font = pg.font.Font(None, 36)

while True:

    keys, held = game.get_inputs()





    player.input_buffer.append([frame,keys[0]])
    player.movement(held[0])
    player.remove_input(frame)
    player.format_input()
    player.do_move(player.read_inputs())
    player.fall()


    player2.input_buffer.append([frame,keys[1]])
    player2.movement(held[1])
    player2.remove_input(frame)
    player2.format_input()
    player2.do_move(player2.read_inputs())
    player2.fall()




    #focus = (player.x + (player2.x + player2.size_x))//2
    #if focus < -1000:
     #   focus = -1000
   # if focus > 1000:
    #    focus = 1000
   # camera_x = focus - 400






    player.update_hitbox(0)
    player2.update_hitbox(0)





    screen.fill(black)
    pg.draw.rect(screen,(255,0,0),player.hitbox)
    pg.draw.rect(screen, (0, 0, 255), player2.hitbox)

    frame +=1

    fps_text = font.render(f"{fps}", True, (255, 255, 255))
    screen.blit(fps_text, (10, 10))

    pg.display.update()
    fps.tick(60)






