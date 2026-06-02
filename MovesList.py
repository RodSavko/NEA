import pygame as pg
from pygame.examples.stars import move_stars


class Move:

    def __init__(self, name, command, active, lunge):
        self.name = name
        self.command = command
        self.active = active
        self.lunge = lunge
        self.holding = False

punch = Move("punch", "i", 6, 0)
kick = Move("kick", "k", 10, 0)
specialmove = Move("special", "26k", 30, 0)
dashleft = Move("dashleft","44",1,-40)
dashright = Move("dashright","66",1,40)
left = Move("left","4",1, -5)
right = Move("right","6",1,5)

MoveList = [specialmove, punch, kick,dashleft,dashright, left,right]



