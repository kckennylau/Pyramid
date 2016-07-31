import sys
from colorama import init, Fore

init()

# Variables.
pointer = ""
modes = {"":0, "o":1, "a":2, "p":3}
mode = -1
output = ""
start = True
buffer = [0,""]

inputs = []
inputscheck = 0

errors = [x for x in open("errors.txt", "r").read().split("\n")]

# Initialise code.
codestart = open("file.sl", "r").read().split("\n")
code = [x for x in ("/" + "/".join(codestart) + "/").split("-")]


# Declares errors.
def call_error(errorno, stack, line):
    stackcheck = bool(stack != "none")
    linecheck = bool(line != "none")
    print(Fore.RED + "ERROR#" + errorno + ": " + errors[errorno] + " (Code found in " * bool(stackcheck or linecheck) +
          ("stack " + str(stack + 1)) * stackcheck + ("line " + str(line + 1) + ")") * linecheck + ")" * stackcheck)
    sys.exit()

for a in range(len(code)):
    code[a] = code[a].split("/")
    if code[a] == []:
        call_error(1, "none", "none")


# Executes code on the pointer of the current stack.
def exec_code(stack, line):
    global pointer,modes,mode,output,buffer,start
    runcode = code[stack][line]
    try:
        pointer = runcode[len(runcode) - 1]
    except IndexError:
        if stack + 1 == len(code):
            buffer[0] = (buffer[0]<<1) | int(pointer)
            buffer[1] += pointer
            if mode == modes["a"]:
                output += chr(buffer[0])
            else:
                output += buffer[1]
            print("Output: " + output)
            sys.exit()
        else:
            if mode == modes[""]:
                if not start:
                    output += buffer[1]
                buffer = [int(pointer),pointer]
            elif mode == modes["a"]:
                buffer[0] = (buffer[0]<<1) | int(pointer)
                buffer[1] += pointer
                output += chr(buffer[0])
                buffer = [0,""]
            else:
                buffer[0] = (buffer[0]<<1) | int(pointer)
                buffer[1] += pointer
            start = False
            find_chars(stack + 1)
        start = False
    if pointer in ["0", "1"]:
        code[stack][line] = runcode[:len(runcode) - 1]
        exec_code(stack, line - ((2 * int(pointer)) - 1))
    elif pointer == "?":
        prompt = raw_input(">>>")
        if prompt not in ["0", "1"]:
            call_error(2, "none", "none")
        else:
            inputs.append(prompt)
            code[stack][line] = runcode[:len(runcode) - 1] + prompt
            exec_code(stack, line)
    elif pointer == "i":
        try:
            code[stack][line] = runcode[:len(runcode) - 1] + inputs[inputscheck]
        except IndexError:
            prompt = raw_input(">>>")
            if prompt not in ["0", "1"]:
                call_error(2, "none", "none")
            else:
                inputs.append(prompt)
                code[stack][line] = runcode[:len(runcode) - 1] + prompt
        inputscheck += 1
        exec_code(stack, line)
    else:
        call_error(0, stack, line)


# Finds "<" symbol, and initiates code there.
def find_marker(stack):
    markercount = 0
    realstart = 0
    for start in range(1, len(code[stack]) - 1):
        tempstart = code[stack][start]
        if tempstart[len(tempstart) - 1] == "<":
            code[stack][start] = tempstart[:len(tempstart) - 1]
            markercount += 1
            realstart = start
    if markercount > 1:
        call_error(3, stack, realstart)
    exec_code(stack, realstart)


# Finds "o" and "a" symbols, and does things accordingly.
def find_chars(stack):
    global pointer,modes,mode,output,buffer
    if "r" in code[stack][1]:
        inputs = []
        inputscheck = 0
        code[stack][1] = code[stack][1].replace("r","")
    number = code[stack][1].count("p")
    for _ in range(number):
        buffer[0] = (buffer[0]<<1) | (buffer[0]&1)
        buffer[1] += buffer[1][-1]
    code[stack][1] = code[stack][1].replace("p","")
    try:
        mode = modes[code[stack][1]]
        code[stack] = [code[stack][0]] + code[stack][2:]
    except KeyError:
        mode = modes[""]
    find_marker(stack)

find_chars(0)
