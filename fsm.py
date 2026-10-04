import sprites




class State:
    def __init__(self,animation = 0):
        self.animation = animation





    def idle(self,player):

        player.size_y = 350


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

    def recovery(self,player):
        if player.statetime > player.currentattack.recovery:
            player.fsm("idle")
            player.currentattack = ""

        elif player.currentattack.name == "Standing Light Punch":
            frame = ((player.attacktime) % len(light_punch_frames))
            image = light_punch_frames[frame]
            player.sprite = image

    def hitstun(self,player):
        if player.stun == 0:
            player.fsm("idle")




