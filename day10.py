
def computeCorrupt(lines):
    score = {")":3, "]":57,"}":1197,">":25137}
    ans = 0
    for line in lines:
        char,_ = detectCorrupt(line)
        if char is not None:
            ans += score[char]
    return ans


def detectCorrupt(line):
    stack = []
    open_set = set({"{", "[", "<", "("})
    closed_set = {"}":"{", "]":"[", ">":"<", ")":"(" }
    for i, char in enumerate(line):
        if char in open_set:
            stack.append(char)
        elif char in closed_set:
            if stack[-1] == closed_set[char]:
                stack.pop()
            else:
                return char, stack
    return None, stack


def completeIncomplete(lines):
    total_scores = []
    scores = {"(":1, "[":2, "{":3, "<":4}
    for line in lines:
        _, stack = detectCorrupt(line)
        if _ is None:
            score = 0
            while stack:
                score = score * 5 + scores[stack.pop()]
            total_scores.append(score)
    total_scores.sort()
    return total_scores[len(total_scores)//2]


if __name__ == "__main__":
    myfile = open("input10.txt")
    lines = myfile.readlines()
    lines = [line[:-1] for line in lines]
    ans2 = completeIncomplete(lines)
    print(ans2)