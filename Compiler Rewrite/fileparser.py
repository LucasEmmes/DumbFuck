from copy import deepcopy
from typing import List

def remove_comments(lines : List[str]) -> List[str]:
    for i, row in enumerate(deepcopy(lines)):
        if "//" in row:
            ind = row.index("//")
            lines[i] = row[:ind]

    # Clean up leading / trailing spaces
    for i, row in enumerate(deepcopy(lines)):
        if len(row) > 0:
            try:
                while row[0] == " ":
                    row = row[1:]
                while row[-1] == " ":
                    row = row[:-1]
            except Exception: pass
            lines[i] = row
    while "" in lines:
        lines.remove("")

def parse_file(filename : str) -> List[str]:
    with open(filename) as f:
        data = f.read()
    
    # Check for all categories
    if data.count(".data") != 1: raise f"Did not find \".data\" section in {filename}"
    if data.count(".funcs") != 1: raise f"Did not find \".funcs\" section in {filename}"
    if data.count(".code") != 1: raise f"Did not find \".code\" section in {filename}"

    lines = data.split("\n")
    
    # Remove comments
    remove_comments(lines)

    # Split into sections
    ind_func = lines.index(".funcs")
    section_data = lines[1:ind_func]
    ind_code = lines.index(".code")
    section_func = lines[ind_func+1:ind_code]
    section_code = lines[ind_code+1:]

    return section_data, section_func, section_code