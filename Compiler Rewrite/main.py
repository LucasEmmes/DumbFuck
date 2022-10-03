import fileparser

def main():
    section_data, section_func, section_code = fileparser.parse_file("z.df")

    print(section_data, section_func, section_code)

if __name__=="__main__":main()