import pygame as pg
from classes import Character, GameLoop


pg.init()
screen = pg.display.set_mode((1920,1080),pg.NOFRAME)

fps = pg.time.Clock()




#moves
#1 jump  - kinda floaty
#2 basic attack - not even half baked yet
#3 crouch - ehhh
# - make thew screen more normal - mayube basic fsm logic
# fsm - done fuck yeah
#4 normal attacks - i mean kinda need to get the actual frame data
#5 - collision checks
#6 command normals
#7 specials
#8 grab
#9 supers

#need to make the arena
# camera focus
# coordinates
# camera move

#need to fix jump - three directional jump = plus all teh fucking air logic

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

background = pg.image.load("suzakicastle.webp").convert()
background = pg.transform.scale(background,(1920,1080))



while True:

    keys, held = game.get_inputs()

    player.check_facing(player2)
    player.directionalise_inputs(keys[0])
    player.input_buffer.append([frame,player.keys])
    player.movement(held[0])
    player.remove_input(frame)
    player.format_input()
    player.read_inputs()
    player.start_move()
    player.fall()

    player2.check_facing(player)
    player2.input_buffer.append([frame,keys[1]])
    player2.movement(held[1])
    player2.remove_input(frame)
    player2.format_input()
    player2.read_inputs()
    player2.start_move()
    player2.fall()









    player.apply_state()
    player2.apply_state()


    player.update_hitbox(0)
    player2.update_hitbox(0)


    screen.blit(background,(0,0))
    pg.draw.rect(screen,(255,0,0),player.hitbox)
    pg.draw.rect(screen, (0, 0, 255), player2.hitbox)


    if player.attack:
        pg.draw.rect(screen,(255,100,255),player.attack)
    if player2.attack:
        pg.draw.rect(screen, (0,255,0), player2.attack)

    frame +=1


    fps_text = font.render(f"{fps} ,  game frame is {frame}, facing {player.facing, player2.facing}", True, (255, 255, 255))
    state = font.render(f"state is {player.state} for {player.statetime} frames / {(player.statetime/60):.2g} s, {keys[0],held[0]}", True, (255,255,255))
    screen.blit(fps_text, (10, 10))
    screen.blit(state,(10,50))


    pg.display.update()
    fps.tick(60)






