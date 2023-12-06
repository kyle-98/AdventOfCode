
class MapElement():
    def __init__(self, dest, src, rang):
        self.dest = dest
        self.src = src
        self.rang = rang

def convert_map_val(val, sts):
    found = False
    for s in sts:
        if val < s.src:
            pass
        elif val >= s.src and val <= (s.src + s.rang) - 1:
            found = True
            return abs(val - s.src) + s.dest
        else:
            pass
    if not found:
        return val

def main():
    with open('input.txt', 'r') as input_file:
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
    for seed in seeds:
        # soil_num = convert_map_val(seed, sts)
        # fert_num = convert_map_val(soil_num, stf)
        # watr_num = convert_map_val(fert_num, ftw)
        # ligt_num = convert_map_val(watr_num, wtl)
        # temp_num = convert_map_val(ligt_num, ltt)
        # humd_num = convert_map_val(temp_num, tth)
        # loct_num = convert_map_val(humd_num, htl)
        ln.append(
            convert_map_val(
                convert_map_val(
                    convert_map_val(
                        convert_map_val(
                            convert_map_val(
                                convert_map_val(
                                    convert_map_val(seed, sts)
                                    , stf)
                                    , ftw)
                                    , wtl)
                                    , ltt)
                                    , tth)
                                    , htl)
        )
    ln.sort()
    print(ln[0])


if __name__ == '__main__':
    main()


# 2673917170 <- too high