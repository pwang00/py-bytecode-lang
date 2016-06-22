import types,re,sys,hashlib
variables = []
varArray = []
valueArray = []
varCount = 0
bytecode = []
consts = [0]
values = []
unary_operators = ['print','input','int','bytes','str','bool']
literals = "1234567890()!@#$%^&*|/<>{}[]|\:;'\"\\"
dictValues = []
version = "1.0.1"
operators = ["+","-","/","*","^^","%","&","^","|","~",">","-","=","=="]
reserved_namespace = ['print','input','int','bytes','str','var','bool','details','info'] #TODO: expand functionality of reserved namespace

program = """
print 1;
input 1;"""
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
    #code = [line for line in code if line]
    convertToByteCode(split(code))
    return 0

def split(program):
    for i in range(len(program)):
        if '"' in program[i] and any([j in program[i] for j in unary_operators]) or "'" in program[i] and any([j in program[i] for j in unary_operators]):
            program[i] = program[i].split(" ",1)
        else:
            program[i] = program[i].split(" ",3)
    
    print(program)
    return program

def convertToByteCode(program):
    i,j = 0,0
    prev_op = ""
    prev_const = None
    prev_var = None
    while len(program) > 0:

        if program[i][j] in reserved_namespace:
            if prev_op == "print":
                #TODO
            elif prev_op == "details" or program[i][j] == "info":
                #TODO
            elif prev_op == "var":
                #TODO
            elif prev_op == "input":
                #TODO
        elif program[i][j] in variables:
            #TODO
        elif program[i][j] in literals:
            #TODO
        print(program,prev_op)
        program.pop(i)
    print(program,prev_op)
    bytecode.append(100);bytecode.append(0);
    bytecode.append(0);bytecode.append(83)

def parse_line():
    
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
scan(program)
"""
while True:
    try:
        compile_and_run()
    except KeyboardInterrupt:
        continue
"""
"""
func=types.FunctionType(types.CodeType(0,0,len(varArray),0,0,bytes(bytecode),tuple(consts),tuple(reserved_namespace),tuple(variables),'','',0,bytes()),globals())
func()
"""

