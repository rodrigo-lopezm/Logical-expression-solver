'''
TODO:
    - Tokenize the expression on the first pass
    - Simplify the expressions
    - Add solver
    - Output table FORMATTED
'''

Operators = ["(", ")", "&", "+", "!"]
SubVars = ["1","0"]
Tokens = []
Vars = []
expression = "a & b + !!C + D"


def Passer():
    global Operators; global Tokens; global Vars; global expression; global SubVars
    #Mode i is the same as "initial pass"
    Tokens = []
    Depth = 0
    Before = ""
    for char in expression:
        #Checks for equation validity
        if char == " ":
            continue
        if Before == "" and char in ["&", "+", ")"]:
            print("Wrong format: Equation starts with operator")
            return False
        if char not in Operators and not char.isalpha() and char not in SubVars:
            print("That is an invalid equation.")
            return False
        elif char.isalpha() or char in SubVars :
            if Before.isalpha() or Before in SubVars:
                print("Wrong format: Two consecutive variables")
                return False
            elif char.upper() not in Vars and char.isalpha():
                if len(Vars) <= 6:
                    Vars.append(char.upper())
                else:
                    print("There is a limit of 6 boolean variables.")
                    return False
        else:
            if char == "(":
                if Before.isalpha() or Before in SubVars:
                    print("Wrong format")
                    return False
                else:
                    Depth+=1
            elif char == ")":
                if Before in ["&", "+"]:
                    print("Wrong format")
                    return False
                else:
                    Depth -= 1
            elif char == "!":
                if Before.isalpha() or Before in SubVars:
                    print("Wrong format")
                    return False
            else:
                if Before in ["&","+","!","("]:
                    print("Worng format")
                    return False

        Tokens.append(char.upper())
        Before = char

    if Depth != 0 or Before in ["&","+","!","("]:
        print("Wrong format: incomplete expression")
        return False
    else:
        return True

def Simplifyer():
    global Tokens
    while i < len(Tokens):
        

def SetValues(Tokens,Values):
    Substituted = []
    for token in Tokens:
        print(Values.get(token, token))
        Substituted.append(Values.get(token, token))
        return Substituted

def SolveExpression(Tokens):
    if len(Tokens) == 1:
        return Tokens
    #Parentheses solver
    LastOpen = -1; Closed = -1
    for i in range(len(Tokens)):
        if Tokens[i] == "(":
            LastOpen = i
        elif Tokens[i]==")":
            Closed = i
            break
    
    if LastOpen != -1 and Closed != -1:
        SubExpression = Tokens[LastOpen+1:Closed]
        Tokens[LastOpen:Closed+1] = SolveExpression(SubExpression)

    #Negation solver



def StartTable():
    global Tokens; global Vars
    NumRows = 2 ** len(Vars)
    for i in range(NumRows):
        #Generates the corresponding binary values for each row and stores them in a dictionary
        RowVals = f"{i:0{len(Vars)}b}"
        CurrentVals = dict(zip(Vars, RowVals))
        CurrentTokens = SetValues(Tokens, CurrentVals)
        

Passer()
print(Vars)
print(Tokens)
StartTable()