
addresses = {"#A2":0,"#B2":1,"#M":2,"#A":3,"#B":4,"#C":5,"#D":6,"#D2":7}
next_var_address = len(addresses)

# ------------------------------------------------------------------------------------------------------------
# META FUNCTIONS ---------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------


def META_ADD_VARIABLE(VAR_NAME):
    """Parses the name of VAR_NAME and its size, then registers it in the index of known variables"""
    global addresses
    global next_var_address
    if "[" in VAR_NAME:
        VAR_NAME, VAR_SIZE = VAR_NAME[:-1].split("[")
        if VAR_NAME in addresses: raise Exception(f"Redeclaration of {VAR_NAME}")
        addresses[VAR_NAME] = next_var_address
        next_var_address += int(VAR_SIZE)
    else:
        if VAR_NAME in addresses: raise Exception(f"Redeclaration of {VAR_NAME}")
        addresses[VAR_NAME] = next_var_address
        next_var_address += 1


def META_GET_VARIABLE_ADDRESS(VAR_NAME):
    """Retrieves the numerical address / index of the variable X"""
    if "[" in VAR_NAME:
        VAR_NAME, VAR_SIZE = VAR_NAME[:-1].split("[")
        if VAR_NAME not in addresses: raise Exception(f"{VAR_NAME} has not been declared")
        return addresses[VAR_NAME] + int(VAR_SIZE)
    else:
        if VAR_NAME not in addresses: raise Exception(f"{VAR_NAME} has not been declared")
        return addresses[VAR_NAME]


# ------------------------------------------------------------------------------------------------------------
# CODE FUNCTIONS ---------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------


def COMMAND_MOV(X, Y):
    """Move contents of cell X into Y, clearing X and overwriting Y  
    Same as Y=X, X=0"""
    return  MICRO_SETVALUE(Y, 0)    +\
            HELPER_DISTRIBUTE_INTO(X, Y)

def COMMAND_ADD(X, Y, Z):
    """Add X to Y, put result into Z  
    Same as Z = (X + Y)"""
    return  HELPER_DISTRIBUTE_INTO(X, 3)    +\
            HELPER_DISTRIBUTE_INTO(Y, 4)    +\
            ALU_ADD()                       +\
            MICRO_SETVALUE(Z, 0)            +\
            HELPER_DISTRIBUTE_INTO(5, Z)

def COMMAND_SUB(X, Y, Z):
    """Subtract Y from X, put result into Z"""
    return  HELPER_DISTRIBUTE_INTO(X, 3)    +\
            HELPER_DISTRIBUTE_INTO(Y, 4)    +\
            ALU_SUB()                       +\
            MICRO_SETVALUE(Z, 0)            +\
            HELPER_DISTRIBUTE_INTO(5, Z)

def COMMAND_MUL(X, Y, Z):
    """Multiply X with Y and put result into Z"""
    return  HELPER_DISTRIBUTE_INTO(X, 3)    +\
            HELPER_DISTRIBUTE_INTO(Y, 4)    +\
            ALU_MUL()                       +\
            MICRO_SETVALUE(Z, 0)            +\
            HELPER_DISTRIBUTE_INTO(5, Z)

def COMMAND_DIV(X, Y, Z):
    """(Whole number) Divide X by Y and put result into Z"""
    pass

def COMMAND_MOD(X, Y, Z):
    """Finds X modulo Y and puts it into Z"""
    pass

def COMMAND_INP(X):
    """Take input from the console and store in X"""
    return  MICRO_INPUT(X)

def COMMAND_OUT(X):
    """Print X to the console"""
    return  MICRO_OUTPUT(X)

def COMMAND_SET(X, V):
    """Set X to value V"""
    return  MICRO_SETVALUE(X, V)

def COMMAND_CPY(X, Y):
    """Copy contents of cell X into Y, leaving X seemingly untouched and overwriting Y"""
    return  HELPER_DISTRIBUTE_INTO(X, 2, Y) +\
            COMMAND_MOV(2, X)


