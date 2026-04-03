'''
TODO:
    - Tokenize de expression on a second pass
    
    - Add solver
'''

Operators = ["(", ")", "&", "+", "!"]
SubVars = ["1","0"]
Tokens = []
Vars = []
VarCounter = 0
expression = ""



def Passer(mode):
    global Operators; global VarCounter; global Tokens; global Vars; global expression; global SubVars
    if mode == "i":
        Depth = 0
        Before = ""
        for char in expression:
            if Before == "" and char in ["&", "+", ")"]:
                print("Wrong format: Equation starts with operator")
                return False
            #Checks
            print(Before, char)
            print(Before.isalpha(),char.isalpha())

            if char not in Operators and not char.isalpha() and char not in SubVars:
                print("That is an invalid equation.")
                return False
            elif char.isalpha() or char in SubVars :
                if Before.isalpha() or Before in SubVars:
                    print("Wrong format: Two consecutive variables")
                    return False
                elif char.upper() not in Vars and char.isalpha():
                    VarCounter +=1
                    if VarCounter <= 6:
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

            Before = char

        if Depth != 0 or Before in ["&","+","!","("]:
            print("Wrong format: incomplete expression")
            return False
        else:
            return True

Passer("i")
print(Vars)
