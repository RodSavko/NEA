#import pygame as pg


class Move:

    def __init__(self, name, command, priority,startup,active,recovery,hitbox = 0):
        self.name = name
        self.command = command
        self.priority = priority
        self.startup =  startup
        self.active = active
        self.recovery = recovery
        self.hitbox = hitbox
        self.total = self.startup + self.active + self.recovery


punch = Move("punch", "i", 1, 6,1,0,(100,100))
kick = Move("kick", "k", 3, 10,1,0,(200,100))
specialmove = Move("special", "26k", 3, 6,3,0,(300,300))
dashleft = Move("dashleft","44",2,0,1,0)
dashright = Move("dashright","66",2,0,1,0)
jump = Move("jump", "8",1,0,1,0)


MoveList = (specialmove, punch, kick,dashleft,dashright,jump)





    