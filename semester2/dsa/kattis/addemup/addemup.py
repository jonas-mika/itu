import sys

# read in the input
#lines = sys.stdin.readlines()

#n, s = [int(i) for i in lines[0].strip().split()]
#N = [i for i in lines[1].strip().split()]


def turn_card(string: str):
    n_rev = list(reversed([l for l in string]))

    for i in range(len(n_rev)):
        if n_rev[i] in ["3","4","7"]:
            return None
        elif n_rev[i] == "6":
            n_rev[i] = "9"
        elif n_rev[i] == "9":
            n_rev[i] = "6"

    return "".join(n_rev)


def valid_combination(ON: list, N: list):
    indexes = []
    for element in N:
        indexes.append(ON.index(element))
    for index in indexes:
        if index+len(ON)/2 in indexes:
            return False
    return True

def solve(n,s,N):
    # make the list of all cards
    reversed_cards = [] 
    for card in N:
        reversed_cards.append(turn_card(str(card)))

    N.extend(reversed_cards)
    print(N)

    # iterate over all possible combinations and see if the sums match
    combinations = set()
    for i in range(len(N)):
        for j in range(len(N)):
            if i != j and N[i]!=N[j] and N[i] != None and N[j] != None:
                combinations.add((N[i],N[j]))

    print(combinations)

    for combination in combinations:
        if valid_combination(N, combination) == True:
            print(combination)
            if sum([int(i) for i in combination]) == s:
                print(combination)
                return "YES"
    return "NO"

if __name__ == '__main__':
    print(solve(5,100,["50","25","10","67","21","72","99"]))
