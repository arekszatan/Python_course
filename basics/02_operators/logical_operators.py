
# operatory logiczne

# and operators
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

print(10 >= 5 and 3 < 9) # True
print(12 < 20 and 5 > 10) # False
print(3 == 5 and 6 < 1) # False

task_completed = True
lines_of_code_written = 100

if task_completed == True and lines_of_code_written >= 50:
    print('Go home')

hour_of_day = 15
if task_completed == True and lines_of_code_written >= 60 and hour_of_day >= 15:
    print('Go home')

# or operator
print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False

print(10 >= 10 or 5 > 3) # True
print(5 <= 7 or 5 == 1) # True
print(2 != 2 or 5 == 5) # True
print(1 == 3 or 4 > 10) # False

if 10 > 5 or "Ania" != "Ola":
    print("True or True")

if 3 == 5 or "Ania" == "Ola":
    print("False or False")

# not operator
print(not True) # False
print(not False) # True

print(not(3 == 3)) # False
print(not(5 > 10)) # True
print(not(10 > 6 and "Ola" != "Ania")) # False

task_completed = False

if task_completed == True:
    print("Go home")

if not task_completed:
    print("Stay a bit longer and finish")
