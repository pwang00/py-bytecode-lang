import types,re,sys,hashlib
variables = []
varArray = []
valueArray = []
varCount = 0
bytecode = []
consts = [0]
values = [] 
type_array = []
prev_op = ""
prev_const = None
prev_var = None
unary_operators = ['print','input','int','bytes','str','bool']
literals = "1234567890()!@#$%^&*|/<>{}[]|\:;'"
dict_values = []
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
    code = [line for line in code if line]
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
    while len(program) > 0:
        parse_line(program.pop(0))
        
    bytecode.append(100);bytecode.append(0);
    bytecode.append(0);bytecode.append(83)
def solve_arithmetic():
    pass

def parse_line(line):
    i = 0
    names = []
    cache = " ".join(line)

    global prev_const
    global prev_op
    global prev_var
    while len(line) > 0:
        if line[i] in reserved_namespace:
            prev_op = line[i]
            names.append(line[i])
            if prev_op == "print":
                #TODO
                bytecode.append(116)
                bytecode.append(0)
                bytecode.append(0)
                consts.append(line[i+1])
                line.pop(i)
            elif prev_op == "details" or prev_op == "info":
                #TODO
                line.pop(i)
            elif prev_op == "var":
                #TODO
                bytecode.append(100)
                bytecode.append(len(consts))
                bytecode.append(0)
                line.pop(i)
            elif prev_op == "input":
                #TODO
                bytecode.append(116)
                bytecode.append(1)
                bytecode.append(0)
                line.pop(i)
            
        elif line[i] in varArray and line[i] == line[-1]:
            #TODO
            prev_var = line.pop(i)
            bytecode.append(124) #load fast
            bytecode.append(varArray.index(prev_var))
            bytecode.append(0)
            bytecode.append(131)
            bytecode.append(1)
            bytecode.append(0)
            bytecode.append(1)
            
        elif prev_op == "var" and any([i not in literals for i in line[i]]) and line[-1] != line[i] and line[i] not in operators and line[i] not in reserved_namespace:
            #TODO
            prev_var = line.pop(i)
            varArray.append(prev_var)
            bytecode.append(125)
            bytecode.append(varArray.index(prev_var))
            bytecode.append(0)
        elif prev_op != "var" and (not all([i not in literals for i in line[i]])):
            prev_const = line.pop(i)
            if "'" in prev_const or '"' in prev_const:
                prev_const = prev_const.replace("'","").replace('"','')
                type_array.append(str)
            consts.append(prev_const)
            bytecode.append(100)
            bytecode.append(consts.index(prev_const))
            bytecode.append(0)
            bytecode.append(131)
            bytecode.append(1)
            bytecode.append(0)
            bytecode.append(1)
            type_array.append(int)
        elif (not any([i not in literals for i in line[i]]) and prev_op == "var") and all([i not in operators for i in line[i]]):
            prev_const = line.pop(i)
            #print("prev_const:",prev_const)
            consts.append(prev_const)
        elif any([i in operators for i in line[i]]) and prev_op == "var" and line[i] != "=":
            prev_const = eval(line.pop(i),{"__builtins__":None},operators)
            consts.append(prev_const)
        elif line[-1][-1] in operators:
            print(cache)
            print(" "*(len(cache)-1)+"^")
            print("Syntax Error: Operator without two operands")
            break
        elif line[i] not in operators and line[i] not in variables and line[i] not in reserved_namespace:
            print("Name Error: Name '"+line[i]+"' is not defined.")
            break     
        else:
            line.pop(i)
def compile_and_run():
    global bytecode;
    global program;
    program = input(">>> ")
    if scan(program) != 1:
        contains = dict(zip(variables,dict_values))
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
#scan(program)
while True:
    try:
        compile_and_run()
    except KeyboardInterrupt:
        continue
"""
func=types.FunctionType(types.CodeType(0,0,len(varArray),0,0,bytes(bytecode),tuple(consts),tuple(reserved_namespace),tuple(variables),'','',0,bytes()),globals())
func()
"""
