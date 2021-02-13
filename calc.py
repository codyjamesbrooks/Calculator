import tkinter as tk

calculator = tk.Tk()
calc_screen = tk.Entry(calculator, width=24, borderwidth=3)
calc_screen.grid(row=0, columnspan=4)

# Button Functions
def int_or_float():
	current_number = calc_screen.get()
	if current_number == '':
		return ""
	elif float(current_number) % 1 == 0:
		return int(current_number.replace('.', ''))
	else: 
		return float(current_number)

def button_click(num):
	# Adds a clicked number on to the screen. If button click is a "." 
	# and calc_screen already has '.' do nothing.
	if num != '.':
		calc_screen.insert('end', num)		
	elif calc_screen.get().count('.') < 1:
		calc_screen.insert('end', '.')		

def swap_sign():
	# used to negate the on screen number
	current_number = int_or_float()
	calc_screen.delete(0, 'end')
	calc_screen.insert(0, str(current_number * -1))

def reciprocal_fun():
	# calculates the reciprocal of the on screen number
	current_number = int_or_float()
	calc_screen.delete(0, 'end')
	calc_screen.insert(0, str(1 / current_number))

def percent_function():
	# outputs decimal version of "percentage" on scren
	current_number = int_or_float()
	calc_screen.delete(0, 'end')
	calc_screen.insert(0, str(current_number/100))

def square_number():
	# outputs the on screen number squared
	current_number = int_or_float()
	calc_screen.delete(0, 'end')
	calc_screen.insert(0, str(current_number ** 2))

def clear_entry():
	# Clears the current entry from the screen
	calc_screen.delete(0, 'end')

def clear_globals():
	# Erase any global variables
	try: 	
		del first_number
		del sign
		calc_screen.delete(0, 'end')
	except UnboundLocalError:
		calc_screen.delete(0, 'end')

def square_root_num():
	# Takes the square root of current number on screen
	current_number = int_or_float()
	calc_screen.delete(0, 'end')
	if current_number >= 0:
		calc_screen.insert(0, current_number ** .5)
	else:
		calc_screen.insert(0, 'Invalid Input')

def backspace_function():
	# Deletes the last entered character
	current_number = int_or_float()
	calc_screen.delete(0, 'end')
	calc_screen.insert(0, str(current_number)[0:-1])

def equals_function():
	# performs the desired calculation using the stored first entered number
	# the stored operation that was clicked, and the second entered number. 
	# Outputs calculation on the screen. Doesn't clear globals to allow for 
	# continued calculation
	second_number = int_or_float()
	calc_screen.delete(0, 'end')
	try: 
		if first_number == '':
			calc_screen.insert(0, str(second_number))
		if sign == '+':
			calc_screen.insert(0, str(first_number + second_number))
		elif sign == '-':
			calc_screen.insert(0, str(first_number - second_number))
		elif sign == '*':
			calc_screen.insert(0, str(first_number * second_number))
		elif sign == '/':
			calc_screen.insert(0, str(first_number / second_number))
	# If there are no store first number, function just reprints what was on 
	# the calculator screen.
	except (NameError, TypeError):
		calc_screen.insert(0, str(second_number))

def add_function():
	# stores the first number on the screen in a global var
	# and establises a global sign var 
	global first_number
	first_number = int_or_float()
	global sign
	sign = '+'
	calc_screen.delete(0, 'end')

def minus_function(): 
	# stores the first number on the screen in a global var
	# and establises a global sign var 	
	global first_number
	first_number = int_or_float()
	global sign
	sign = '-'
	calc_screen.delete(0, 'end')

def multiply_function():
	# stores the first number on the screen in a global var	
	# and establises a global sign var 	
	global first_number
	first_number = int_or_float()
	global sign
	sign = '*'
	calc_screen.delete(0, 'end')

def divide_function():
	# stores the first number on the screen in a global var	
	# and establises a global sign var 		
	global first_number
	first_number = int_or_float()
	global sign
	sign = '/'
	calc_screen.delete(0, 'end')

# Establish all of the buttons on a grid
# Buttons established from left column to right
# Col = 0
sign_change = tk.Button(calculator, text='+/-', width=6, height=3, command=swap_sign).grid(row=6, column=0)
one = tk.Button(calculator, text='1', width=6, height=3, command=lambda: button_click(1)).grid(row=5, column=0)
four = tk.Button(calculator, text='4', width=6, height=3, command=lambda: button_click(4)).grid(row=4, column=0)
seven = tk.Button(calculator, text="7", width=6, height=3, command=lambda: button_click(7)).grid(row=3, column=0)
reciprocal = tk.Button(calculator, text="1/x", width=6, height=3, command=reciprocal_fun).grid(row=2, column=0)
percent = tk.Button(calculator, text="%", width=6, height=3, command=percent_function).grid(row=1, column=0)

# Col = 1
zero = tk.Button(calculator, text="0", width=6, height=3, command=lambda: button_click(0)).grid(row=6, column=1)
two = tk.Button(calculator, text="2", width=6, height=3, command=lambda: button_click(2)).grid(row=5, column=1)
five = tk.Button(calculator, text="5", width=6, height=3, command=lambda: button_click(5)).grid(row=4, column=1)
eight = tk.Button(calculator, text="8", width=6, height=3, command=lambda: button_click(8)).grid(row=3, column=1)
square = tk.Button(calculator, text="x^2", width=6, height=3, command=square_number).grid(row=2, column=1)
ce = tk.Button(calculator, text="CE", width=6, height=3, command=clear_entry).grid(row=1, column=1)

# Col = 2
decimal = tk.Button(calculator, text=".", width=6, height=3, command=lambda: button_click('.')).grid(row=6, column=2)
three = tk.Button(calculator, text="3", width=6, height=3, command=lambda: button_click(3)).grid(row=5, column=2)
six = tk.Button(calculator, text="6", width=6, height=3, command=lambda: button_click(6)).grid(row=4, column=2)
nine = tk.Button(calculator, text="9", width=6, height=3, command=lambda: button_click(9)).grid(row=3, column=2)
square_root = tk.Button(calculator, text="x^.5", width=6, height=3, command=square_root_num).grid(row=2, column=2)
c = tk.Button(calculator, text="C", width=6, height=3, command=clear_globals).grid(row=1, column=2)

# Col = 3
equal = tk.Button(calculator, text="=", width=6, height=3, command=equals_function).grid(row=6, column=3)
plus = tk.Button(calculator, text="+", width=6, height=3, command=add_function).grid(row=5, column=3)
minus = tk.Button(calculator, text="-", width=6, height=3, command=minus_function).grid(row=4, column=3)
multiply = tk.Button(calculator, text="x", width=6, height=3, command=multiply_function).grid(row=3, column=3)
divide = tk.Button(calculator, text="÷", width=6, height=3, command=divide_function).grid(row=2, column=3)
backspace = tk.Button(calculator, text="←", width=6, height=3, command=backspace_function).grid(row=1, column=3)

# Start the GUI loop
calculator.mainloop()
