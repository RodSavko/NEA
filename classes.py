from MovesList import MoveList
import pygame as pg

pg.init()
limit = 15
movement = ("w", "a", "s", "d")

player1binds = {pg.K_a : "4",pg.K_d : "6",pg.K_w:"8",pg.K_i:"i",pg.K_k:"k"}
player2binds = {pg.K_g : "4",pg.K_j : "6",pg.K_y:"8",pg.K_b:"i",pg.K_n:"k"}
allowed = player1binds|player2binds

class GameLoop:
    def __init__(self, inputs = []):
        self.inputs = inputs

    def get_inputs(self):
        add = [[],[]]
        for press in pg.event.get():
            if press.type == pg.QUIT:
                pg.quit()
            elif press.type == pg.KEYDOWN:
                if press.key in player1binds:
                    add[0].append(player1binds[press.key])
                elif press.key in player2binds:
                    add[1].append(player2binds[press.key])
        return add




class Character:
    def __init__(self, x=100, y=100, left=pg.K_a, right=pg.K_d, size_x=150, size_y=300, vx=0, vy=0, attack="k"):
        self.input_buffer = []
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
        self.hitbox = pg.Rect(self.x, self.y, self.size_x, self.size_y)
        self.inputs = []
        self.vy = vy
        self.vx = vx
        self.attack = attack
        self.left = left
        self.right = right
        self.movelist = MoveList

    def add_input(self, frame):
        add = []
        hold = pg.key.get_pressed()
        if hold[self.left]:
            add.append("+")
        if hold[self.right]:
            add.append("=")
        if hold[pg.K_s]:
            add.append("-")

        for press in pg.event.get():
            if press.type == pg.QUIT:
                pg.quit()
            elif press.type == pg.KEYDOWN:
                if press.key == pg.K_w:
                    add.append("w")
                if press.key == pg.K_i:
                    add.append("i")
                if press.key == pg.K_j:
                    add.append("j")
                if press.key == pg.K_k:
                    add.append("k")
                if press.key == pg.K_l:
                    add.append("l")
                if press.key == self.left:
                    add.append("4")
                if press.key == self.right:
                    add.append("6")
                if press.key == pg.K_s:
                    add.append("2")
        if add:
            self.input_buffer.append([frame, add])

    def remove_input(self, frame):

        while self.input_buffer and self.input_buffer[0][0] <= frame - limit:
            self.input_buffer.pop(0)

    def format_input(self):
        queue = ""
        for i in range(len(self.input_buffer)):
            for j in range(len(self.input_buffer[i][1])):
                queue += self.input_buffer[i][1][j]

        self.inputs = queue

    def update_hitbox(self, camera_x):
        self.hitbox = pg.Rect(self.x - camera_x, self.y, self.size_x, self.size_y)

    def read_inputs(self):

        for move in self.movelist:
            string = ""
            i = 0
            for input in self.inputs:

                if input == move[i]:
                    i += 1

                    string += input

                    if string == move:
                        return move
                    if i == len(move):
                        break

    def do_move(self, move):

        if move == "6":
            self.x += 10

        elif move == "4":
            self.x -= 10
        elif move == "26k":
            print("special move")

    def fall(self):

        self.y -= self.vy
        self.vy -= 1
        if self.y >= 500:
            self.vy = 0
            self.y = 500

