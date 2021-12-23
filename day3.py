from collections import Counter


def BinToDec(bin):
    res = 0
    for ele in bin:
        res = (res << 1) | ele
    return res

def powerConsumption(lines):
    gamma,epsilon = [], []
    for line in list(zip(*lines)):
        counter = Counter(line)
        gamma.append(int(max(counter,key=counter.get)))
        epsilon.append(int(min(counter,key=counter.get)))
    return BinToDec(gamma) * BinToDec(epsilon)


def oxygenGeneratorRating(lines):
    n_bit = max([len(line) for line in lines])
    cur_bit = 0
    while cur_bit < n_bit and len(lines) > 1:
        counter = Counter([line[cur_bit] for line in lines])
        Max =  "1" if counter['0'] == counter['1'] else max(counter,key=counter.get)
        index = [i for i in range(len(lines)) if lines[i][cur_bit] == Max ]
        lines = [lines[i] for i in index]
        cur_bit += 1
    
    return BinToDec([int(val) for val in lines[0]])

def scrubberRating(lines):
    n_bit = max([len(line) for line in lines])
    cur_bit = 0
    while cur_bit < n_bit and len(lines) > 1:
        counter = Counter([line[cur_bit] for line in lines])
        Min =  "0" if counter['0'] == counter['1'] else min(counter,key=counter.get)
        index = [i for i in range(len(lines)) if lines[i][cur_bit] == Min ]
        lines = [lines[i] for i in index]
        cur_bit += 1
    
    return BinToDec([int(val) for val in lines[0]])

def lifeSupportRating(lines):
    ogr = oxygenGeneratorRating(lines)
    co2 = scrubberRating(lines)
    return ogr * co2

if __name__ == "__main__":
    myfile = open("input3.txt")
    lines = myfile.readlines()
    lines = [line[:-1] for line in lines]
    ans2 = lifeSupportRating(lines)
    print(ans2)
 