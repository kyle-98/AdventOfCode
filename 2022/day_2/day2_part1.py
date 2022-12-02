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

def is_loss(opponent, player):
    if opponent == 'A' and player == 'Z':
        return True
    elif opponent == 'B' and player == 'X':
        return True
    elif opponent == 'C' and player == 'Y':
        return True
    else:
        return False

with open("input.txt", "r") as infile:
    for line in infile:
        outcome = ''
        round_points = 0
        opponent_c, player_c = line.strip().split(" ")

        #Draw
        if choices_dict[opponent_c] == choices_dict[player_c]:
            round_points += conditions_dict['D']
            round_points += conditions_dict[player_c]
        
        #Loss
        elif is_loss(opponent_c, player_c):
            round_points += conditions_dict['L']
            round_points += conditions_dict[player_c]

        #Win
        else:
            round_points += conditions_dict['W']
            round_points += conditions_dict[player_c]


        scores.append(round_points)
        
print(sum(scores))     