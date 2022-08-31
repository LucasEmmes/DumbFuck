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
        COMMAND_SET(3, 3) +
        COMMAND_SET(4, 3)  +
        ALU_CMP_A_EQUALS_B()
    ))

if __name__ == '__main__':
    main()