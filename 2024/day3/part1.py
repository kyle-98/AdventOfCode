import re
import operator as op

with open('input.txt', 'r') as infile:
    data = infile.read()

regex_match = r'mul\([0-9]{1,3},[0-9]{1,3}\)'

matches = re.findall(regex_match, data)
final_count = 0

for match in matches:
    final_count += eval(f'op.{match}')

print(final_count)