# A function is a collection of individual instructions
# Getting information back from a function through
# return functions.

def cube(num):
    return num*num*num # "return" tells python to deliver a result
    # 'return' breaks us out of the function. It's the last line.

result = cube(4) # Stores the returned value for later use
print(cube(4))
