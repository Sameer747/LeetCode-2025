'''
ALL ABOUT GLOBAL VARIABLES
'''
x = 'awsome' # global var

def myFunc():
    print('Python is ' + x)

myFunc()

# global variable with local variable
z = 2 # global var

def myFunc2():
    z = 1 # local variable 
    print(z)

myFunc2()

print(z)

# To create a global variable inside the func
def myFunc3():
    global a
    a = 'game'

myFunc3()

print('Python is like a ' + a)

# Manipulate the value of global var inside the func
b = 'great'

def myFunc4():
    global b
    b = 'greatest'

myFunc4()

print('Python is '+b) 