#import pygame as pg


class Move:

    def __init__(self, name, command, priority,startup,active,recovery,hitbox = 0, lungex = 0, lungey = 0, knockbackx=0,knockbacky=0,damage=0,stun=0, y_offset = 50, startstates = ("idle","crouch","walking"), jugglecost = 0):
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
        self.y_offset = y_offset
        self.startstates = startstates
        self.jugglecost = jugglecost

# =========================
# NORMAL ATTACKS
# priority = 1
# =========================

st_lp = Move(
    "Standing Light Punch",
    "i",
    1,
    4, 3, 8,
    (28, 20),
    0, 0,
    10, 0,
    20, 3,
    25,
    ("idle")
)

st_mp = Move(
    "Standing Medium Punch",
    "j",
    1,
    5, 4, 9,
    (38, 22),
    0, 0,
    15, 0,
    100, 11,
    25,
    ("idle")
)

st_lk = Move(
    "Standing Light Kick",
    "k",
    1,
    4, 3, 8,
    (32, 18),
    0, 0,
    10, 0,
    30, 3,
    55,
    ("idle")
)

st_mk = Move(
    "Standing Medium Kick",
    "l",
    1,
    6, 4, 12,
    (48, 20),
    0, 0,
    15, 0,
    80, 7,
    55,
    ("idle")
)


cr_lp = Move(
    "Crouching Light Punch",
    "i",
    1,
    4, 3, 7,
    (27, 17),
    0, 0,
    8, 0,
    20, 3,
    50,
    ("crouch")
)

cr_mp = Move(
    "Crouching Medium Punch",
    "j",
    1,
    5, 4, 7,
    (40, 22),
    0, 0,
    15, 0,
    90, 7,
    48,
    ("crouch")
)

cr_lk = Move(
    "Crouching Light Kick",
    "k",
    1,
    4, 3, 8,
    (30, 13),
    0, 0,
    8, 0,
    30, 3,
    70,
    ("crouch")
)

cr_mk = Move(
    "Crouching Medium Kick",
    "l",
    1,
    7, 5, 16,
    (48, 15),
    0, 0,
    18, 0,
    80, 7,
    70,
    ("crouch")
)


# =========================
# HEAVY ATTACKS
# priority = 2
# =========================

st_hp = Move(
    "Standing Heavy Punch",
    "j",
    2,
    11, 3, 18,
    (45, 28),
    0, 0,
    25, 0,
    130, 13,
    20,
    ("walking")
)

st_hk = Move(
    "Standing Heavy Kick",
    "l",
    2,
    8, 5, 18,
    (52, 22),
    0, 0,
    25, 0,
    140, 13,
    50,
    ("walking")
)

cr_hp = Move(
    "Crouching Heavy Punch",
    "j",
    2,
    5, 5, 19,
    (42, 30),
    0, 0,
    25, 0,
    130, 13,
    35,
    ("crouch",)
)

cr_hk = Move(
    "Crouching Heavy Kick",
    "l",
    2,
    8, 5, 20,
    (52, 15),
    0, 0,
    30, -5,
    100, 12,
    75,
    ("crouch",)
)


# =========================
# COMMAND NORMALS
# priority = 3
# Cannot start from idle
# =========================

sakotsu_wari = Move(
    "Sakotsu Wari",
    "i",
    3,
    7, 5, 25,
    (35, 30),
    0, 0,
    15, 0,
    100, 16,
    20,
    ("walking",)
)

kyuubi_kudaki = Move(
    "Kyuubi Kudaki",
    "k",
    3,
    12, 5, 25,
    (45, 25),
    0, 0,
    25, 0,
    120, 16,
    30,
    ("walking",)
)



dashbackwards = Move("dash backwards","44",3,0,15,0, 0, -15)
dashforwards = Move("dash forwards","66",3,0,15,0,0,15)
jump = Move("jump", "8",1,3,1,0,0,0,25)


MoveList = (st_lp,cr_lp,st_mp,st_hp,cr_hp,st_lk,cr_lk,st_mk,st_hk,cr_hk,sakotsu_wari,kyuubi_kudaki,dashbackwards,dashforwards,jump)





    