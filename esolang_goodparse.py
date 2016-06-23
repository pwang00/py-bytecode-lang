import types,re,sys,hashlib
variables = []
varArray = []
valueArray = []
varCount = 0
bytecode = []
consts = [0]
values = [] 
type_array = []
unary_operators = ['print','input','int','bytes','str','bool']
literals = "1234567890()!@#$%^&*|/<>{}[]|\:;'\\"
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
    i = 0
    prev_op = ""
    prev_const = None
    prev_var = None
    while len(program) > 0:
        parse_line(program.pop(i))
        
    bytecode.append(100);bytecode.append(0);
    bytecode.append(0);bytecode.append(83)
    print(consts)
    print(bytecode)
    print(type_array)
def parse_line(line):
    i = 0
    names = []
    while len(line) > 0:
        print(line)
        if line[i] in reserved_namespace:
            prev_op = line[i]
            names.append(line[i])
            if prev_op == "print":
                #TODO
                bytecode.append(116)
                bytecode.append(0)
                bytecode.append(0)
                line.pop(i)
            elif prev_op == "details" or prev_op == "info":
                #TODO
                print()
                line.pop(i)
            elif prev_op == "var":
                #TODO
                varArray.append(line[i+1])
                bytecode.append(100)
                bytecode.append(len(consts))
                bytecode.append(0)
                bytecode.append(125)
                bytecode.append(varArray.index(line[i+1]))
                bytecode.append(0)
                line.pop(i)
            elif prev_op == "input":
                #TODO
                print()
                bytecode.append(116)
                bytecode.append(1)
                bytecode.append(0)
                line.pop(i)
            
        elif line[i] in variables:
            #TODO
            print("True var")
            prev_var = line[i]
            varArray.append(prev_var)
            print()
            line.pop(i)
        elif not any([i not in literals for i in line[i]]) or line[i] not in varArray and prev_op not in reserved_namespace:
            print("True lit")
            prev_const = line[i]
            if "'" in line[i] or '"' in line[i]:
                prev_const = line[i].replace("'","").replace('"','')
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
            line.pop(i)
        else:
            line.pop(i)
    print("names",names)
    print("consts",consts)
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

