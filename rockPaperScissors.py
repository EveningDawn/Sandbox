"""
Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input), compare them,
Print out a message of congratulations to the winner,
And ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""
def rockPaperScissors():
    player1 = input ("Enter contestant 1's name: ")
    player2 = input ("Enter contestant 2's name: ")

    print ("Go!")
    move1 = input (player1 + ": Enter one: Rock, paper, or scissors? \n").lower()
    for i in range (100):
        print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    move2 = input (player2 + ": Enter one: Rock, paper, or scissors? \n").lower()

    if move1 == "rock":
        if move2 == "rock":
            print ("Tie!")
        if move2 == "paper":
            print ("Paper beats rock: " + player2 + " wins!")
        if move2 == "scissors":
            print ("Rock beats scissors: " + player1 + " wins!")
    if move1 == "paper":
        if move2 == "rock":
            print ("Paper beats rock: " + player1 + " wins!")
        if move2 == "paper":
            print ("Tie!")
        if move2 == "scissors":
            print ("Scissors beats paper: " + player2 + " wins!")
    if move1 == "scissors":
        if move2 == "rock":
            print ("Rock beats scissors: " + player2 + " wins!")
        if move2 == "paper":
            print ("Scissors beats paper: " + player1 + " wins!")
        if move2 == "scissors":
            print ("Tie!")

    return i

goOn = "yes"
while goOn[0] == "y":
    rockPaperScissors()
    goOn = input ("Do you want to play agian? Yes/No \n").lower()