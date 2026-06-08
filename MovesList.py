import pygame as pg


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
left = Move("left","4",1, 5)
right = Move("right","6",1,5)
leftstop = Move("leftstop","$",1,0)
rightstop = Move("rightstop","^",1,0)
MoveList = [specialmove, punch, kick,dashleft,dashright, left,right]