# ------------------------------------------------------------------------------------------------------------
# HELPING FUNCTIONS ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------


def HELPER_DISTRIBUTE_INTO(X, *args):
    """Will take X and distribute it into multiple other cells"""
    return  FORMULATE_FOR_LOOP(X, 1,
        "".join([
            MICRO_INCREMENT(pos, 1) for pos in args
            ]))


# ------------------------------------------------------------------------------------------------------------
# FORMULATING FUNCTIONS --------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------


def FORMULATE_IF_ELSE(CONDITION, INSTRUCTIONS_IF, INSTRUCTIONS_ELSE):
    """Formulates an if/else statement"""
    pass

def FORMULATE_FOR_LOOP(X, DECREMENT_AMOUNT, INSTRUCTIONS_LOOP):
    """Formulates a for-loop running over X and decrementing it DECREMENT_AMOUNT times each iteration.  
    WILL AUTOMATICALLY MOVE TO X BEFORE STARTING THE LOOP AND AT THE END OF LOOP"""
    return  MICRO_PTR_GOTO(X)       +\
            "["                     +\
            MICRO_PTR_GOTO(-X)      +\
            INSTRUCTIONS_LOOP       +\
            MICRO_PTR_GOTO(X)       +\
            "-"*DECREMENT_AMOUNT    +\
            "]"                     +\
            MICRO_PTR_GOTO(-X)


# ------------------------------------------------------------------------------------------------------------
# ALU FUNCTIONS ----------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------


def ALU_ADD():
    """Add A and B into C, consuming A and B"""
    return  HELPER_DISTRIBUTE_INTO(3, 5)    +\
            HELPER_DISTRIBUTE_INTO(4, 5)

def ALU_SUB():
    """Subtract B from A and put into C"""
    return  HELPER_DISTRIBUTE_INTO(3, 5)    +\
            FORMULATE_FOR_LOOP(4, 1, MICRO_DECREMENT(5, 1))

def ALU_MUL():
    """Multiply X and Y and put into C"""
    return  FORMULATE_FOR_LOOP(3, 1,
            "".join([
                COMMAND_CPY(4, 5)
            ]))                         +\
            MICRO_SETVALUE(4, 0)

def ALU_DIV():
    """Divide X by Y and put into C"""
    pass

def ALU_MODULO():
    """Calculates A modulo B and puts it into C"""
    pass

def ALU_CMP_A_GREATER_THAN_B():
    """Checks if A is larger than B, putting result into D"""
    pass

def ALU_CMP_A_EQUALS_B():
    """Checks if A is equal to B, putting result into D"""
    return 


# ------------------------------------------------------------------------------------------------------------
# MICRO FUNCTIONS --------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------


def MICRO_PTR_GOTO(POSITION):
    """Move pointer to position X"""
    if POSITION < 0:    return "<" * -POSITION
    else:               return ">" * POSITION

def MICRO_INCREMENT(X, N):
    """Increments the current cell by N"""
    return  MICRO_PTR_GOTO(X)   +\
            "+" * N             +\
            MICRO_PTR_GOTO(-X)

def MICRO_DECREMENT(X, N):
    """Decrements the current cell by N"""
    return  MICRO_PTR_GOTO(X)   +\
            "-" * N             +\
            MICRO_PTR_GOTO(-X)

def MICRO_SETVALUE(X, N):
    return  MICRO_PTR_GOTO(X)                       +\
            ("[-]" if N == 0 else "")               +\
            ("[-]" + "+" * N if N < 128 else "")    +\
            ("[-]" + "-" * N if N >= 128 else "")   +\
            MICRO_PTR_GOTO(-X)

def MICRO_INPUT(X):
    """Takes input from terminal and stores it in the current cell"""
    return  MICRO_PTR_GOTO(X)   +\
            ","                 +\
            MICRO_PTR_GOTO(-X)

def MICRO_OUTPUT(X):
    """Takes the current cell and outputs it to terminal"""
    return  MICRO_PTR_GOTO(X)   +\
            "."                 +\
            MICRO_PTR_GOTO(-X)