import sys
sys.path.append('ParticipantList')

import Participants #These Participants are imported from the Participants.py program.
import Rules #For Checking Rules and How to Play type "Rules.Rules()" below and Run the code.

Rules.Rules()  #<----Write like this without '#'


# Contains the If/Else statements for gamelogic and point distribution
def prisoners_dilemma(player1decision,player2decision):

    if player1decision == "cooperate" and player2decision == "cooperate":
        return (3,3)
    elif player1decision == "cooperate" and player2decision == "defect":
        return (0,5)
    elif player1decision == "defect" and player2decision == "cooperate":
        return (5,0)
    elif player1decision == "defect" and player2decision == "defect":
        return (1,1)

# For Repeating Scenarios and Summing up the Points.
def Repeater():   
    continuation = int(input("Enter number of time to run the code : "))
    point1,point2 = (0,0)
    player1decision = None
    player2decision = None

    while continuation > 0:
    # Enter Your Programs name imported from Participants.py
        player1decision = Participants.cooperator()   # Enter Player 1
        player2decision = Participants.randomer()     # Enter Player 2

        print(player1decision)
        print(player2decision,"\n")

        point1 += prisoners_dilemma(player1decision,player2decision)[0]
        point2 += prisoners_dilemma(player1decision,player2decision)[1]

        continuation = continuation-1

    print(f"Points Player1 = {point1}")
    print(f"Points Player2 = {point2}")

Repeater()

