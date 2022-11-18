# SigCal
SigCal is a simple summation calculator.
# User Guide
When SigCal is launched, it ask for two float inputs: `Bottom var`[iable] & `Top var`[iable].
Bottom Variable is equal to `x`, and Top variable is equal to `y`. See `fig 1`.
`i[0]` is the function which will be operated on `x`. See `fig 1`.

![202580653-512523ef-da6f-436b-aa4b-80cc6e54ce30](https://user-images.githubusercontent.com/60891047/202605227-0b869a16-5195-402c-bc68-24dd423a6660.png)
`fig 1`

# Changing `i[]`
`i[0]` is hard coded into the program. You can change it by using an text editor or IDE (some good ones are pycharm and nano).
Open `SigCal.py` and look inside the `sigma()` function. There you will find the list `i[]`.
`i[0]` does the physical calculation on `x`. `i[1]` is a string that is returned when the `func` command is used.
Since `i[]` is edited a lot, I recomend using an in-terminal editor like nano or Vim.

# SigCal Commands
SigCal includes some built in commands. The command input feild (`> `) will show after the first calculation is preformed.

The commands are:
   
   - `help`: Shows the HELP MENU
   
   - `debug`: Shows a detailed answer of the calculation preformed. (eg. 1 + 2 + 4 + 6 = 13)
   
   - `func`: Shows the function that 'Bottom Var' is being operated on (in f(x) formating) and gives and example.
   
   - `reset`: Resets the program.
   
   - `clear`: Clears the screen. Works on all OSs. (Windows, MAC, Linux)
   
   - `exit`: Exits the program.
# Thank You!
Thank you for using SigCal! If you have any question/comments please feel free to email me at: itsjoeygofficial@outlook.com
