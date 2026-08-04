#import pygame as pg


class Move:

    def __init__(self, name, command, active, lunge,priority, boost = 0, hitbox = 0):
        self.name = name
        self.command = command
        self.active = active
        self.lunge = lunge
        self.holding = False
        self.priority = priority
        self.boost = boost
        self.hitbox = hitbox

punch = Move("punch", "i", 6, 0,1,0,(100,100))
kick = Move("kick", "k", 10, 0,1,0,(200,100))
specialmove = Move("special", "26k", 30, 0,3,0,(300,300))
dashleft = Move("dashleft","44",1,-400,2)
dashright = Move("dashright","66",1,400,2)
jump = Move("jump", "8",1,0,1,30)


MoveList = (specialmove, punch, kick,dashleft,dashright,jump)





    