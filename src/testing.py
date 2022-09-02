from instruction_rewrite import *

def optimize(program):
    new = program
    while ("+-" in new or "-+" in new or "<>" in new or "><" in new):
        new = new.replace("+-", "")
        new = new.replace("-+", "")
        new = new.replace("<>", "")
        new = new.replace("><", "")
    
    while (new[-1] == "<" or new[-1] == ">"):
        new = new[:-1]

    return new

def e(a, b, d):
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
    return (f[a:b])

def assert_eq(i, a, b):
    if a != b:
        raise Exception(f"Failed test {i}\nShould be {a}\nBut was   {b}")
    else:
        print(f"Passed test {i}")

def TESTS():
    t1 = "".join([
        MICRO_SETVALUE(5,5),
        MICRO_SETVALUE(3,5)
        ])
    r1 = e(0, 6, optimize(t1))
    s1 = [0,0,0,5,0,5]
    assert_eq(1, s1, r1)

    t2 = "".join([
        MICRO_SETVALUE(2,10),
        MICRO_DECREMENT(2, 5)
        ])
    r2 = e(0,3, optimize(t2))
    s2 = [0,0,5]
    assert_eq(2, s2, r2)

    t3 = "".join([
        MICRO_SETVALUE(1,5),
        FORMULATE_FOR_LOOP(1,1, MICRO_INCREMENT(4, 5))
        ])
    r3 = e(0, 5, optimize(t3))
    s3 = [0, 0, 0, 0, 25]
    assert_eq(3, s3, r3)

    t4 = "".join([
        MICRO_SETVALUE(2, 10),
        HELPER_DISTRIBUTE_INTO(2, 0, 4)
        ])
    r4 = e(0, 5, optimize(t4))
    s4 = [10, 0, 0, 0, 10]
    assert_eq(4, s4, r4)

    t5 = MICRO_SETVALUE(0, 10) + COMMAND_MOV(0, 1)
    r5 = e(0,2,optimize(t5))
    s5 = [0, 10]
    assert_eq(5, s5, r5)

    t6 = MICRO_SETVALUE(5, 10) + COMMAND_CPY(5, 7)
    r6 = e(0, 8, optimize(t6))
    s6 = [0,0,0,0,0,10,0,10]
    assert_eq(6, s6, r6)

    t7 = COMMAND_SET(3, 4) + COMMAND_SET(4, 5) + ALU_ADD()
    r7 = e(0,6,optimize(t7))
    s7 = [0,0,0,0,0,9]
    assert_eq(7, s7, r7)

    t8 = COMMAND_SET(3, 9) + COMMAND_SET(4, 5) + ALU_SUB()
    r8 = e(0,6,optimize(t8))
    s8 = [0,0,0,0,0,4]
    assert_eq(8, s8, r8)


def main():

    TESTS()

if __name__ == '__main__':
    main()