class KMP:
    def __init__(self, txt):
        self.txt = txt
        self.n = len(txt)

    @staticmethod
    def build_dfa(pat, r=256):
        dfa = [[0 for _ in range(0, len(pat))] for _ in range(0, r)]
        dfa[ord(pat[0])][0] = 1
        X = 0
        for j in range(1, len(pat)):
            # Compute dfa[][j]
            for c in range(0, r):
                dfa[c][j] = dfa[c][X]  # Copy mismatch cases
            dfa[ord(pat[j])][j] = j + 1  # Set match case
            X = dfa[ord(pat[j])][X]  # Update restart state
        return dfa

    def search(self, pat):
        """Returns the index of the first occurrrence of the pattern string in the
        text string.
        :param txt: the text string
        :return: the index of the first occurrence of the pattern string
        in the text string; N if no such match
        """

        n = len(self.txt)
        m = len(pat)

        dfa = self.build_dfa(pat)

        i = 0
        j = 0
        while i < n and j < m:
            j = dfa[ord(self.txt[i])][j]
            i += 1
        if j == m:  # found (hit end of pattern)
            return True
        else:  # not found (hit end of text)
            return False


kmp = KMP('aaaababaabbabbbaba')
pat = 'babaabbbb'

print(kmp.search(pat))
