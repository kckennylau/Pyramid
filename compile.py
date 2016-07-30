import sys
from colorama import init, Fore

init()

# Variables.
pointer = ""
outputcheck = False
asciicheck = False
output = []
finaloutput = []
errors = [x for x in open("errors.txt", "r").read().split("\n")]

# Initialise code.
codestart = open("file.pmd", "r").read().split("\n")
code = [x for x in ("/" + "/".join(codestart) + "/").split("-")]

for a in range(len(code)):
    code[a] = code[a].split("/")

# Declares errors.
def call_error(errorno, stack, line):
    stackcheck = bool(stack != "none")
    linecheck = bool(line != "none")
    print(Fore.RED + "ERROR#" + errorno + ": " + errors[errorno] + " (Code found in " * bool(stackcheck or linecheck) +
          ("stack " + str(stack + 1)) * stackcheck + ("line " + str(line + 1) + ")") * linecheck + ")" * stackcheck)
    sys.exit()

def exec_code(stack, line):
    runcode = code[stack][line]
    try:
        pointer = runcode[len(runcode) - 1]
    except IndexError:
        global pointer, output, outputcheck, opstartcheck, asciicheck
        if stack + 1 == len(code):
            if outputcheck is True:
                output.append(pointer)
                finaloutput.append("".join(output))
            else:
                finaloutput.append(pointer)
            if asciicheck is True:
                finaloutput[len(finaloutput) - 1] = chr(int(finaloutput[len(finaloutput) - 1], 2))
            print("Output: " + "".join(finaloutput))
            sys.exit()
        else:
            if outputcheck is True:
                output.append(pointer)
                outputcheck = False
            else:
                print(code[stack + 1])
                if ["o"] in code[stack + 1]:
                    finaloutput.append("".join(output))
                output = [pointer]
            if asciicheck is True:
                finaloutput.append("".join(output))
                output = [pointer]
                finaloutput[len(finaloutput) - 1] = chr(int(finaloutput[len(finaloutput) - 1], 2))
                asciicheck = False
            find_chars(stack + 1)
    if pointer in ["0", "1"]:
        code[stack][line] = runcode[:len(runcode) - 1]
        exec_code(stack, line - ((2 * int(pointer)) - 1))
    elif pointer == "?":
        prompt = raw_input(">>>")
        if prompt not in ["0", "1"]:
            call_error(2, "none", "none")
        else:
            code[stack][line] = runcode[:len(runcode) - 1] + prompt
            exec_code(stack, line)


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
    global outputcheck, opstartcheck, asciicheck
    for chars in range(1, len(code[stack]) - 1):
        if "o" == code[stack][chars]:
            outputcheck = True
            code[stack] = [code[stack][0]] + code[stack][2:]
        elif "a" == code[stack][chars]:
            outputcheck = True
            asciicheck = True
            code[stack] = [code[stack][0]] + code[stack][2:]
    find_marker(stack)

find_chars(0)