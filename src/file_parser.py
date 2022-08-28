from typing import List
import instructions

def parse_file(filename : str) -> List[str] | bool:
    with open(filename) as f:
        data = f.read()
    
    # Check for all categories
    if data.count(".data") != 1: raise f"Did not find \".data\" section in {filename}"
    if data.count(".funcs") != 1: raise f"Did not find \".funcs\" section in {filename}"
    if data.count(".code") != 1: raise f"Did not find \".code\" section in {filename}"

    # Semi-Tokenize lines
    lines = data.split("\n")
    for i, line in enumerate(lines):
        if "#" in line:
            comment_position = line.index("#")
            line = line[:comment_position]
        while " " in line:
            line = line.replace(" ", "")
    
        lines[i] = line
    while "" in lines:
        lines.remove("")

    
    index_data = lines.index(".data")
    index_funcs = lines.index(".funcs")
    index_code = lines.index(".code")

    data_section = lines[index_data+1:index_funcs]
    funcs_section = lines[index_funcs+1:index_code]
    code_section = lines[index_code+1:]
    
    print(data_section)
    print(funcs_section)
    print(code_section)


if __name__ == '__main__':
    parse_file("z.df")