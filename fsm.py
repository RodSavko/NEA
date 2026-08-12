import pygame as pg
class State:
    def __init__(self,animation = 0):
        self.animation = animation

    def idle(self,player):
        player.size_y = 400

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
            player.fsm("active")
        else:
            return (player.x + 150, player.y, player.currentattack.hitbox[0], player.currentattack.hitbox[1])

    def recovery(self,player):
        if player.statetime > player.currentattack.recovery:
            player.fsm("idle")
            player.move = ""




