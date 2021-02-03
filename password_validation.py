
#   ___________________________________________
#
#   BY:- heisdanieldade | www.heisdanielade.com
#   ___________________________________________
"""This is a password creation program in which the user will
    be asked if he wants to create a password by himself or
    the system should generate a secure password which will
    include symbol(s), letters, number(s) and will start with
    a letter.
    Packages used in this program are :
    1. Re
    2. Random
    3. Datetime
"""
import re
import random
import datetime

def spaces():
    print('  ')
    print('  ')
print('  ')


print("                                  CREATE PASSWORD")
spaces()
print("+ Do you want a secure password to be generated for you?")
print('   ')

# generate secure password
symbols = "@+&?#$&!£?%@$%"
numbers = "36!150427594708"
numbers2 = "83684+054270159"
lower = "adcjklm@nopzqrsefghibtuvwxy"
lower2 = "ijklc$dhopegfqwxrabvsztumny"
upper = "CFWNGHIJTUZVKLMOP#BQRDYEASX"
upper2 = "UHIL£MVWXBNOPCDEFGQRSTAJKYZ"
length = 11
length2 = 1

first_char1 = upper2 + lower
first_char2 = lower2 + upper
all1 = lower + symbols + upper + numbers
all2 = upper2 + lower2 + symbols + numbers2
gen_pass = "".join(random.sample(all1, length))
gen_2pass = "".join(random.sample(all2, length))
char_pass1 = "".join(random.sample(first_char1, length2))
char_pass2 = "".join(random.sample(first_char2, length2))

# use re module with Regex, make my own character set and pass
# this as argument in compile method
regex_symbol = re.compile('[@+#£%$!%&?]')
regex_number = re.compile('[0-9]')
regex_upper_letter = re.compile("[A-Z]")
regex_lower_letter = re.compile("[a-z]")
print('  ')
timestamp = datetime.datetime.now()   # timestamp


class Password:   # password validation
    def main_validation(self):
        if len(enter_pass) < 8:
            print("     (i) Password is less than 8 characters")
            print('  ')
        elif (regex_number.search(enter_pass) == None):
            print("     (i) Password must have number")
            print('  ')
        elif (regex_symbol.search(enter_pass) == None):
            print("     (i) Password must have symbol")
            print('  ')
        elif (regex_upper_letter.search(enter_pass) == None):
            print("     (i) Password must have Uppercase letter")
            print('  ')
        elif (regex_lower_letter.search(enter_pass) == None):
            print("     (i) Password must have Lowercase letter")
            print('  ')
        elif (enter_pass != con_pass):
            print("     (i) Passwords do not match")
            print('  ')
        else:
            print(f"     (i) Password Created Successfully at {timestamp}")
            print("  ")


start = True
# get user input whether to generate password, collect password or quit program
print('   ')
while start == True:
    print('+---------------------------------------------------------+')
    print("+ Y for YES  |  A for YES(New)  |  N for NO  |  X to QUIT +")
    print('+---------------------------------------------------------+')
    print('  ')
    reply = input("> ").lower()
    if reply == "y":
        print('  ')
        print(f"     (i) Secure Password:  {char_pass1}{gen_pass} created at {timestamp}")
        spaces()
    elif reply == "a":
        print('  ')
        print(f"     (i) Secure Password:  {char_pass2}{gen_2pass} created at {timestamp}")
        spaces()
    elif reply == "n":
        print("  ")
        enter_pass = input("+ Enter Password:  ")
        spaces()
        con_pass = input("+ Confirm Password:  ")
        print("  ")
        Password.main_validation("validation")  # validate passwords
    elif reply == "x":
        print('  ')
        print("    (i) Program Terminated.")
        print('  ')
        quit()
    elif reply == "":
        print('  ')
        print("    (i) Command can not be empty")
        print('  ')
    else:
        print('  ')
        print("    (i) Invalid Command")
        print('  ')

spaces()