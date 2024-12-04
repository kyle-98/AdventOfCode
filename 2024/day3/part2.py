import re
import operator as op
from operator import itemgetter as ig

with open('input.txt', 'r') as infile:
    data = infile.read()

# 57150294 too low
# 82733683
# 91627985 too high
# 28227497 too low

regex_match_mul = r'mul\([0-9]{1,3},[0-9]{1,3}\)'
regex_match_do = r'do\(\)'
regex_match_dont = r'don\'t\(\)'

do_instructs = [(m.start(), 'DO') for m in re.finditer(regex_match_do, data)]
dont_instructs = [(m.start(), 'DONT') for m in re.finditer(regex_match_dont, data)]
mul_instructs = [(m.start(), m.group()) for m in re.finditer(regex_match_mul, data)]

do_mul = True
full_exec_instructs = do_instructs + dont_instructs
full_exec_instructs = sorted(full_exec_instructs, key=ig(0))

def nearest_index(l: list, val: int) -> int:
    valids = [i for i in l if i[0] <= val]
    return max(valids, key=lambda x: x[0], default=None) if valids else None

final_count = 0
do_exec = True

for mi in mul_instructs:
    mul_index = mi[0]
    nearest = nearest_index(full_exec_instructs, mul_index)
    if nearest == None:
        # print('EXEC', mi)
        final_count += eval(f'op.{mi[1]}')
    elif nearest[1] == 'DO':
        # print('EXEC', mi)
        final_count += eval(f'op.{mi[1]}')
    # else:
    #     print('NON-EXEC', mi)
    


   

    

print(final_count)