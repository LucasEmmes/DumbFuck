from instruction_rewrite import *
testctr = 1

def optimize(program):
    new = program
    while ("+-" in new or "-+" in new or "<>" in new or "><" in new or "[-][-]" in new):
        new = new.replace("+-", "")
        new = new.replace("-+", "")
        new = new.replace("<>", "")
        new = new.replace("><", "")
        new = new.replace("[-][-]", "[-]")
    
    while (new[-1] == "<" or new[-1] == ">"):
        new = new[:-1]

    return new

def e(d):
    (i:=0,s:=[],c:=0,p:=0,f:=[0])
    while i<len(d):
        c=d[i]
        if c==">":p+=1;f.append(0)if p==len(f)else 0
        if c=="<":p-=1 if p>0 else f.insert(0,0)
        if c=="+":f[p]=f[p]+1%256
        if c=="-":f[p]=f[p]-1%256
        if c==".":print(chr(f[p]),end="")
        if c==",":e=input();f[p]=(ord(e[0])if len(e)>0 else 0)%256
        if c=="[":
            if f[p]:s.append(i-1)
            else:
                c=1
                while c!=0:
                    i+=1
                    if d[i]=="[":c+=1
                    elif d[i]=="]":c-=1
        if c=="]":i=s.pop()
        i+=1
    return f

def assert_eq(i, b, a):
    if a != b:
        raise Exception(f"Failed test {i}\nShould be {a}\nBut was   {b}")
    else:
        print(f"Passed test {i}")

def test(expected_result, instructions, debug=False):
    global testctr
    
    if debug:
        print(f"Debugger code for test {testctr}")
        print(optimize(instructions))
        return

    assert_eq(testctr, e(optimize(instructions)), expected_result)

    testctr+=1

def RUN_TESTS():

    # 1 Test setvalue
    test([0,0,0,5,0,5],
    "".join([
        MICRO_SETVALUE(5,5),
        MICRO_SETVALUE(3,5)
    ]))

    # 2 Test decrement
    test([0,0,5],
    "".join([
        MICRO_SETVALUE(2,10),
        MICRO_DECREMENT(2, 5)
    ]))

    # 3 Test for-loop
    test([0, 0, 0, 0, 25],
    "".join([
        MICRO_SETVALUE(1,5),
        FORMULATE_FOR_LOOP(1,1, MICRO_INCREMENT(4, 5))
    ]))

    # 4 Test distribution over multiple
    test([10, 0, 0, 0, 10],
    "".join([
        MICRO_SETVALUE(2, 10),
        HELPER_DISTRIBUTE_INTO(2, 0, 4)
    ]))

    # 5 Test move
    test([0,10],"".join([
        MICRO_SETVALUE(0, 10),
        COMMAND_MOV(0, 1)
    ]))

    # 6 Test copy
    test([0,0,0,0,0,10,0,10],
    "".join([
        MICRO_SETVALUE(5, 10),
        COMMAND_CPY(5, 7)
    ]))

    # 7 Test alu add
    test([0,0,0,0,0,9],
    "".join([
        COMMAND_SET(3, 4),
        COMMAND_SET(4, 5),
        ALU_ADD()
    ]))

    # 8 Test alu sub
    test([0,0,0,0,0,4],
    "".join([
        COMMAND_SET(3, 9),
        COMMAND_SET(4, 5),
        ALU_SUB()
    ]))

    # 9 Test command add
    test([0,0,0,0,0,0,0,0,12],
    "".join([
        COMMAND_SET(6, 4),
        COMMAND_SET(7, 8),
        COMMAND_ADD(6, 7, 8)
    ]))

    # 10 Test alu multiply
    test([0,0,0,0,0,12],
    "".join([
        COMMAND_SET(3, 3),
        COMMAND_SET(4, 4),
        ALU_MUL()
    ]))

    # 11 Test command sub
    test([0,0,0,0,0,0,0,0,11],
    "".join([
        COMMAND_SET(6, 21),
        COMMAND_SET(7, 10),
        COMMAND_SUB(6, 7, 8)
    ]))

    # 12 Test command mul
    test([0,0,0,0,0,0,0,0,21],
    "".join([
        COMMAND_SET(6, 3),
        COMMAND_SET(7, 7),
        COMMAND_MUL(6, 7, 8)
    ]))

    # 13 Test alu a==b
    test([0,0,0,0,0,1],
    "".join([
        COMMAND_SET(3, 5),
        COMMAND_SET(4, 5),
        ALU_CMP_A_EQUALS_B()
    # ]), True)
    ]))

    # 14 Test 
    

    # test([],
    # "".join([

    # ]))


def main():

    RUN_TESTS()
    print("All tests successful")

if __name__ == '__main__':
    main()