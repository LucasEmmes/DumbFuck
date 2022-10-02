from typing import List
import instructions

def parse_file(filename : str) -> List[str] | bool:
    with open(filename) as f:
        data = f.read()
    
    # Check for all categories
    if data.count(".data") != 1: raise f"Did not find \".data\" section in {filename}"
    if data.count(".funcs") != 1: raise f"Did not find \".funcs\" section in {filename}"
    if data.count(".code") != 1: raise f"Did not find \".code\" section in {filename}"



if __name__ == '__main__':
    parse_file("z.df")