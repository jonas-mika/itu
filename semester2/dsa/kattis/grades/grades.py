import sys

lines = sys.stdin.readlines()
n = int(lines[0]) # number of students to be sorted
# S = {grade: student for student, grade in [line.strip().split(' ') for line in lines[1:]]}
S = {}
for line in lines[1:]:
    student, grade = line.strip().split(' ')
    if grade not in S:
        S[grade] = [student]
    else: S[grade].append(student)

grade_lookup = {
        "A": 0,
        "B": 100,
        "C": 200, 
        "D": 300, 
        "E": 400,
        "X": -100,
        "F": 600,
        "+": -1,
        "-": 1
        }

def is_higher(grade1, grade2):
    value1 = sum([grade_lookup[letter] for letter in grade1])
    value2 = sum([grade_lookup[letter] for letter in grade2])

    if value1 < value2:
       return True 
    else: return False

def sort_grades(L: list):
    N = len(L)

    for i in range(1,N):
        for j in range(i, 0, -1):
            if not is_higher(L[j], L[j-1]):
                break
            t = L[j]
            L[j] = L[j-1]
            L[j-1] = t
    return L 

def solve(S):
    # sorting grade
    sorted_grades = sort_grades(list(S.keys()))

    for grade in sorted_grades:
        sorted_students = sorted(S[grade])
        for student in sorted_students:
            print(student)

if __name__ == '__main__':
    solve(S)
