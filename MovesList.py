class Move:

    def __init__(self,name,command,active,lunge):
        self.name = name
        self.command = command
        self.active = active
        self.lunge = lunge

punch = Move("punch","i", 6,0)
kick = Move("kick","k",10,0)
specialmove = ("special","26k",30,0)




specialmove = "26k"
punch = "i"
kick = "k"
move_left = "4"
move_right = "6"

MoveList = [specialmove,punch,kick,move_left,move_right]
print(MoveList)

if specialmove == list(specialmove):
    print("yes")


    