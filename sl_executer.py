from sl_compiler import file_check

def executer_userrequest():
    print("Wellcome to the SL-Executer, in this software you can start your sl scripts")
    def menu():
        print("""
        1. start # to start a script
        2. help # to show this menu
        3. exit # to exit the program
        """)
    maincount = 1
    while (maincount == 1):
        userinput = input("Enter your command: ")
        if userinput == "start":
            start()
        elif userinput == "help":
            menu()
        elif userinput == "exit":
            maincount = 0
        else:
            print("Command not found")
            menu()


def start():
    sl_script_input = input("Enter your scriptname: ")
    file_check(sl_script_input)

executer_userrequest()