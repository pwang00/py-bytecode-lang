import types,re,sys,hashlib
variables = []
varArray = []
valueArray = []
varCount = 0
bytecode = []
consts = [0]
values = []
unary_operators = ['print','input','int','bytes','str','bool']
literals = "1234567890!@#$%^&*(){}\|"
dictValues = []
version = "1.0.1"
operators = ["+","-","/","*","^^","%","&","^","|","~",">","-","=","=="]
reserved_namespace = ['print','input','int','bytes','str','var','bool','details','info'] #TODO: expand functionality of reserved namespace

def scan(code):
    statements = []
    lines = code.count("\n")-1
    for i in program.split(";"):
        statements.append(i.replace("\n",""))
    return parse_code(statements)

def parse_code(script):
    #script = map(lambda script: script.replace('var', ), script)
    code = program.split("\n")
    error = 0
    [code.pop(code.index("")) if "" in code else i for i in code]
    for i in range(0,len(code)):#Iterate through the program to check for syntax errors.
        try:
            if '$' in code[i].split(" ")[0]:
                pass
            elif ";" not in code[i][-1:]:
                print("Syntax Error: Line "+str(i+1)+", missing line termination character ';'")
                print(code[i])
                print(" "*(len(code[i]))+"^")
                return 1
            elif code[i].split(" ")[0] in reserved_namespace and code[i].split(" ")[1].replace(";","") in reserved_namespace:
                print("Syntax Error: Invalid Syntax")
                print(code[i])
                print(" "*code[i].index(" ")+"^")
                return 1
        except:
            print("Syntax Error detected in program.")
            return 1
    code = "".join(code).split(";")
    convertToByteCode(split(code))
    return 0

def split(program):
    for i in range(len(program)):
        if '"' in program[i] and any([j in program[i] for j in unary_operators]) or "'" in program[i] and any([j in program[i] for j in unary_operators]):
            program[i] = program[i].split(" ",1)
        else:
            program[i] = program[i].split(" ",3)
    return program

def convertToByteCode(program):

    for i in range(len(program)):
        for j in range(len(program[i])):
            if program[i][j] in reserved_namespace:
                if program[i][j] == "print":
                    
                    if "'" in program[i][j+1] or '"' in program[i][j+1]:
                        program[i][j+1] = program[i][j+1].replace("\"","").replace('\'','')
                        consts.append(program[i][j+1])
                    else:
                        consts.append(program[i][j+1])
                    bytecode.append(116)
                    bytecode.append(0)
                    bytecode.append(0)


                    if any([i not in literals for i in program[i]]) and program[i][j+1] in varArray:

                        bytecode.append(124) #load fast
                        bytecode.append(varArray.index(program[i][j+1]))
                        bytecode.append(0)
                    else:
                        bytecode.append(100)
                        bytecode.append(len(consts)-1)
                        bytecode.append(0)
                    bytecode.append(131) #call function
                    bytecode.append(1)
                    bytecode.append(0)
                    bytecode.append(1) #pop
                elif program[i][j] == "details" or program[i][j] == "info":
                    consts.append("\nEsolang was created by Philip Wang (me), a 10th grader at Poolesville High School's Science, Math, and Computer Science program.\n")
                    bytecode.append(116)
                    bytecode.append(0)
                    bytecode.append(0)
                    bytecode.append(100)
                    bytecode.append(len(consts)-1)
                    bytecode.append(0)
                    bytecode.append(131) #call function
                    bytecode.append(1)
                    bytecode.append(0)
                    bytecode.append(1) #pop
                elif program[i][j] == "var":
                    bytecode.append(100)
                    bytecode.append(len(consts))
                    bytecode.append(0)
                    if program[i][j+1] not in literals:
                        if "'" in program[i][j+3]:
                            program[i][j+3] = program[i][j+3].replace("'","")
                        elif '"' in program[i][j+3]:
                            program[i][j+3] = program[i][j+3].replace('"',"")
                        else:
                            if program[i][j+3] not in varArray and any([i not in literals for i in program[i][j+3]]):
                                print("Variable Error: Variable '"+program[i][j+3]+"' is not defined.")
                                sys.exit(0)
                        varArray.append(program[i][j+1])
                        consts.append(program[i][j+3])
                        bytecode.append(125)
                        bytecode.append(varArray.index(program[i][j+1]))
                        bytecode.append(0)
                    else:
                        print("\nAssign Error: Can't assign to literals.")
                        sys.exit(0)
                elif program[i][j] == "input":

                    if len(program[i]) != 1:
                        consts.append(program[i][j+1].replace("\"","").replace('\'',''))
                        bytecode.append(116)
                        bytecode.append(1)
                        bytecode.append(0)
                        bytecode.append(100)
                        bytecode.append(consts.index(program[i][j+1].replace("\"","").replace('\'','')))
                        bytecode.append(0)

                        bytecode.append(131)
                        bytecode.append(1)
                        bytecode.append(0)
                        bytecode.append(1)
                    else:
                        bytecode.append(116)
                        bytecode.append(1)
                        bytecode.append(0)
                        bytecode.append(100)
                        bytecode.append(0)
                        bytecode.append(0)
                        bytecode.append(131)
                        bytecode.append(0)
                        bytecode.append(0)
                        bytecode.append(1)
            else:
                pass
    bytecode.append(100);bytecode.append(0);
    bytecode.append(0);bytecode.append(83)

def compile_and_run():
    global bytecode;
    global program;
    program = input(">>> ")
    if scan(program) != 1:
        contains = dict(zip(variables,dictValues))
        func=types.FunctionType(types.CodeType(0,0,len(varArray),0,0,bytes(bytecode),tuple(consts),tuple(reserved_namespace),tuple(variables),'','',0,bytes()),globals())

        func()


        if 116 in bytecode:
            bytecode = bytecode[:bytecode.index(116)]
        else:
            bytecode = bytecode[:-4]

print("Esolang "+version+" interpreter, build hash: "+hashlib.md5(bytes(version,"utf-8")).hexdigest()[:12]+ ", running on "+"".join(sys.platform))
print("Type \"info;\" or \"details;\" for more information.")
if "idlelib" in sys.modules:
    print(">>> -------------------------------- BEGIN ----------------------------------\n>>>")
    
while True:
    compile_and_run()
"""
func=types.FunctionType(types.CodeType(0,0,len(varArray),0,0,bytes(bytecode),tuple(consts),tuple(reserved_namespace),tuple(variables),'','',0,bytes()),globals())
func()
"""
