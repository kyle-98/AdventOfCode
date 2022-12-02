#   OPPONENT MAP VARIABLES
#A = Rock
#B = Paper
#C = Scissors

#   PLAYER MAP VARIABLES
#X = Rock
#Y = Paper
#Z = Scissors

#   RULE POINTS
#1 for rock
#2 for paper
#3 for scissors

#   OUTCOME POINTS
#0 for loss
#3 for draw
#6 for win

scores = []
conditions_dict = {
    'X': 1,
    'Y': 2,
    'Z': 3,
    'L': 0,
    'D': 3,
    'W': 6
}
choices_dict = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
}


def choosing(opponent, round_outcome):
    #Player Choices for Loss
    if round_outcome == 'X':
        if opponent == 'A':
            return 'Z'
        elif opponent == 'B':
            return 'X'
        else: 
            return 'Y'
        

    #Player choices for Draw
    elif round_outcome == 'Y':
        if opponent == 'A':
            return 'X'
        elif opponent == 'B':
            return 'Y'
        else:
            return 'Z'
    
    #Player choices for Win
    else:
        if opponent == 'A':
            return 'Y'
        elif opponent == 'B':
            return 'Z'
        else:
            return 'X'



with open("input.txt", "r") as infile:
    for line in infile:
        outcome = ''
        round_points = 0
        opponent_c, round_end_choice = line.strip().split(" ")
        player_choice = choosing(opponent_c, round_end_choice)

        #Loss
        if round_end_choice == 'X':
            round_points += conditions_dict['L']
            round_points += conditions_dict[player_choice]
        
        #Draw
        elif round_end_choice == 'Y':
            round_points += conditions_dict['D']
            round_points += conditions_dict[player_choice]
        
        #Win
        else:
            round_points += conditions_dict['W']
            round_points += conditions_dict[player_choice]
            
        scores.append(round_points)
        
print(sum(scores))     