import sys


class shell:
    def __init__(self):
        while(True):
            print(
                "Select an option from the following menu:\n\n\
                    1: Option_1\n\
                    \n\
                    0: exit"
            )
            x = input("ENTER: ")
            if x is "0":
                sys.exit()

shell()
