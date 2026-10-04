def stateanimation(player,statesprites):
    if player.state in statesprites:
        frame = (player.statetime//5) % len(statesprites[player.state]) # loop through the animation frames
        image = statesprites[player.state][frame]
        return image

def attackanimation(player,attacksprites):
    if player.currentattack:
        if player.currentattack.name in attacksprites:
            scale = player.currentattack.total // len(attacksprites[player.currentattack.name]) # make it so the attack does a full animation loop
            frame = (player.attacktime//scale) % len(attacksprites[player.currentattack.name])
            image = attacksprites[player.currentattack.name][frame]
            return image



idle_frames = [
    (1,   12, 78, 101),
    (80,  11, 78, 102),
    (159,  7, 78, 106),
    (238,  5, 78, 108),
    (317,  4, 78, 109),
    (396,  4, 78, 109),
    (475,  4, 78, 109),
    (554,  5, 78, 108),
    (633,  6, 78, 107),
]

walk_frames = [
    (1026, 9,  93, 104),
    (1120, 9,  93, 104),
    (1214, 8,  74, 105),
    (1289, 9,  70, 104),
    (1360, 6,  67, 107),
    (1428, 2,  60, 111),
    (1489, 3,  63, 110),
    (1553, 3,  81, 110),
    (1635, 5,  91, 108),
    (1727, 5,  92, 108),
    (1820, 8,  92, 105),
]

hitstun_frames = [
    (741,  3345, 70,  104),
    (813,  3350, 70,   99),
    (884,  3356, 68,   93),
    (953,  3354, 79,   95),
    (1033, 3351, 104,  98),
]

light_punch_frames = [
    (1730, 1430, 78, 104),  # guard (last frame, row 14)
    (1,    1537, 121, 105), # fist snaps out to full extension
    (123,  1537, 114, 105), # held/slight retract
    (238,  1537, 93,  105), # retracting
    (332,  1537, 78,  105), # back to guard
]

statesprites = {
    "idle" : idle_frames,
    "walking" : walk_frames,
    "hitstun" : hitstun_frames
}

attacksprites = {
    "st_lp" : light_punch_frames,
    "dash forwards" : walk_frames,
    "dash backwards" : walk_frames
}