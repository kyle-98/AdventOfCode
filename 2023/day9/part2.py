class CustomSequence():
    def __init__(self, sub_seqs, next_val):
        self.sub_seqs = sub_seqs
        self.next_val = next_val


def main():
    with open('input.txt', 'r') as input_file:
        data = [[int(num) for num in line.rstrip().split(' ')] for line in input_file]
    
    sequences_list = []
    for d in data:
        this_data, ph_subseq, sub_seqs = d, [], [d[::-1]]
        while True:
            if ph_subseq != []:
                this_data = ph_subseq
                ph_subseq = []
            for i in range(1, len(this_data)):
                #print(temp[i], temp[i - 1])
                ph_subseq.append(this_data[i] - this_data[i - 1])
            
            sub_seqs.append(ph_subseq[::-1])
            if all(a == 0 for a in ph_subseq):
                sub_seqs.reverse()
                sequences_list.append(CustomSequence(sub_seqs, None))
                break
    ex_vals = 0
    for sequence in sequences_list:
        sequence.sub_seqs[0].append(0)
        for s in range(0, len(sequence.sub_seqs) - 1):
            sequence.sub_seqs[s + 1].append(sequence.sub_seqs[s + 1][-1] - sequence.sub_seqs[s][-1])
        ex_vals += sequence.sub_seqs[-1][-1]
    print(ex_vals)


if __name__ == '__main__':
    main()