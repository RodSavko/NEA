from MovesList import MoveList
import pygame as pg

pg.init()
limit = 15


player1binds = {pg.K_a : "4",pg.K_d : "6",pg.K_w:"8",pg.K_i:"i",pg.K_k:"k"}
player2binds = {pg.K_g : "4",pg.K_j : "6",pg.K_y:"8",pg.K_b:"i",pg.K_n:"k"}
allowed = player1binds|player2binds
moving_right = False
moving_left = False

movement = {"4","6","^","$"}
hold = {"4","6"}
letgo = {"^","$"}


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

            elif press.type == pg.KEYUP:
                if press.key == pg.K_a:

                    add[0].append("$")
                elif press.key == pg.K_d:
                    add[0].append("^")

                if press.key == pg.K_g:
                    add[1].append("$")
                elif press.key == pg.K_j:
                    add[1].append("^")

        return add




class Character:
    def __init__(self, x=100, y=100, size_x=150, size_y=300, vx=0, vy=0):
        self.input_buffer = []
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
        self.hitbox = pg.Rect(self.x, self.y, self.size_x, self.size_y)
        self.inputs = []
        self.vy = vy
        self.vx = vx
        self.movelist = MoveList
        self.moving_right = False
        self.moving_left = False
        self.state = "idle"
        self.direction = ""



    def remove_input(self, frame):

        while self.input_buffer and self.input_buffer[0][0] <= frame - limit:
            self.input_buffer.pop(0)

    def format_input(self):
        queue = ""
        for i in range(len(self.input_buffer)):
            for j in range(len(self.input_buffer[i][1])):
                char = self.input_buffer[i][1][j]
                if char in movement:
                    if self.state == "moving":
                        if char in letgo:
                            queue += char
                    else:
                        queue += char


                else:
                    queue += char

        self.inputs = queue


    def update_hitbox(self, camera_x):
        self.hitbox = pg.Rect(self.x - camera_x, self.y, self.size_x, self.size_y)

    def read_inputs(self):
        if self.inputs:
            if self.inputs[0] == "4":
                self.direction = "left"
                self.state = "moving"
                return
            elif self.inputs[0] == "6":
                self.direction = "right"
                self.state = "moving"
                return
            elif self.inputs[0] in letgo:
                self.direction = ""
                self.state = "idle"
                return


            for move in self.movelist:
                string = ""
                i = 0

                for input in self.inputs:

                    if input == move.command[i]:
                        i += 1

                        string += input

                        if string == move.command:
                            return move
                        if i == len(move.command):
                            break

    def do_move(self, move):

        if move:
            self.x += move.lunge





    def fall(self):




        self.y -= self.vy
        self.vy -= 1
        if self.y >= 500:
            self.vy = 0
            self.y = 500

        if self.direction == "left":
            self.x -= 5
        elif self.direction == "right":
            self.x += 5
