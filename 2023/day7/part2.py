import re
from collections import Counter

class CardInfo():
    def __init__(self, cards, bet, type, mask):
        self.cards = cards    
        self.bet = bet
        self.type = type
        self.mask = mask


def find_type(cards):

    if 'J' in cards:
        c = Counter(cards)
        c1 = max(c, key=c.get)
        if c1 == 'J':
            t = cards.replace('J', '')
            if len(t) >= 1:
                c2 = Counter(t)
                cards = cards.replace('J', max(c2, key=c2.get))
            # if len(t) > c[c1]:
            #     c2 = Counter(t)
            #     cards = cards.replace('J', max(c2, key=c2.get))
        else:
            cards = cards.replace('J', c1)

    #print(f'\033[34m{cards}\033[0m')
    #five of a kind
    if all(x == cards[0] for x in cards):
        return('five-of-a-kind')
        
    sorted_card = [x for x in cards]
    sorted_card.sort()
    sorted_card = ''.join(sorted_card)

    r = re.findall(r'AAAA|KKKK|QQQQ|JJJJ|TTTT|9999|8888|7777|6666|5555|4444|3333|2222', sorted_card)
    if len(r) == 1:
        return('four-of-a-kind')

    
    r = re.findall(r'AAA|KKK|QQQ|JJJ|TTT|999|888|777|666|555|444|333|222', sorted_card)

    #full house
    if len(r) == 1:
        t = re.sub(r'AAA|KKK|QQQ|JJJ|TTT|999|888|777|666|555|444|333|222', '', sorted_card)
        if all(x == t[0] for x in t):
            return('full-house')

        #three of a kind
        elif t[0] != t[1] and t[0] not in r and t[1] not in r:
            return('three-of-a-kind')

    r = re.findall(r'AA|KK|QQ|JJ|TT|99|88|77|66|55|44|33|22', sorted_card)
    #two pair
    if len(r) == 2:
        return('two-pair')
    
    #one pair
    if len(r) == 1:
        t = re.sub(r'AA|KK|QQ|JJ|TT|99|88|77|66|55|44|33|22', '', sorted_card)
        if (
            (len(set(t)) == 3) and 
            t[0] not in r and 
            t[1] not in r and 
            t[2] not in r
        ):
            return('one-pair')

    if len(set(cards)) == 5:
        return('high-card')


def get_rank(hands):
    mask = {
        'K': 'B',
        'Q': 'C',
        'T': 'D',
        '9': 'E',
        '8': 'F',
        '7': 'G',
        '6': 'H',
        '5': 'I',
        '4': 'K',
        '3': 'L',
        '2': 'M',
        'J': 'N'
    }
    for hand in hands:
        t = hand.cards
        for m in mask:
            t = t.replace(m, mask[m])
        hand.mask = t
    sorted_hands = sorted(hands, key=lambda x: x.mask)
    
    # for s in sorted_hands:
    #     print(s.cards, s.mask)
    return sorted_hands




def main():
    with open('input.txt', 'r') as input_file:
        data = [i.rstrip().split(' ') for i in input_file]
    
    hands = []
    five_of_a_kind, four_of_a_kind, full_house, three_of_a_kind, two_pair, one_pair, high_card  = [], [], [], [], [], [], []

    for d in data:
        t = find_type(d[0])
        if t == 'five-of-a-kind':
            five_of_a_kind.append(
                CardInfo(
                    cards=d[0], 
                    bet=int(d[1]), 
                    type=t, 
                    mask=None
                )
            )
        elif t == 'four-of-a-kind':
            four_of_a_kind.append(
                CardInfo(
                    cards=d[0], 
                    bet=int(d[1]), 
                    type=t, 
                    mask=None
                )
            )
        elif t == 'full-house':
            full_house.append(
                CardInfo(
                    cards=d[0], 
                    bet=int(d[1]), 
                    type=t, 
                    mask=None
                )
            )
        elif t == 'three-of-a-kind':
            three_of_a_kind.append(
                CardInfo(
                    cards=d[0], 
                    bet=int(d[1]), 
                    type=t, 
                    mask=None
                )
            )
        elif t == 'two-pair':
            two_pair.append(
                CardInfo(
                    cards=d[0], 
                    bet=int(d[1]), 
                    type=t, 
                    mask=None
                )
            )
        elif t == 'one-pair':
            one_pair.append(
                CardInfo(
                    cards=d[0], 
                    bet=int(d[1]), 
                    type=t, 
                    mask=None
                )
            )
        else:
            high_card.append(
                CardInfo(
                    cards=d[0], 
                    bet=int(d[1]), 
                    type=t, 
                    mask=None
                )
            )
    

    if len(five_of_a_kind) > 0:
        for i in get_rank(five_of_a_kind):
            hands.append(i)
    if len(four_of_a_kind) > 0:
        for i in get_rank(four_of_a_kind):
            hands.append(i)
    if len(full_house)> 0:
        for i in get_rank(full_house):
            hands.append(i)
    if len(three_of_a_kind) > 0:
        for i in get_rank(three_of_a_kind):
            hands.append(i)
    if len(two_pair) > 0:
        for i in get_rank(two_pair):
            hands.append(i)
    if len(one_pair) > 0:
        for i in get_rank(one_pair):
            hands.append(i)
    if len(high_card) > 0:
        for i in get_rank(high_card):
            hands.append(i)

    winnings = 0
    c = len(hands)
    for i in range(0, len(hands)):
        print(hands[i].cards, hands[i].type, hands[i].mask, hands[i].bet, c)
        winnings += (hands[i].bet * c)
        c -= 1
        #print(winnings)
    
    print(winnings)


if __name__ == '__main__':
    main()


# 248935819 <- too low
# 248970048 <- too low
# 249239876 <- too low
# 249515436