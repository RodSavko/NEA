def stateanimation(player,statesprites):
    if player.state in statesprites:
        frame = (player.statetime//6) % len(statesprites[player.state]) # loop through the animation frames
        image = statesprites[player.state][frame]
        return image

def attackanimation(player,attacksprites):
    if player.currentattack:
        if player.currentattack.name in attacksprites:
            scale = player.currentattack.total // len(attacksprites[player.currentattack.name]) # make it so the attack does a full animation loop
            frame = (player.attacktime//scale)  % len(attacksprites[player.currentattack.name])
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

jump_flip_frames = [
    (1281, 274, 71, 89),   # tuck begins
    (1354, 308, 68, 55),   # tumbling
    (1423, 316, 70, 46),
    (1494, 309, 60, 51),
    (1555, 305, 53, 58),
    (1611, 314, 66, 49),   # last tumble frame
    (1679, 286, 79, 77),   # opening out of the flip
    (1759, 254, 69, 109),  # coming down
    (1829, 249, 62, 114),  # descent / pre-landing
]
crouch_idle_frames = [
    (1145, 156, 88, 70),
    (1234, 155, 87, 71),
    (1322, 152, 88, 74),
]
forward_dash_frames = [
    (1,   511, 111, 98),   # lunge forward, headband streaming back
    (113, 515, 116, 94),
    (230, 515,  95, 94),
    (326, 514,  92, 95),
    (419, 506,  78, 103),  # straightening up

]

backward_dash_frames = [
    (655,  511, 100, 98),  # starts the backward hop
    (756,  506,  93, 103),
    (850,  507,  77, 102),
    (928,  505,  76, 104),
    (1005, 505,  78, 104),

]
medium_punch_frames = [
    (411, 1538, 81, 104),   # windup, fist pulled back
    (493, 1538, 80, 104),
    (574, 1541, 80, 101),
    (655, 1543, 125, 99),   # fist extended
    (781, 1541, 119, 101),  # extended, held
    (901, 1540, 90, 102),   # retracting
  #  (992, 1539, 85, 103),
 #   (1078, 1539, 94, 103),  # back to guard
]
heavy_punch_frames = [
    # row 15
    (1173, 1543,  98,  99),   # windup
    (1272, 1541, 100, 101),
    (1373, 1541, 102, 101),   # fist pulled back furthest
    (1476, 1540, 121, 102),   # extension
    (1598, 1540, 129, 102),   # full reach
    (1728, 1543, 100,  99),   # starting to retract
    # continues at the start of row 16
    (1,    1652, 100,  99),
    (102,  1652,  98,  99),   # retracting
    (201,  1651,  96, 100),
    (298,  1647,  80, 104),   # back to guard
]
medium_kick_frames = [
    # last 3 of row 17
    (1600, 1769,  64, 106),   # chamber / guard
    (1665, 1768,  82, 107),   # knee lifting
    (1748, 1774, 154, 101),   # leg fully extended
    # first 4 of row 18
    (1,    1887, 146, 103),   # extended, held
    (148,  1887, 121, 103),   # retracting
    (270,  1884,  86, 106),
    (357,  1885,  70, 105),   # back to guard
]

heavy_kick_frames = [
    (532,  1893,  76,  97),   # windup, turning
    (609,  1896,  77,  94),
    (687,  1890,  91, 100),
    (779,  1892,  80,  98),
    (860,  1890,  74, 100),   # leg starting to lift
    (935,  1878, 112, 112),   # high kick rising
    (1048, 1876, 115, 114),   # peak, leg overhead
    (1164, 1878, 118, 112),   # coming back down
    (1283, 1894, 117,  96),
    (1401, 1892,  76,  98),
    (1478, 1889,  70, 101),   # recovery
   # (1549, 1886,  78, 104),
    #(1628, 1886,  77, 104),   # back to guard
]
light_kick_frames = [
    (113, 1996,  76, 105),   # knee lifting
    (190, 2000,  68, 101),
    (259, 1999, 104, 102),   # leg extending
    (364, 1998, 102, 103),   # full extension
    (467, 2000,  65, 101),   # leg pulling back
    #(533, 1999,  64, 102),   # back to guard
]

crouching_lp_frames = [
    (928,  2162,  85, 70),   # crouch guard
    (1014, 2162, 113, 70),   # fist snaps out
    (1128, 2163, 110, 69),   # extended
    (1239, 2164,  85, 68),   # back to guard
]
crouching_hp_frames = [
    # end of row 20
    (1325, 2163, 93,  69),   # crouch, fist coming back
    (1419, 2156, 85,  76),   # starting to rise
    (1505, 2153, 81,  79),
    (1587, 2145, 81,  87),
    (1669, 2110, 76, 122),   # fully extended, fist overhead
    (1746, 2110, 76, 122),
    (1823, 2111, 76, 121),
    # start of row 21
    (1,    2243, 79,  97),   # coming down
    (81,   2243, 80,  97),
    (162,  2256, 85,  84),
    (248,  2269, 81,  71),   # settling back into crouch
    #(330,  2274, 84,  66),   # crouch guard
]
crouching_lk_frames = [
    (415, 2278, 137, 62),   # leg extended
    (553, 2279, 129, 61),   # held
    (683, 2277,  94, 63),   # pulling back
    (778, 2269,  87, 71),   # back to crouch guard
]
crouching_hk_frames = [
    # end of row 21
    (1630, 2264, 121, 76),   # new windup, turning
    (1752, 2268,  70, 72),
    # start of row 22
    (1,    2373, 135, 70),   # low leg out
    (137,  2374, 133, 69),
    (271,  2375, 121, 68),   # leg rising
    (393,  2380, 107, 63),
    (501,  2382,  83, 61),   # back to low crouch
]
sakotsu_wari_frames = [
    (201,  3457, 106, 106),   # wide stance, fist coming up
    (308,  3457, 102, 106),
    (411,  3456,  98, 107),   # fist raised overhead
    (510,  3455, 104, 108),   # turning into the chop
    (615,  3450, 110, 113),   # chop landing, headband flying
    (726,  3455, 106, 108),
    (833,  3464, 106,  99),   # recovering
    (940,  3465,  96,  98),
    (1037, 3461,  80, 102),   # back toward guard
]

kyuubi_kudaki_frames = [
    (969,  3723, 106, 97),   # fist pulled back
    (1076, 3723, 105, 97),   # arm starting to drive forward
    (1182, 3721,  96, 99),
    (1279, 3722,  90, 98),
    (1370, 3720, 122, 100),  # full thrust
    (1493, 3721, 108, 99),   # retracting
    (1602, 3721, 103, 99),
    (1706, 3717,  83, 103),  # back to guard
    (1790, 3717,  78, 103),
]

statesprites = {
    "idle" : idle_frames,
    "walking" : walk_frames,
    "hitstun" : hitstun_frames,
    "airborne" : jump_flip_frames,
    "crouch" : crouch_idle_frames
}

attacksprites = {
    "st lp" : light_punch_frames,
    "st mp" : medium_punch_frames,
    "st hp" : heavy_punch_frames,
    "st mk" : medium_kick_frames,
    "st hk" : heavy_kick_frames,
    "st lk" : light_kick_frames,
    "cr lp" : crouching_lp_frames,
    "cr hp" : crouching_hp_frames,
    "cr lk" : crouching_lk_frames,
    "cr hk" : crouching_hk_frames,
    "sakotsu wari" : sakotsu_wari_frames,
    "kyuubi kudaki" : kyuubi_kudaki_frames,
    "dash forwards" : forward_dash_frames,
    "dash backwards" : backward_dash_frames
}