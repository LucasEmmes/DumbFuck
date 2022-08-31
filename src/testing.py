from instructions import *

def optimize(program):
    new = program
    while ("+-" in new or "-+" in new or "<>" in new or "><" in new):
        new = new.replace("+-", "")
        new = new.replace("-+", "")
        new = new.replace("<>", "")
        new = new.replace("><", "")
    return new


def main():

    print(optimize(
        COMMAND_SET(0, 10) +
        HELPER_DISTRIBUTE_INTO(0, 5, 6, 1, 2, 3, 4)
    ))

if __name__ == '__main__':
    main()