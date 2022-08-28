class MICRO:
    def __init__(self):
        self.ptr_position = 0

    def clear_cell(self):
        return "[-]"

    def set_cell_value(self, cell_value):
        if cell_value < 128:    return "+" * cell_value
        else:                   return "-" * (256 - cell_value)

    def move_ptr_to(self, cell_number):
        location_delta = cell_number - self.ptr_position
        self.ptr_position = cell_number
        if location_delta < 0:  return "<" * -location_delta
        else:                   return ">" * location_delta

    def loop_instructions(self, *args):
        return "[-" + "".join(args) + "]"
    