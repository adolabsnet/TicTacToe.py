def print_board():
    for i in range(0,3):
        for j in range(0,3):
            print map[2-i][j],
            if j != 2:
                print "|",
        print ""


def check_done():
    for i in range(0,3):
        if map[i][0] == map[i][1] == map[i][2] != " " \
        or map[0][i] == map[1][i] == map[2][i] != " ":
            print "  "
            print " "
            print " "
            print " "
            print " "
            print " "
            print_board()
            print " "
            print turn2, "won!!!"
            return True

    if map[0][0] == map[1][1] == map[2][2] != " " \
    or map[0][2] == map[1][1] == map[2][0] != " ":
            print " "
            print " "
            print " "
            print " "
            print " "
            print " "
            print_board()
            print " "
            print turn2, "won!!!"
            return True

    if " " not in map[0] and " " not in map[1] and " " not in map[2]:
        print "Draw"
        return True


    return False


print "Hi, welcome to Nathan's TicTacToe"
player_1 = raw_input("Player 1 (X) : ")
print " "
player_2 = raw_input("Player 2 (O) : ")
print " "
print "Instructions: Please select position by typing in a number between 1 and 9, see below for which number that is which position..."

turn = "X"
turn2= player_1
map = [[" "," "," "],
       [" "," "," "],
       [" "," "," "]]


done = False






while done != True:
    print " "
    print " "
    print " "
    print " "
    print turn2, "'s turn"
    print " "
    print " "
    print_board()
    print " "
    print " "
    print "Select position:"
    print "7|8|9"
    print "4|5|6"
    print "1|2|3"


    moved = False
    while moved != True:

        try:
            pos = input("Select: ")
            if pos <=9 and pos >=1:
                Y = pos/3
                X = pos%3
                if X != 0:
                    X -=1
                    print " "
                    print "ERROR, try again"
                    print " "
                else:
                    print " "
                    print "ERROR, try again"
                    print " "
                    X = 2
                    Y -=1

                if map[Y][X] == " ":
                    map[Y][X] = turn
                    moved = True
                    done = check_done()

                    if done == False:
                        if turn == "X":
                            turn = "0"
                        if turn2 == player_1:
                            turn2 = player_2
                        else:
                            turn = "X"
                            turn2 = player_1
        except:
            print "You need to add a numeric value"
