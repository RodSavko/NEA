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

    def attack(self,player,move):

        hitbox = pg.Rect(self.x + 150, self.y, move.hitbox[0], move.hitbox[1])






