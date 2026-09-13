from sprites import idle_frames

class State:
    def __init__(self,animation = 0):
        self.animation = animation


    def idle(self,player):

        player.size_y = 400
        frame = ((player.statetime//6) % len(idle_frames))
        print(frame)
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
                    hitbox = (player.x + 150, player.y, player.currentattack.hitbox[0], player.currentattack.hitbox[1])
                else:
                    hitbox = (player.x - player.currentattack.hitbox[0],player.y,player.currentattack.hitbox[0], player.currentattack.hitbox[1])
                if player.statetime == 1:
                    player.hitbox = hitbox
                return hitbox

    def recovery(self,player):
        if player.statetime > player.currentattack.recovery:
            player.fsm("idle")
            player.currentattack = ""

    def hitstun(self,player):
        if player.stun == 0:
            player.fsm("idle")



