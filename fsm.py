class State:
    def __init__(self,animation = 0):
        self.animation = animation

    def idle(self,player):
        player.size_y = 400

    def crouch(self,player):
        player.size_y = 250

    def walking(self,player):

        if player.direction == "6":
            player.x += 5
        elif player.direction == "4":
            player.x -= 5
        else:
            print("error: no direction when moving")

    def startup(self,player):
        if player.statetime > player.currentattack.startup:
            player.prevstate = "startup"
            player.statetime = "1"
            player.state = "active"

    def active(self,player):
        if player.statetime > player.currentattack.active:
            player.prevstate = "active"
            player.statetime = "1"
            player.state = "recovery"
        else:
            pg.draw.rect(screen, (255, 0, 255), (player.x+150,player.y, player.move.hitbox[0], player.move.hitbox[1]))

    def recovery(self,player):
        if player.statetime > player.currentattack.recovery:
            player.prevstate = "recovery"
            player.statetime = "1"
            player.state = "idle"




