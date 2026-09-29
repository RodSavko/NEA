import pygame as pg

player1binds = {pg.K_a : "4",pg.K_d : "6",pg.K_w:"8",pg.K_i:"i",pg.K_k:"k",pg.K_j:"j", pg.K_l:"l",pg.K_s:"2"}
player2binds = {pg.K_f : "4",pg.K_h : "6",pg.K_t:"8",pg.K_c:"i",pg.K_v:"j",pg.K_b:"k",pg.K_n:"l",pg.K_h:"2"}


heldinputs = {pg.K_a,pg.K_d,pg.K_g,pg.K_j,pg.K_s,pg.K_h}


class GameLoop:
    def __init__(self, players):
        self.inputs = []
        self.players = players
        self.hitboxes = []

    def get_inputs(self):
        add = [[],[]]
        add2 = [[],[]]
        for press in pg.event.get():
            if press.type == pg.QUIT:
                pg.quit()
            elif press.type == pg.KEYDOWN:
                if press.key in player1binds:

                    add[0].append(player1binds[press.key])

                elif press.key in player2binds:
                    add[1].append(player2binds[press.key])

        hold = pg.key.get_pressed()

        for i in heldinputs:

            if hold[i] and i in player1binds:
                add2[0].append(player1binds[i])
            if hold[i] and i in player2binds:
                add2[1].append(player2binds[i])

        return add,add2

    def get_hitboxes(self):

        for player in self.players:
            if player.hitbox:
                self.hitboxes.append(player.hitbox)

