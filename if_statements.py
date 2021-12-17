# Making decisions in python > if true then... if false then...

# basic statement
is_male = False
is_tall = False

if is_male and is_tall: # or means at least one must be true
    # and means both must be true
    print('You are a tall male.')
elif is_male and not(is_tall):
    print('You are a short male.')
elif not(is_male) and is_tall:
    print('You are not a male but are tall.')
else:
    print('You are neither male or tall.')

# elif is a way to add many more possible outcomes to an if~else statements
