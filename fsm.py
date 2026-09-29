from sprites import idle_frames,walk_frames,hitstun_frames

class State:
    def __init__(self,animation = 0):
        self.animation = animation


    def idle(self,player):

        player.size_y = 400
        frame = ((player.statetime//5) % len(idle_frames))
        image = idle_frames[frame]
        player.sprite = image

    def crouch(self,player):
        player.size_y = 250
        if player.statetime == 1:
            player.y += 150

    def walking(self,player):

        if player.direction == "6":
            player.x += 5
        elif player.direction == "4":
            player.x -= 5
        else:
            print("error: no direction when moving")
        frame = ((player.statetime//6) % len(walk_frames))
        image = walk_frames[frame]
        player.sprite = image

    def startup(self,player):

        if player.statetime > player.currentattack.startup:
            player.fsm("active")

    def active(self,player):
        if player.statetime > player.currentattack.active:
            player.fsm("recovery")





        else:





            player.x += player.currentattack.lungex * player.currentattackfacing

            if player.currentattack.lungey: player.vy = player.currentattack.lungey
            if player.currentattack.hitbox:
                if player.statetime == 1:
                    player.currentattackhit = False


                if player.currentattackfacing == 1:
                    hitbox = (player.x + player.size_x, player.y + player.currentattack.y_offset, player.currentattack.hitbox[0] * 3, player.currentattack.hitbox[1] * 3)
                else:
                    hitbox = (player.x - player.currentattack.hitbox[0] * 3,player.y + player.currentattack.y_offset,player.currentattack.hitbox[0] * 3, player.currentattack.hitbox[1] * 3)
                if player.statetime == 1:
                    player.hitbox = hitbox
                return hitbox
        if player.currentattack.name == "dash forwards":
            frame = ((player.statetime//2) % len(walk_frames))
            image = walk_frames[frame]
            player.sprite = image

    def recovery(self,player):
        if player.statetime > player.currentattack.recovery:
            player.fsm("idle")
            player.currentattack = ""

    def hitstun(self,player):
        if player.stun == 0:
            player.fsm("idle")

        frame = ((player.statetime//6) % len(hitstun_frames))
        image = hitstun_frames[frame]
        player.sprite = image


