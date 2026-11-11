import sprites




class State:



    def idle(self,player):

        player.size_y = 350


    def crouch(self,player):
        player.size_y = 250
        if player.statetime == 1:
            player.y += 100

    def walking(self,player):
        player.size_y = 350
        if player.direction == "6":
            player.vx = 5
        elif player.direction == "4":
            player.vx = -5
        else:
            print("error: no direction when moving")


    def startup(self,player):

        if player.statetime > player.currentattack.startup:
            player.fsm("active")





    def active(self,player):

        if player.statetime > player.currentattack.active:
            player.fsm("recovery")

        else:


            player.vx = player.currentattack.lungex * player.currentattackfacing

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

            if player.statetime == player.currentattack.recovery:


                if player.currentattack.startstates == ("airborne"):
                    if player.y + player.size_y == 1050:
                        player.fsm("landing")
                    else:
                        player.fsm("airborne")
                else:
                    player.fsm("idle")

                player.currentattack = None
    def hitstun(self,player):
        if player.stun == 0:
            player.fsm("idle")


    def airborne(self,player):
        player.size_y = 200
        player.vx = player.jumpvx
        if player.size_y + player.y == 1050:
            player.fsm("landing")

    def landing(self,player):
        player.size_y = 350
        if player.statetime > 6:
            player.fsm("idle")
