import os
program = True
shutdown = None
while program:
    print('Simple Sigma Calculator. Remember: You must HARD CODE the function before running')
    bot = int(input('Bottom var: '))
    top = int(input('Top var: '))
    b = bot
    t = top
    i = 0
    command = True

    # Sigma Function. Does the Heavy Lifting 
    def sigma(num, printout):
        i = [num * 5 / 2, 'x * 5 / 2']
        if not printout:
            return i[0]
        elif printout:
            print(f'F(x) = {i[1]}')
            print(f'F({num}) = {i[0]}')

    # Clear Function. Acts as a cls command in the custom terminal.
    def clear():
        from sys import platform
        if platform == 'win32':
            os.system('cls')
        elif platform == 'darwin':
            os.system('clear')
        elif platform == 'linux' or platform == 'linux2':
            os.system('clear')

    # first run
    while b <= t:
        h = sigma(b, False)
        i += h
        b += 1
    print(i)

    # Command System
    while command:
        check = input("> ").upper()
        if check == 'DEBUG':
            i = 0
            x = bot
            y = top
            while x <= y:
                h = sigma(x, False)
                print(f'+ {h}')
                i += h
                x += 1
            print(f'= {i}')
        elif check == 'EXIT':
            print('shutting down...')
            shutdown = True
            command = False
        elif check == 'HELP':
            print(f'*' * 10 + ' HELP MENU ' + '*' * 10)
            print('| - help - | Shows this menu \n| - debug - | Shows detailed answer \n| - func - | Shows what function is being '
                  'operated and shows an example of the function \n| - reset -  | Resets the program \n| - clear - | Clears the screen \n| - exit - | Exits the program'
                  '\nTo change the funtion that is being operated, go to the sigma function in SigCal.py and change the values for i[].')
        elif check == 'RESET':
            print('resetting...')
            clear()
            command = False
        elif check == 'CLEAR':
            clear()
        elif check == 'FUNC':
            sigma(1, True)
        else:
            print('Did not recognize command.')
    
    # Program Shutdown call.
    if shutdown:
        program = False
