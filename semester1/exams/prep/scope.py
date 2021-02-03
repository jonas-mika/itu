# this is a file to explore the scope of variables in prep for the idsp exam

my_name = "Jonas-Mika"
#print = "Hello"

# print(my_name)

# enclosed scope
def main():
    L = [1,2,3]

    def print_list():
        for item in L:
            print(item)

    print("-"*5 + "INNER FUNCTION" + "-"*5)
    print_list()


    print("-"*5 + "OUTER FUNCTION" + "-"*5)
    for item in L:
        print(item)

main()