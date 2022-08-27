import sys

variables = {"#A2":0,"#B2":1,"#M":2,"#A":3,"#B":4,"#C":5,"#D":6,"#D2":7,"R0":8,"R1":9,"R2":10,"R3":11,"R4":12,"R5":13,"R6":14,"R7":15,"R8":16,"R9":17,"R10":18,"R11":19,"R12":20,"R13":21,"R14":22,"R15":23,"R16":24,"R17":25,"R18":26,"R19":27,}
variables_size = 28


functions = {}

instructions = {}

ptr_position = 0

def check_a_equals_b_into_d():
    return "[->-<]>>+<[>-<[-]]<"

def check_a_greater_than_b_into_d():
    return "[->[-[-<<+>>]>>-<<]<<[->>+<<]>>>>+<<<]>[-]<"

def micro_add_a_and_b_into_c():
    return "[->>+<<]>[->+<]<"

def micro_clear_current_cell():
    return "[-]"

def micro_setvalue(x):
    if (x < 128):
        return x * "+"
    else:
        return x * "-"

def micro_move_ptr(destination):
    global ptr_position
    delta = parse_location(destination) - ptr_position
    ptr_position = parse_location(destination)
    if delta == 0:
        return ""
    elif delta > 0:
        return ">"*delta
    elif delta < 0:
        return "<"*(-1*delta)

def micro_move_cell_value(x, y):
    i = ""
    i += micro_move_ptr("#A2", x)
    i += "[-"
    i += micro_move_ptr(x, y)
    i += "+"
    i += micro_move_ptr(y, x)
    i += "]"
    i += micro_move_ptr(x, "#A2")
    return i

def comp_copy(x, y):
    i = ""
    i += micro_move_ptr("#A2", x)
    i += "[-"
    i += micro_move_ptr(x, "#M")
    i += "+"
    i += micro_move_ptr("#M", y)
    i += "+"
    i += micro_move_ptr(y, x)
    i += "]"
    i += micro_move_ptr(x, "#A2")
    i += micro_move_cell_value("#M", x)
    return i

def comp_setvalue(x, val):
    i = ""
    i += micro_move_ptr(x)
    i += micro_setvalue(val)
    i += micro_move_ptr("#A2")
    return i

def comp_move(x, y):
    i = ""
    i += micro_move_ptr("#A2", y)
    i += micro_clear()
    i += micro_move_ptr(y, "#A2")
    i += micro_move_cell_value("X", "Y")
    return i

def add_var(x, size):
    global variables
    global variables_size
    if x in variables.keys():
        raise Exception("Redeclaration of variable!")
    else:
        print("adding ", x, " at ", variables_size)
        variables[x] = variables_size
        variables_size += size

def optimize(program):
    new = program
    while ("+-" in new or "-+" in new or "<>" in new or "><" in new):
        new = new.replace("+-", "")
        new = new.replace("-+", "")
        new = new.replace("<>", "")
        new = new.replace("><", "")
    return new

def parse_location(var_name):
    global variables
    if "[" not in var_name:
        return variables[var_name]
    else:
        temp = var_name.split("[")
        temp[1] = int(temp[1].replace("]", ""))
        return variables[temp[0]] + temp[1]

def main():
    result = ""
    # First variable should be at cell 28


    result += comp_setvalue("#A", 12)
    result += comp_setvalue("#B", 12)
    result += micro_move_ptr("#A")
    result += check_a_greater_than_b_into_d()
    print(optimize(result))


if __name__ == "__main__": main()