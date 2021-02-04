import sys
from itu.algs4.fundamentals.stack import Stack

line = sys.stdin.readline()


def check_syntax(s: str):
    stack = Stack()
    map_ = {
        "(": [0,1],
        "[": [0,2],
        "{": [0,3],
        ")": [1,1],
        "]": [1,2],
        "}": [1,3]
    }

    for cha in s.strip():
        if map_[cha][0] == 0:
            stack.push(map_[cha][1])
        elif map_[cha][0] == 1:
            try:
                if stack.peek() == map_[cha][1]:
                    stack.pop()
                else: return "0"
            except: return "0"

    if stack.is_empty() == True:
        return "1"
    else: return "0"

def main():
    print(check_syntax(line))

if __name__ == '__main__':
    main()