
# TRY TO USE AS MANY MICROINSTRUCTIONS AS POSSIBLE
# A2, B2, M, A, B, AND C MUST BE 0 BY THE END

class ALU:
    def __init__(self, micro_instructor):
        self.micro = micro_instructor

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
        command += self.micro.loop_instructions(
            
        )

    def alu_divide(self):
        pass

    def cmp_a_greater_than_b(self):
        pass

    def cmp_a_equals_b(self):
        pass
