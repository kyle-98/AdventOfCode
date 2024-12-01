import numpy as np

def main():
    with open('test_input.txt', 'r') as input_file:
        #data = np.array([line.rstrip() for line in input_file])
        data = (line.readline() for line in input_file) 
    print(data)


if __name__ == '__main__':
    main()