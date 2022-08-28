import micro

# ALL COMPOSITE FUNCTIONS MUST START AND END POINTING AT CELL 0

# A2 B2 M A B C D D2
# 0  1  2 3 4 5 6 7

class COMPOSITE:
    def __init__(self):
        self.micro = micro.MICRO()

    def alu_add(self):
        command = ""
        start_pos = self.micro.ptr_position
        command += self.micro.move_ptr_to(3)
        command += "[->>+<<]>[->+<]<"
        command += self.micro.move_ptr_to(start_pos)
        return command

    def alu_sub(self):
        start_pos = self.micro.ptr_position
        command = ""
        command += self.micro.move_ptr_to(3)
        command += "[->>+<<]>[->-<]<"
        command += self.micro.move_ptr_to(start_pos)
        return command

    def alu_multiply(self):
        start_pos = self.micro.ptr_position
        command = ""
        command += self.micro.move_ptr_to(3)
        # For A do loop
        command += self.micro.loop_instructions(
            # Copy B to C and M
            self.distribute_cell_over(4, 2, 5),
            # Put M back into B
            self.cut_cell_value_into_cell(5, 2)
        )
        # Move to B and reset
        command += self.micro.move_ptr_to(4)
        command += self.micro.clear_cell()
        
        return command

    def alu_divide(self):
        pass

    def cmp_a_greater_than_b(self):
        pass

    def cmp_a_equals_b(self):
        pass


    def distribute_cell_over(self, x, *args):
        """Distributes x over a variable number of cells"""
        command = ""
        # Goto x
        command += self.micro.move_ptr_to(x)
        # For x do loop
        command += self.micro.loop_instructions(
            # Goto and increment cells
            "".join([self.micro.move_ptr_to(i) + "+" for i in args]),
            # Goto x
            self.micro.move_ptr_to(x)
        )
        # Goto 0
        command += self.micro.move_ptr_to(0)

        return command

    def cut_cell_value_into_cell(self, x, y):
        command = ""
        # Goto x
        command += self.micro.move_ptr_to(x)
        # For x do loop
        command += self.micro.loop_instructions(
            # Goto y
            self.micro.move_ptr_to(y),
            # Increment
            "+",
            # Goto x
            self.micro.move_ptr_to(x)
        )
        # Go back to 0
        command += self.micro.move_ptr_to(0)

        return command

    def copy_cell_value(self, x, y):
        command = ""
        # Goto x
        command += self.micro.move_ptr_to(x)
        # Distribute x over y and M
        command += self.distribute_cell_over(x, y, 2)
        # Move M back to x
        command += self.cut_cell_value_into_cell(2, x)
        # Goto 0
        command += self.micro.move_ptr_to(0)
        
        return command

    def move_value_into_cell(self, x, value):
        command = ""
        # Goto x
        command += self.micro.move_ptr_to(x)
        # Reset
        command += self.micro.clear_cell()
        # Add value
        command += self.micro.set_cell_value(value)
        # Goto 0
        command += self.micro.move_ptr_to(0)

        return command
    
    def add_cells_into(self, x, y, z):
        command = ""
        # Move x into #A
        command += self.cut_cell_value_into_cell(x, 3)
        # Move y into #B
        command += self.cut_cell_value_into_cell(y, 4)
        # ALU add
        command += self.alu_add()
        # Move #C into z
        command += self.cut_cell_value_into_cell(5, z)
        # Goto 0
        command += self.micro.move_ptr_to(0)

        return command

    def sub_cells_into(self, x, y, z):
        pass

    def multiply_cells_into(self, x, y, z):
        """Loads cells X and Y into A and B, does ALU multiplication, then stores resulting C into Z"""
        command = ""
        command += self.copy_cell_value(x, 3)
        command += self.copy_cell_value(y, 4)
        command += self.alu_add()
        command += self.micro.move_ptr_to(z)
        command += self.micro.clear_cell()
        command += self.cut_cell_value_into_cell(5, z)
        
        return command

    def divide_cells_into(self, x, y, z):
        pass
