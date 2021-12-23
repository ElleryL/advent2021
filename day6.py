import multiprocessing



def oneDay(state):
    pool = multiprocessing.Pool()
    updated_state = pool.map(reproduce,state)
    numZeros = state.count(0)
    while numZeros > 0:
        updated_state.append(8)
        numZeros -= 1
    return updated_state 

def numOfReproduce(state):
    daysRemain = 256
    while daysRemain > 0:
        state = oneDay(state)
        daysRemain -= 1
    return len(state)


def reproduce(fish):
    if fish == 0:
        return 6
    return fish - 1



if __name__ == "__main__":
    myfile = open("input6.txt")
    lines = myfile.readlines()
    lines = [line for line in lines]
    line = [int(fish) for fish in lines[0].split(",")]
    ans1 = numOfReproduce(line)
    print(ans1)