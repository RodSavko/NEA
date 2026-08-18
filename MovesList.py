#import pygame as pg


class Move:

    def __init__(self, name, command, priority,startup,active,recovery,hitbox = 0, lungex = 0, lungey = 0):
        self.name = name
        self.command = command
        self.priority = priority
        self.startup =  startup
        self.active = active
        self.recovery = recovery
        self.hitbox = hitbox
        self.total = self.startup + self.active + self.recovery
        self.lungex = lungex
        self.lungey = lungey


punch = Move("punch", "i", 1, 1,12,1,(100,100),1)
kick = Move("kick", "k", 3, 10,18,3,(200,100),1)
specialmove = Move("special", "26k", 3, 12,3,18,(300,300),2)
dashbackwards = Move("dash backwards","44",2,0,6,0, 0, -20)
dashforwards = Move("dash forwards","66",2,0,6,0,0,20)
jump = Move("jump", "8",1,3,1,0,0,0,25)


MoveList = (specialmove, punch, kick,dashbackwards,dashforwards,jump)





    