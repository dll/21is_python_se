import sys

from Horse import Horse

class HorseGroup:

    count=3

    horses=[]

    def __init__(self,horses):
        print("HorseGroup Total horses " + str(sys.maxsize))
        for i in range(0, len(horses)):
            self.horses.append(horses[i])
        print("HorseGroup initial size " + str(len(horses)));