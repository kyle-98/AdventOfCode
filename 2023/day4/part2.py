class CardData():
    def __init__(self, id, my_nums, win_nums, m_nums, cc):
        self.id = id
        self.my_nums = my_nums
        self.win_nums = win_nums
        self.m_nums = m_nums
        self.cc = cc


def main():
    with open('input.txt', 'r') as input_file:
        data = [i[5:].rstrip() for i in input_file]

    cards_data = []
    for row in data:
        t1 = row.split(' | ')
        t2 = t1[0].split(': ')

        mc = 0
        mn = [int(i) for i in list(filter(None, t2[1].split(' ')))]
        wn = [int(i) for i in list(filter(None, t1[1].split(' ')))]

        for i in wn:
            if i in mn:
                mc += 1

        cards_data.append(CardData(
            int(t2[0]), 
            mn,
            wn,
            mc,
            1
        ))

    for card_data in cards_data:
        #print(card_data.id, card_data.cc)
        for x in range(0, card_data.cc):
            for i in range(card_data.id, card_data.id + card_data.m_nums):
                cards_data[i].cc += 1
        
        # for i in cards_data:
        #     print(i.id, i.cc)
        #     print('-------------------')
        # print('@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    
    print(sum([i.cc for i in cards_data]))


if __name__ == '__main__':
    main()