
class MapElement():
    def __init__(self, dest, src, rang):
        self.dest = dest
        self.src = src
        self.rang = rang

def convert_map_val(value_range, sts):
    found = False
    for s in sts:
        target_range = range(s.src, s.src + s.rang)
        print(target_range)


    # for s in sts:
    #     if val < s.src:
    #         pass
    #     elif val >= s.src and val <= (s.src + s.rang) - 1:
    #         found = True
    #         return abs(val - s.src) + s.dest
    #     else:
    #         pass
    # if not found:
    #     return val

def main():
    with open('test_input.txt', 'r') as input_file:
        data = [i.rstrip() for i in input_file]

    seeds = [int(i) for i in data[0][7:].split(' ')]
    sts, stf, ftw, wtl, ltt, tth, htl = [], [], [], [], [], [], []
    cc = None
    for d in data:
        if d == '':
            cc = None
        
        if cc != None:
            t = [int(i) for i in d.split(' ')]
            if cc == 'sts':
                sts.append(MapElement(t[0], t[1], t[2]))
            elif cc == 'stf':
                stf.append(MapElement(t[0], t[1], t[2]))
            elif cc == 'ftw':
                ftw.append(MapElement(t[0], t[1], t[2]))
            elif cc == 'wtl':
                wtl.append(MapElement(t[0], t[1], t[2]))
            elif cc == 'ltt':
                ltt.append(MapElement(t[0], t[1], t[2]))
            elif cc == 'tth':
                tth.append(MapElement(t[0], t[1], t[2]))
            elif cc == 'htl':
                htl.append(MapElement(t[0], t[1], t[2]))
        else:
            if d == 'seed-to-soil map:':
                cc = 'sts'
            elif d == 'soil-to-fertilizer map:':
                cc = 'stf'
            elif d == 'fertilizer-to-water map:':
                cc = 'ftw'
            elif d == 'water-to-light map:':
                cc = 'wtl'
            elif d == 'light-to-temperature map:':
                cc = 'ltt'
            elif d == 'temperature-to-humidity map:':
                cc = 'tth'
            elif d == 'humidity-to-location map:':
                cc = 'htl'

    ln = []
    
    convert_map_val(0, sts)
    
    



    t = 0
    # t2 = 999999999999
    # for i in range(1, len(seeds), 2):
    #     for x in range(seeds[i - 1], seeds[i - 1] + seeds[i]):
    #         print(f'\033[31mConverting seed:\033[0m \033[34m{x}\033[0m')
    #         t = (
    #         convert_map_val(
    #             convert_map_val(
    #                 convert_map_val(
    #                     convert_map_val(
    #                         convert_map_val(
    #                             convert_map_val(
    #                                 convert_map_val(x, sts)
    #                                 , stf)
    #                                 , ftw)
    #                                 , wtl)
    #                                 , ltt)
    #                                 , tth)
    #                                 , htl)
    #         )
    #         if t < t2:
    #             t2 = t
    #         else:
    #             pass
    # print(t2)
    #ln.sort()
    #print(ln[0])
    


if __name__ == '__main__':
    main()


# 2673917170 <- too high