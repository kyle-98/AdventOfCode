"""
    NOTES:

- X register is the middle of a 3 pixel sprite
- one pixel is drawn every cycle
- if one of the 3 pixels from the sprite appear as a pixel being drawn in that cycle change . to #
"""
with open('input.txt', 'r') as infile:
    operations = [line.rstrip() for line in infile]

cycle_counter = 0
pixel_c = 0
x_value = 1
signal_list = []
sprite_pos = [0, 1, 2]
selected_row = 0
# screen = [['.'*40] for _ in range(6)]
screen = [[] for _ in range(6)]
for op in operations:
    flag = 0
    if op.startswith('n'):
        flag = 1
    else:
        flag = 2
    for i in range(flag):
        cycle_counter += 1
        
        if cycle_counter % 40 == 1 and cycle_counter != 1:
            selected_row += 1
            pixel_c = 0
        
        if pixel_c in sprite_pos:
            screen[selected_row].append('#')
        else:
            screen[selected_row].append('.')
        pixel_c += 1

        # print(f'Cycle {cycle_counter}->',f'PIXEL: {pixel_c}' , f'X: {x_value}', sprite_pos)
        # print(''.join(screen[selected_row]))

    if flag == 2:
        x_value += int(op.split()[1])
        sprite_pos = [x_value - 1, x_value, x_value + 1]

print()
[print(''.join(s)) for s in screen]