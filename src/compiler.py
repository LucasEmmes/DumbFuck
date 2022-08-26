import sys


vars = {"#A2":0,"#B2":1,"#M":2,"#A":3,"#B":4,"#C":5,"#D":6,"#D2":7,"R0":8,"R1":9,"R2":10,"R3":11,"R4":12,"R5":13,"R6":14,"R7":15,"R8":16,"R9":17,"R10":18,"R11":19,"R12":20,"R13":21,"R14":22,"R15":23,"R16":24,"R17":25,"R18":26,"R19":27,}

functions = {}

instructions = {}

def micro_add():
    pass

def micro_clear():
    return "[-]"

def micro_setvalue(x):
    if (x < 128):
        return x * "+"
    else:
        return x * "-"

def micro_move_ptr(start, destination):
    delta = vars[destination] - vars[start]
    if delta == 0:
        return ""
    elif delta > 0:
        return ">"*delta
    elif delta < 0:
        return "<"*(-1*delta)

def micro_move_cell_value(x, y):
    i = ""
    i += micro_move_ptr("#A", x)
    i += "[-"
    i += micro_move_ptr(x, y)
    i += "+"
    i += micro_move_ptr(y, x)
    i += "]"
    i += micro_move_ptr(x, "#A")
    return i

def comp_copy(x, y):
    i = ""
    i += micro_move_ptr("#A", x)
    i += "[-"
    i += micro_move_ptr(x, "#M")
    i += "+"
    i += micro_move_ptr("#M", y)
    i += "+"
    i += micro_move_ptr(y, x)
    i += "]"
    i += micro_move_ptr(x, "#A")
    i += micro_move_cell_value("#M", x)
    return i

def comp_set(x, val):
    i = ""
    i += micro_move_ptr("#A", x)
    i += micro_setvalue(val)
    i += micro_move_ptr(x, "#A")
    return i

def comp_move():
    pass

def optimize(program):
    new = program
    while ("+-" in new or "-+" in new or "<>" in new or "><" in new):
        new = new.replace("+-", "")
        new = new.replace("-+", "")
        new = new.replace("<>", "")
        new = new.replace("><", "")
    return new

def main():

    vars["X"] = 21
    vars["Y"] = 22
    vars["Z"] = 23
    result = micro_move_ptr("#A2", "#A")
    result += comp_set("X", 9)
    result += comp_copy("X", "Y")

    print(optimize(result))


if __name__ == "__main__": main()