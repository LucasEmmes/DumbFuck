import composite

class PROGRAM:
    def __init__(self):
        self.program = ""
        self.variables = {"#A2":0,"#B2":1,"#M":2,"#A":3,"#B":4,"#C":5,"#D":6,"#D2":7}
        self.functions = {}
        self.next_variable_position = len(self.variables)
        self.composite = composite.COMPOSITE()
    
    def optimize(self):
        pass

    def add_variable(self, variable_name):
        if "[" in variable_name:
            variable_name, variable_size = variable_name[:-1].split("[")
            self.variables[variable_name] = self.next_variable_position
            self.next_variable_position += int(variable_size)
        else:
            self.variables[variable_name] = self.next_variable_position
            self.next_variable_position += 1

    def translate_variable(self, variable_name):
        if "[" in variable_name:
            variable_name, variable_size = variable_name[:-1].split("[")
            return self.variables[variable_name] + int(variable_size)
        else:
            return self.variables[variable_name]

    def parse_variables(self):
        pass

    def parse_functions(self):
        pass

    def parse_instructions(self):
        pass