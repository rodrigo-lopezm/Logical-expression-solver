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
expression = ""

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
    i=0
    while i < len(Tokens)-1:
        if Tokens[i] == "!" and Tokens[i+1] == "!":
            del Tokens[i:i+2]
        else:
            i+=1

def SetValues(Tokens,Values):
    Substituted = []
    for token in Tokens:
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
        return SolveExpression(Tokens)
    
    i=0
    while i < len(Tokens)-1:
        if Tokens[i] == "!" and Tokens[i+1]=="0":
            Tokens[i:i+2] = ["1"]
        elif Tokens[i] == "!" and Tokens[i+1] == "1":
            Tokens[i:i+2] = ["0"]
        else:
            i+=1

    i=1
    while i<len(Tokens)-1:
        if Tokens[i] == "&":
            if Tokens[i-1] == "1" and Tokens[i+1] == "1":
                Tokens[i-1:i+2]=["1"]
            else:
                Tokens[i-1:i+2]=["0"]
        else:
            i+=1

    i=1
    while i<len(Tokens)-1:
        if Tokens[i] == "+":
            if Tokens[i-1] == "0" and Tokens[i+1] == "0":
                Tokens[i-1:i+2]=["0"]
            else:
                Tokens[i-1:i+2]=["1"]
        else:
            i+=1

    return Tokens

def StartTable():
    global Tokens; global Vars
    print(" | ".join(Vars) + " | RESULT")
    print("-" * (len(Vars) * 4 + 8))
    NumRows = 2 ** len(Vars)
    for i in range(NumRows):
        #Generates the corresponding binary values for each row and stores them in a dictionary
        RowVals = f"{i:0{len(Vars)}b}"
        CurrentVals = dict(zip(Vars, RowVals))
        CurrentTokens = SetValues(Tokens, CurrentVals)
        SolvedExpression = SolveExpression(CurrentTokens.copy()) # type: ignore
        Variables = " | ".join(CurrentVals.values())
        print(f"{Variables} |   {SolvedExpression[0]}")

print("Welcome to the simple boolean truth table evaluator, please enter a boolean expression following the set syntax.\n\n")   
while True:
    expression = input("Please enter an expression: ")
    if Passer():
        Simplifyer()
        StartTable()
        Tokens = []
        expression = ""
        Vars = []
        print("\n")
        print("Evaluate another expression? (Y/N)")
        while True:
            choice = input().upper().strip()
            if choice not in ["Y", "N"]:
                print("Invalid choice, enter again. \n")
            elif choice == "N":
                exit()
            else:
                print("\n\n")
                break