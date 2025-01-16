# Quotes inside a string
print("He is called 'Sameer'")

# multi line string
a = """
Hi
Hello
Haha
"""
print(a)

# A string is an array
# since python does not have a char type, a single character is simply a
# string with length 1
test = 'sameer'
print(test[0])

# loop through string since it is an array
for i in test:
    print(i)

# length of string 
print(len(test))

# check if a string is present in a var
txt ='hi sameer'
print('hi' in txt) 

# slicing of string
slice= 'hello world'

print(slice[0:-2])