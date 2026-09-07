from MovesList import MoveList
import pygame as pg
from fsm import State
from data import state_transitions


pg.init()
limit = 15

state = State()








class Character:
    def __init__(self, x=100, y=100, size_x=150, size_y=400, vx=0, vy=0):
        self.input_buffer = []
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
        self.hurtbox = pg.Rect(self.x, self.y, self.size_x, self.size_y)
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
        self.attack = ""
        self.facing = 1
        self.keys = 0
        self.currentattackfacing = 1
        self.currentattackhit = False
        self.hitbox = 0
        self.health = 1000
        self.attackhashit = False
        self.stun = 0


    def remove_input(self, frame):



        while self.input_buffer and self.input_buffer[0][0] <= frame - limit: #wtf is this line

            self.flagpos -= len(self.input_buffer[0][1])
            self.input_buffer.pop(0)
        if self.flagpos < 0:
            self.flagpos = -1
            self.flagpri = -1

    def directionalise_inputs(self,keys):
        for i in range(len(keys)):
            if keys[i] == "4":
                if self.facing == -1:
                    keys[i] = "6"
                    continue
            elif keys[i] == "6":
                if self.facing == -1:
                    keys[i] = "4"
        self.keys = keys

    def format_input(self):
        queue = ""

        for i in range(len(self.input_buffer)):
            for j in range(len(self.input_buffer[i][1])):
                char = self.input_buffer[i][1][j]


                if char:
                    queue += char


        self.inputs = queue

    def update_hurtbox(self, camera_x):
        self.hurtbox = pg.Rect(self.x - camera_x, self.y, self.size_x, self.size_y)
        if self.state != "active":
            self.hitbox = 0




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
                            self.movequeue.append([move, self.facing])
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
            if not self.currentattack and not self.stun:
                self.fsm("idle")

    def fsm(self,newstate):
        if newstate != self.state:
            if newstate in state_transitions[self.state]:
                self.statetime = 0
                self.prevstate = self.state
                self.state = newstate

    def start_move(self):

        if self.movequeue and not self.currentattack:

            self.currentattack, self.currentattackfacing = self.movequeue.pop(0)

            self.fsm("startup")

    def check_facing(self,enemy):
        if self.x > enemy.x:
            self.facing = -1 #facing left
        elif self.x < enemy.x:
            self.facing = 1 #facing right

    def fall(self):




        self.y -= self.vy
        self.vy -= 1
        if self.y >= 1050-self.size_y:
            self.vy = 0
            self.y = 1050-self.size_y

    def apply_state(self):
        if self.stun:
            self.stun -= 1


        if self.state == "idle":
            state.idle(self)
        elif self.state == "crouch":
            state.crouch(self)
        elif self.state == "walking":
            state.walking(self)

        if self.state == "startup":
            state.startup(self)

        if self.state == "active":
            self.attack =  state.active(self)


        if self.state == "recovery":
            state.recovery(self)
        if self.state == "hitstun":
            state.hitstun(self)



        self.statetime += 1

    def checkifgothit(self,enemy):
        if enemy.hitbox and not enemy.currentattackhit:
            if self.hurtbox.colliderect(enemy.hitbox):
                self.stun = enemy.currentattack.stun
                self.health -= enemy.currentattack.damage
                self.x += enemy.currentattack.knockbackx * self.facing * -1
                self.y -= enemy.currentattack.knockbacky * 10
                enemy.currentattackhit = True
                self.fsm("hitstun")

