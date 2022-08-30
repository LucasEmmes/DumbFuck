
cell_ptr = 0
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
    return  COMMAND_SET(Y, 0)           +\
            FORMULATE_FOR_LOOP(X, 1, 
                "".join([
                    MICRO_PTR_GOTO(Y),
                    MICRO_INCREMENT(1),
                    MICRO_PTR_GOTO(X)
                ])
            )

def COMMAND_ADD(X, Y, Z):
    """Add X to Y, put result into Z  
    Same as Z = (X + Y)"""
    return

def COMMAND_SUB(X, Y, Z):
    """Subtract Y from X, put result into Z"""
    pass

def COMMAND_MUL(X, Y, Z):
    """Multiply X with Y and put result into Z"""
    pass

def COMMAND_DIV(X, Y, Z):
    """(Whole number) Divide X by Y and put result into Z"""
    pass

def COMMAND_MOD(X, Y, Z):
    """Finds X modulo Y and puts it into Z"""
    pass

def COMMAND_INP(X):
    """Take input from the console and store in X"""
    pass

def COMMAND_OUT(X):
    """Print X to the console"""
    pass

def COMMAND_SET(X, V):
    """Set X to value V"""
    return  MICRO_PTR_GOTO(X)   +\
            MICRO_SETVALUE(V)   +\
            MICRO_PTR_GOTO(0)

def COMMAND_CPY(X, Y):
    """Copy contents of cell X into Y, leaving X seemingly untouched and overwriting Y"""
    pass


# ------------------------------------------------------------------------------------------------------------
# FORMULATING FUNCTIONS --------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------


def FORMULATE_IF_ELSE(CONDITION, INSTRUCTIONS_IF, INSTRUCTIONS_ELSE):
    """Formulates an if/else statement"""
    pass

def FORMULATE_FOR_LOOP(X, DECREMENT_AMOUNT, INSTRUCTIONS_LOOP):
    """Formulates a for-loop running over X and decrementing it DECREMENT_AMOUNT times each iteration.  
    WILL AUTOMATICALLY MOVE TO X BEFORE STARTING THE LOOP AND AT THE END OF LOOP"""
    return  MICRO_PTR_GOTO(X)                   +\
            "["                                 +\
            MICRO_DECREMENT(DECREMENT_AMOUNT)   +\
            INSTRUCTIONS_LOOP                   +\
            MICRO_PTR_GOTO(X)                   +\
            "]"                                 +\
            MICRO_PTR_GOTO(0)


# ------------------------------------------------------------------------------------------------------------
# ALU FUNCTIONS ----------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------


def ALU_ADD():
    """Add A and B into C, consuming A and B"""
    return  MICRO_PTR_GOTO(3)           +\
            FORMULATE_FOR_LOOP(3, 1,
                "".join([
                    MICRO_PTR_GOTO(5),
                    MICRO_INCREMENT(1),
                    MICRO_PTR_GOTO(3),
                ])
            ) +\
            MICRO_PTR_GOTO(4)           +\
            FORMULATE_FOR_LOOP(4, 1,
                "".join([
                    MICRO_PTR_GOTO(5),
                    MICRO_INCREMENT(1),
                    MICRO_PTR_GOTO(4),
                ])
            )                           +\
            MICRO_PTR_GOTO(3)

def ALU_SUB():
    """Subtract B from A and put into C"""
    return  MICRO_PTR_GOTO(3)           +\
            FORMULATE_FOR_LOOP(3, 1,
                "".join([
                    MICRO_PTR_GOTO(5),
                    MICRO_INCREMENT(1),
                    MICRO_PTR_GOTO(3),
                ])
            ) +\
            MICRO_PTR_GOTO(4)           +\
            FORMULATE_FOR_LOOP(4, 1,
                "".join([
                    MICRO_PTR_GOTO(5),
                    MICRO_DECREMENT(1),
                    MICRO_PTR_GOTO(4),
                ])
            )                           +\
            MICRO_PTR_GOTO(3)

def ALU_MUL():
    """Multiply X and Y and put into C"""
    pass

def ALU_DIV():
    """Divide X by Y and put into C"""
    pass

def ALU_MODULO():
    """Calculates A modulo B and puts it into C"""

def ALU_CMP_A_GREATER_THAN_B():
    """Checks if A is larger than B, putting result into D"""
    pass

def ALU_CMP_A_EQUALS_B():
    """Checks if A is equal to B, putting result into D"""
    pass


# ------------------------------------------------------------------------------------------------------------
# MICRO FUNCTIONS --------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------


def MICRO_PTR_GOTO(POSITION):
    """Move pointer to position X"""
    global cell_ptr
    location_delta = POSITION - cell_ptr
    cell_ptr = POSITION
    if location_delta < 0:  return "<" * -location_delta
    else:                   return ">" * location_delta

def MICRO_INCREMENT(N):
    """Increments the current cell by N"""
    return "+" * N

def MICRO_DECREMENT(N):
    """Decrements the current cell by N"""
    return "-" * N

def MICRO_SETVALUE(N):
    if N == 0:  return "[-]"
    if N < 128: return "+" * N
    else:       return "-" * (256-N)

def MICRO_INPUT():
    """Takes input from terminal and stores it in the current cell"""
    pass

def MICRO_OUTPUT():
    """Takes the current cell and outputs it to terminal"""