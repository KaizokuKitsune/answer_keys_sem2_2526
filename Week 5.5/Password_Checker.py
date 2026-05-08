# Alex W.
# Period: 6 & 7
# Week 5.5 - Password Checker
# Time: 30 minutes.

from time import sleep # for dramatic effect
 
# initialization block
upper_case = 0
special_char = 0
nums = 0
min_len = 0
max_len = 0

uc_count = 0
sc_count = 0
num_count = 0


"🗹☐🗵" #special characters for later


print('Welcome to the Password Checker') # welcome text

# input validaiton
while True:
    try:
        upper_case = int(input('Enter the number of upper case letters required: '))
        special_char = int(input('Enter the number of special characters required: '))
        nums = int(input('Enter the number of numbers required: '))
        min_len = int(input('Enter the minimum number of characters: '))
        max_len = int(input('Enter the maximum number of characters: '))
        if sum([upper_case,special_char,nums]) > max_len: # makes sure it is possible
            print('Complexity requirements exceed character limit. Try Again.')
            continue
        if min_len >= max_len: # makes sure its possible
            print('Max length less than or equal to minimum length. Try Again.')
            continue
    except:
        print('An error has occured. Restarting...')
        continue
    else:
        break

# show user what they entered
print(f'''
Upper Case: {upper_case}
Spechial Chars: {special_char}
Numbers: {nums} 
Length: {min_len}-{max_len}     
''')

# get input
password = input('Enter your trial password: ')

# do checks
for letter in password:
    if letter.isupper():
        uc_count +=1
    elif letter.isdigit():
        num_count +=1
    elif letter.islower():
        continue
    elif letter.isspace():
        continue
    else:
        sc_count +=1

# booleans
uc_check = uc_count >= upper_case
sc_check = sc_count >= special_char
num_check = num_count >= nums
len_check = len(password) >= min_len and len(password) <= max_len
# is it valid
print('Checking...')
sleep(0.5) # adds punch
if uc_check:print('Upper Case: 🗹')
else:print('Upper Case: 🗵')
sleep(0.5)
if sc_check:print('Special Char: 🗹')
else:print('Special Char: 🗵')
sleep(0.5)
if num_check:print('Numbers: 🗹')
else:print('Numbers: 🗵')
sleep(0.5)
if len_check:print('Length: 🗹')
else:print('Length: 🗵')


if uc_check and sc_check and num_check and len_check:
    print("Good Job, Password saved.")
    with open("Week 5.5/passwords.txt","a") as outfile:
        outfile.write(f'{upper_case}|{special_char}|{nums}|{min_len}|{max_len}|{password}') # not a record but im lazy and it was EC
else: print('Attempt Failed. Try Again.')