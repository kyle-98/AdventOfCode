import sys

def calculateCost(x):
    total = 0
    for i in positions:
        total += abs(x - i)
        
    return total
    

with open('input.txt') as file:
    positions = file.readline().split(',')

max = -1

for i in range(len(positions)):
    positions[i] = int(positions[i])
    if positions[i] > max:
        max = positions[i]

best = sys.maxsize      
for x in range(max):
    val = calculateCost(x)
    #print( val )
    if val < best:
        best = val
        bestX = x

print( "Best value: " + str(best))
#print( "Best location: " + str(bestX))