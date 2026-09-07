#import pygame as pg


class Move:

    def __init__(self, name, command, priority,startup,active,recovery,hitbox = 0, lungex = 0, lungey = 0, knockbackx=0,knockbacky=0,damage=0,stun=0):
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
        self.knockbackx = knockbackx
        self.knockbacky = knockbacky
        self.damage = damage
        self.stun = stun

punch = Move(
    "punch", "i",
    1,              # priority
    3, 2, 6,        # startup, active, recovery
    (100, 100),     # hitbox
    1, 0,            # lungex, lungey
    2, 1,            # knockbackx, knockbacky
    30,              # damage
    10               # stun
)

kick = Move(
    "kick", "k",
    1,
    6, 3, 10,
    (150, 100),
    2, 0,
    4, 2,
    50,
    15
)



forward_punch = Move(
    "forward punch", "6i",
    2,
    6, 3, 10,
    (130, 100),
    3, 0,
    40, 3,
    45,
    15
)



sweep = Move(
    "sweep", "2k",
    3,
    9, 4, 18,
    (180, 140),
    2, 0,
    5, 7,
    70,
    25
)

specialmove = Move(
    "special", "26k",
    4,
    12, 3, 18,
    (300, 300),
    2, 0,
    6, 5,
    90,
    30
)
dashbackwards = Move("dash backwards","44",3,0,6,0, 0, -20)
dashforwards = Move("dash forwards","66",3,0,6,0,0,20)
jump = Move("jump", "8",1,3,1,0,0,0,25)


MoveList = (specialmove,sweep,forward_punch,kick,punch,dashbackwards,dashforwards,jump)





    