class Spring():
    def __init__(self, record, eng_record):
        self.record = record
        self.eng_record = eng_record

def main():
    with open('test_input.txt', 'r') as input_file:
        data = [Spring(line.rstrip().split(' ')[0], [int(l) for l in line.rstrip().split(' ')[1].split(',')]) for line in input_file]

    for d in data:
        print(d.record, d.eng_record, '\n')
if __name__ == '__main__':
    main()