# python brute force substring search
class SubstringSearch(str):
    def __init__(self, string):
        self.txt = string
        super().__init__()

    def contains(self, pat):
        n = len(self.txt)
        m = len(pat)

        for c in range(n-m + 1):  # inclusive interval
            for j in range(m):
                # print(self.txt[c+j], pat[j])
                if self.txt[c+j] != pat[j]:
                    break
                if j+1 == m:
                    return True
        return False

    def alternative_contains(self, pat):
        n = len(self.txt)
        m = len(pat)

        i = 0
        j = 0
        print('Starting Search...\n')
        while i < n and j < m:
            print(f'Compare: {self.txt[i]}[{i}] to {pat[j]}[{j}]')
            if self.txt[i] == pat[j]:
                print('match')
                j += 1
            else:
                print('no match')
                i -= j
                j = 0
            i += 1
        print(f'Search Ended, i={i}, j={j}')
        if j == m:  # found (hit end of pattern)
            return True
        else:  # not found (hit end of text)
            return False

    def find(self, pat):
        n = len(self.txt)
        m = len(pat)

        for c in range(n-m + 1):
            for j in range(m):
                # print(self.txt[c+j], pat[j])
                if self.txt[c+j] != pat[j]:
                    break
                if j+1 == m:
                    if n == 1:
                        return(c)
                    else:
                        return((c, c+j))
        return False

    def findall_matches(self, pat):
        n = len(self.txt)
        m = len(pat)

        matches = []
        for c in range(n-m + 1):
            for j in range(m):
                if self.txt[c+j] != pat[j]:
                    break
                if j+1 == m:
                    matches.append(self.txt[c: c + len(pat)])
        return matches

    def findall_indices(self, pat):
        n = len(self.txt)
        m = len(pat)

        indices_matches = []
        for c in range(n-m + 1):
            for j in range(m):
                if self.txt[c+j] != pat[j]:
                    break
                if j+1 == m:
                    if n == 1:
                        indices_matches.append(c)
                    else:
                        indices_matches.append((c, c + j))
        return indices_matches


test = SubstringSearch("heyhello")
pat = "hell"
print(test.alternative_contains(pat))
