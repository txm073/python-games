nums = ["0","1","2","3","4","5","6","7","8","9"]
places = [" "," "," "," "," "," "," "," "," "," "]

def print_board(places):
    print("")
    print('     |     |')
    print('  ' + places[1] + '  |  ' + places[2] + '  |  ' + places[3])
    print('     |     |')
    print('-----------------')
    print('     |     |')
    print('  ' + places[4] + '  |  ' + places[5] + '  |  ' + places[6])
    print('     |     |')
    print('-----------------')
    print('     |     |')
    print('  ' + places[7] + '  |  ' + places[8] + '  |  ' + places[9])
    print('     |     |')

def check(places,player):
    for p in range(3):
        if places[p] == player and places[p+3] == player and places[p+6] == player:
            return True
    for p in (1,4,7):
        if places[p] == player and places[p+1] == player and places[p+2] == player:
            return True
    if places[1] == player and places[5] == player and places[9] == player:
        return True
    if places[3] == player and places[5] == player and places[7] == player:
        return True

def O_turn(places):
    valid_pos = False
    while valid_pos == False:
        O_entry = input("\nNoughts - enter a position: ")
        for index, value in enumerate(nums):
            if O_entry == value:
                if places[index] == " ":
                    places[index] = "O" 
                    print_board(places)
                    valid_pos = True
                else:
                    print("That position is taken!")
    if check(places, "O") == True:
        print("Game Over!")
        print("Noughts Win!")
        return True
    return False
    
def X_turn(places):
    valid_pos = False
    while valid_pos == False:
        X_entry = input("\nCrosses - enter a position: ")
        for index, value in enumerate(nums):
            if X_entry == value:
                if places[index] == " ":
                    places[index] = "X" 
                    print_board(places)
                    valid_pos = True
                else:
                    print("That position is taken!")
    if check(places, "X") == True:
        print("Game Over!")
        print("Crosses Win!")
        return True
    return False

turns = 9
winner = False
while turns != 0:
    if O_turn(places) == True:
        winner = True
        break
    turns -= 1
    if X_turn(places) == True:
        winner = True
        break
    turns -= 1

if winner == False:
    print("Game Over!")
    print("It's a tie!")

