import program


def optimize(program):
    new = program
    while ("+-" in new or "-+" in new or "<>" in new or "><" in new):
        new = new.replace("+-", "")
        new = new.replace("-+", "")
        new = new.replace("<>", "")
        new = new.replace("><", "")
    return new

def main():
    p = program.PROGRAM()

    prog = ""

    p.add_variable("X")
    p.add_variable("Y")
    p.add_variable("Z")


    prog += p.composite.move_value_into_cell(3, 3)
    prog += p.composite.move_value_into_cell(4, 5)
    print(p.composite.alu_multiply())
    # prog += p.composite.move_value_into_cell(p.translate_variable("X"), 3)
    # prog += p.composite.move_value_into_cell(p.translate_variable("Y"), 5)
    # prog += p.composite.multiply_cells_into(p.translate_variable("X"), p.translate_variable("Y"), p.translate_variable("Z"))

    print(optimize(prog))



if __name__ == '__main__':
    main()