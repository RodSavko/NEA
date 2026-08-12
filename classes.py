from MovesList import MoveList
import pygame as pg
from fsm import State
from data import state_transitions

pg.init()
limit = 15

state = State()

player1binds = {pg.K_a : "4",pg.K_d : "6",pg.K_w:"8",pg.K_i:"i",pg.K_k:"k",pg.K_s:"2"}
player2binds = {pg.K_g : "4",pg.K_j : "6",pg.K_y:"8",pg.K_b:"i",pg.K_n:"k",pg.K_h:"2"}
allowed = player1binds|player2binds
moving_right = False
moving_left = False

heldinputs = {pg.K_a,pg.K_d,pg.K_g,pg.K_j,pg.K_s,pg.K_h}
hold = {"4","6"}
letgo = {"^","$"}


class GameLoop:
    def __init__(self, inputs = []):
        self.inputs = inputs

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








class Character:
    def __init__(self, x=100, y=100, size_x=150, size_y=400, vx=0, vy=0):
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
        self.facing = 1
        self.flagpos = -1
        self.flagpri = -1
        self.movequeue = []
        self.currentattack = ""
        self.statetime = 1
        self.prevstate = "idle"



    def remove_input(self, frame):



        while self.input_buffer and self.input_buffer[0][0] <= frame - limit: #wtf is this line

            self.flagpos -= len(self.input_buffer[0][1])
            self.input_buffer.pop(0)
        if self.flagpos < 0:
            self.flagpos = -1
            self.flagpri = -1

    def format_input(self):
        queue = ""

        for i in range(len(self.input_buffer)):
            for j in range(len(self.input_buffer[i][1])):
                char = self.input_buffer[i][1][j]


                if char:
                    queue += char


        self.inputs = queue


    def update_hitbox(self, camera_x):


        self.hitbox = pg.Rect(self.x - camera_x, self.y, self.size_x, self.size_y)

    def read_inputs(self):
        if self.inputs:



            for move in self.movelist:
                string = ""
                count = 0
                if move.priority > self.flagpri:
                    start = 0
                else:
                    start = self.flagpos + 1
                for i in range(start,len(self.inputs)):

                    if self.inputs[i] == move.command[count]:
                        count += 1

                        string += self.inputs[i]

                        if string == move.command:
                            self.flagpos = i
                            self.flagpri = move.priority
                            self.movequeue.append(move)
                            break
                        if count == len(move.command):
                            break

    def movement(self, held):

        if held:
            if held[0] == "6":

                self.direction = "6"
                self.fsm("walking")
            elif held[0] == "4":
                self.direction = "4"
                self.fsm("walking")


            if "2" in held:

                self.fsm("crouch")

        else:
            self.fsm("idle")
    def fsm(self,newstate):
        if newstate != self.state:
            if newstate in state_transitions[self.state]:
                self.statetime = 1
                self.prevstate = self.state
                self.state = newstate



    def start_move(self):

        if self.movequeue and not self.currentattack:
            print("2")
            self.currentattack = self.movequeue.pop(0)
            self.fsm("startup")



    def do_move(self):
       pass




    def fall(self):




        self.y -= self.vy
        self.vy -= 1
        if self.y >= 1050-self.size_y:
            self.vy = 0
            self.y = 1050-self.size_y



    def apply_state(self):



        if self.state == "idle":
            state.idle(self)
        elif self.state == "crouch":
            state.crouch(self)
        elif self.state == "walking":
            state.walking(self)

        if self.state == "startup":
            state.startup(self)
            print("4")
        if self.state == "active":
            print("3 ")
            return state.active(self)
        if self.state == "recovery":
            state.recovery(self)

        self.statetime += 1