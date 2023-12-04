class CardData():
    def __init__(self, id, my_nums, win_nums):
        self.id = id
        self.my_nums = my_nums
        self.win_nums = win_nums


def main():
    with open('input.txt', 'r') as input_file:
        data = [i[5:].rstrip() for i in input_file]

    cards_data = []
    for row in data:
        t1 = row.split(' | ')
        t2 = t1[0].split(': ')
        cards_data.append(CardData(
            int(t2[0]), 
            [int(i) for i in list(filter(None, t2[1].split(' ')))], 
            [int(i) for i in list(filter(None, t1[1].split(' ')))]
        ))

    points = []
    for card_data in cards_data:
        tp = 1
        c = 0
        for num in card_data.win_nums:
            if num in card_data.my_nums:
                if c != 0:
                    tp += tp
                c += 1
        if c > 0:
            points.append(tp)

    print(sum(points))

if __name__ == '__main__':
    main()