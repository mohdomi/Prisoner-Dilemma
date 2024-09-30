def Rules():
    print("\nThis is a Famous Game in Game Theory called the Prisoner's Dilemma.")
    print("The Rules for the game are simple.")
    print('Two players are going to compete against eachother.')
    print("There are two choices for each of the players :-")
    print("either 'COOPERATE' or 'DEFECT' each other.")
    print("if both the player choose to cooperate then both of them get 3,3 points each.")
    print("if either of them Defect then both get 1,1 points each.")
    print("if one player defects and the other player cooperates the player that defected will get 5 points")
    print("and the one who cooperated will get 0 points")
    print("The Table below Highlights the Game rules.\n")
    print("Player1   | Player2  ")
    print("Cooperate | Cooperate  =  '3,3' ")
    print("Cooperate | Defect     =  '0,5' ")
    print("Defect    | Cooperate  =  '5,0' ")
    print("Defect    | Defect     =  '1,1' ")

    print("\n For playing the game.Save your program in file and import the file in Participant.py file and save it.")
    print("\nThen open the Logic.py file and write the name of both the participants programs in the format :- ")
    print("Player1Decision = Participant.'your Program name()'")
    print("Similarly for Player2 write Participant.'Name of Other program()'")

    print("Run the Game,Write number of Rounds for the program to run.")
    print("then check your points")

    print("Enjoy!!!\n\n")



if __name__ ==  "__main__":
    Rules()