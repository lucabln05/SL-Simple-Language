def file_check(x):
    print(x)
    file_check.filename = x
    try:
        filename, file_extension = x.split(".")
    except:
        print("Error: Please use a valid file extension, dont use a dot in the filename (e.g. 'test.sl' not 'test.sl.)")

    if file_extension == "sl":
        print("File extension is valid") 
        open_sl_script()
    else:
        print('Error: Extension is not valid, please use ".sl"')


def open_sl_script():
    file = open(file_check.filename, "r")
    open_sl_script.file_content = file.read()
    sl_script_content_split()


def sl_script_content_split():
    # for loop to split eatch line
    try:
        for line in open_sl_script.file_content.splitlines():
            # split the line in 2 parts, the command and the content
            sl_script_content_split.command = line.split(" ", 1)[0]
            sl_script_content_split.content = line.split(" ", 1)[1]
            compiler()
    except:
        print("!Script END!")



def compiler():

    compiler.content = sl_script_content_split.content

    try:
        getattr(commands, sl_script_content_split.command)(compiler.content)
    except:
        print(f"Error: Command ({sl_script_content_split.command})not found")
    




class commands():

    def print(content):
        # get fist letter from the content
        compiler.content_variable_check = content[0]
        # check if the first letter is a $, if yes, print the variable
        if compiler.content_variable_check == "$":
            # remove the first letter from the content
            content = content[1:]
            # print the variable
            print(getattr(compiler, content))
        else:
            print(content)

    def input(content):
        # get fist letter from the content
        compiler.content_variable_check = content[0]
        # check if the first letter is a $, if yes, print the variable
        if compiler.content_variable_check == "$":
            content = content[1:]
            input(getattr(compiler, content))
        else:
            input(content)

    def set(content):
        compiler.variablename = content.split(" ", 1)[0]
        # split the the value from the rest set <variable> to <value> 
        compiler.variablevalue = content.split(" ", 2)[2]

        # check if value is another variable
        compiler.variablevalue_variable_check = compiler.variablevalue[0]
        if compiler.variablevalue_variable_check == "$":
            compiler.variablevalue = compiler.variablevalue[1:]
            compiler.variablevalue = getattr(compiler, compiler.variablevalue)    
        # set the variable to the value
        setattr(compiler, compiler.variablename, compiler.variablevalue)

    def get(content):
        compiler.variablename = content.split(" ", 1)[0]
        print(getattr(compiler, compiler.variablename))

    def calc(content):
        # check if value are variables format is calc <value> <operator> <value>
        compiler.value1 = content.split(" ", 1)[0]
        compiler.operator = content.split(" ", 2)[1]
        compiler.value2 = content.split(" ", 3)[2]

        # check if value1 is a variable
        compiler.value1_variable_check = compiler.value1[0]
        if compiler.value1_variable_check == "$":
            compiler.value1 = compiler.value1[1:]
            compiler.value1 = getattr(compiler, compiler.value1)

        # check if value2 is a variable
        compiler.value2_variable_check = compiler.value2[0]
        if compiler.value2_variable_check == "$":
            compiler.value2 = compiler.value2[1:]
            compiler.value2 = getattr(compiler, compiler.value2)

        # check if operator is valid
        if compiler.operator == "+":
            print(int(compiler.value1) + int(compiler.value2))
        elif compiler.operator == "-":
            print(int(compiler.value1) - int(compiler.value2))
        elif compiler.operator == "*":
            print(int(compiler.value1) * int(compiler.value2))
        elif compiler.operator == "/":
            print(int(compiler.value1) / int(compiler.value2))
        else:
            print("Error: Operator not valid")

    def when(content):
        # check if value are variables format is if <value> <operator> <value> then <command>
        compiler.value1 = content.split(" ", 1)[0]
        compiler.operator = content.split(" ", 2)[1]
        compiler.value2 = content.split(" ", 3)[2]
        compiler.command = content.split(" ", 5)[4]
        compiler.content = content.split(" ", 5)[5]

        # check if value1 is a variable
        compiler.value1_variable_check = compiler.value1[0]
        if compiler.value1_variable_check == "$":
            compiler.value1 = compiler.value1[1:]
            compiler.value1 = getattr(compiler, compiler.value1)

        # check if value2 is a variable
        compiler.value2_variable_check = compiler.value2[0]
        if compiler.value2_variable_check == "$":
            compiler.value2 = compiler.value2[1:]
            compiler.value2 = getattr(compiler, compiler.value2)

        # check if operator is valid
        if compiler.operator == "==":
            if compiler.value1 == compiler.value2:
                getattr(commands, compiler.command)(compiler.content)
        elif compiler.operator == "!=":
            if compiler.value1 != compiler.value2:
                getattr(commands, compiler.command)()
        elif compiler.operator == ">":
            if compiler.value1 > compiler.value2:
                getattr(commands, compiler.command)()
        elif compiler.operator == "<":
            if compiler.value1 < compiler.value2:
                getattr(commands, compiler.command)()
        else:
            print("Error: Operator not valid")
        