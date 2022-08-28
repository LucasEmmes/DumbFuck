from instructions import *


def main():

    print(COMMAND_SET(0, 3) + COMMAND_SET(1, 5) + COMMAND_MOV(0, 1))

if __name__ == '__main__':
    main()