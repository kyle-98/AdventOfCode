
class Game():
    def __init__(self, gameid, sets):
        self.gameid = gameid
        self.sets = sets


def get_num_color(s):
    try:
        return int(s[0:2])
    except:
        return int(s[0])


# 12 red; 13 green; 14 blue
def main():
    with open('input.txt', 'r') as input_file:
        data = [line.rstrip() for line in input_file]
    
    g_list = []
    for d in data:
        temp = d.split(':')
        temp[0] = temp[0][5:]
        set_data_temp = temp[1].strip().split('; ')
        for i,sd in enumerate(set_data_temp):
            set_data_temp[i] = sd.split(', ')
        g_list.append(Game(int(temp[0]), set_data_temp))
    
    gg = []
    for g in g_list:
        gg_check = False
        for set in g.sets:
            gg_check = False
            bc, gc, rc = 0, 0, 0
            for s in set:
                if 'blue' in s:
                    bc += get_num_color(s)
                elif 'green' in s:
                    gc += get_num_color(s)
                else:
                    rc += get_num_color(s)
            if bc <= 14 and gc <= 13 and rc <= 12:
                gg_check = True
            if not gg_check:
                break
        if gg_check:
            gg.append(g.gameid)
        
    print(sum(gg))    



if __name__ == '__main__':
    main()