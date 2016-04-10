import sys, os, time
import patterns

def main():
    while True:
        print "Choose a mode: "
        print "1) Blinker"
        print "2) Toad"
        print "3) Beacon"
        print "4) Pulsar"
        print "5) Glider"
        print "6) Lightweight spaceship"
        print "7) Glider gun"
        print "8) Enter custom field..."
        print "0) Exit"
        print "---------------------------"

        mode = int(raw_input())
        if mode == 1:
            blinker()
        elif mode == 2:
            toad()
        elif mode == 3:
            beacon()
        elif mode == 4:
            pulsar()
        elif mode == 5:
            glider()
        elif mode == 6:
            lwss()
        elif mode == 7:
            glider_gun()
        elif mode == 8:
            custom_field()
        elif mode == 0:
            sys.exit()
        else:
            print "No valid option. Please enter one of the above modes.\n"


def play(hor, vert, field, iterations, speed):
    while(iterations > 0):
        new_field = [[0 for x in range(hor)] for x in range(vert)]
        #Go through every cell
        for i in range(vert):
            for j in range(hor):
                if (field[i][j] == 1):
                    new_field = checkLivingCell(field, new_field, hor, vert, i, j)
                elif (field[i][j] == 0):
                    new_field = checkDeadCell(field, new_field, hor, vert, i, j)

        field = new_field
        iterations -= 1
        time.sleep(speed)
        os.system("clear") #Clear console window
        print_array(field, hor, vert)


def checkLivingCell(field, new_field, hor, vert, i, j):
    livNeighbors = countNeighbors(field, new_field, hor, vert, i, j)
    #Check for two or three living neighbor cells to keep cell
    if (livNeighbors == 2 or livNeighbors == 3):
        new_field[i][j] = 1

    return new_field


def checkDeadCell(field, new_field, hor, vert, i, j):
    livNeighbors = countNeighbors(field, new_field, hor, vert, i, j)
    #Check for three living neighbors to reincarnate cell
    if (livNeighbors == 3):
        new_field[i][j] = 1

    return new_field


def countNeighbors(field, new_field, hor, vert, i, j):
    livNeighbors = 0
    for k in range(-1, 2):
        for l in range(-1,2):
            if (((i+k) > -1) and (j+l) > -1 and (i+k) < vert and (j+l) < hor): #Neighbor cell in the boundaries of the array?
                if (field[(i+k)][(j+l)] == 1 and not (k == 0 and l == 0)): #Neighbor cell living and not checked cell?
                    livNeighbors += 1
    return livNeighbors


def print_array(array, hor, vert):
    for i in range(vert):
        for j in range(hor):
            if j == hor - 1:
                if array[i][j] != 0:
                    print u"\u2587" #Print a block character
                else:
                    print " "
            else:
                if array[i][j] != 0:
                    print u"\u2587",
                else:
                    print " ",


def blinker():
    field = blinker
    new_field = [[0 for x in range(3)] for x in range(3)]
    play(3, 3, patterns.blinker, 10, 0.5)


def toad():
    field = toad
    new_field = [[0 for x in range(4)] for x in range(4)]
    play(4, 4, patterns.toad, 10, 0.5)


def beacon():
    new_field = [[0 for x in range(4)] for x in range(4)]
    play(4, 4, patterns.beacon, 10, 0.5)


def pulsar():
        new_field = [[0 for x in range(15)] for x in range(15)]
        play(15, 15, patterns.pulsar, 12, 0.3)


def glider():
    new_field = [[0 for x in range(12)] for x in range(12)]
    play(12, 12, patterns.glider, 36, 0.2)


def lwss():
    new_field = [[0 for x in range(20)] for x in range(6)]
    play(20, 6, patterns.lwss, 36, 0.2)


def glider_gun():
    new_field = [[0 for x in range(50)] for x in range(30)]
    play(50, 30, patterns.gun, 200, 0.01)


def custom_field():
    vert = int(raw_input("Height: "))
    hor = int(raw_input("Width: "))
    print "Enter your field (1 is living, 0 is dead; separated by spaces)"

    field = [[0 for x in range(hor)] for x in range(vert)]
    new_field = [[0 for x in range(hor)] for x in range(vert)]

    for i in range(vert):
        field_input = raw_input()
        for j in range(hor):
            field_input_arr = field_input.split(" ", hor)
            field[i][j] = int(field_input_arr[j])

    iteration = int(raw_input("Iterations: "))
    speed = float(raw_input("Speed in seconds (for example 0.5): "))
    print_array(field, hor, vert)
    play(hor, vert, field, iteration, speed)


if __name__ == '__main__':
    main()
