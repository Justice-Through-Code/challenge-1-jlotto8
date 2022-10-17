def convert_100_to_celsius():
    # Convert a temperature of 100 degrees fahrenheit to celsius
    # Save this to a variable called celsius_100, and use print() to print out the value
    # Is the resulting temperature you get an integer or float?
    # Print 'float' if it is a float or 'int' if it is an int
    # How do you know? Write a comment below your code explaining how you know which it is
    celsius_100 = (100 - 32) * 5/9
    print(celsius_100)
    print("float")
# It is a float because the solution is not a whole number

def convert_0_to_celsius():
    # Convert a temperature of 0 degrees fahrenheit to celsius
    # Save this to a variable called celsius_0, and use print() to print out the value
    celsius_0 = (0 - 32) * 5/9
    print(celsius_0)

def convert_34_2_to_celsius():
# #     # Convert a temperature of 34.2 degrees fahrenheit to celsius
# #     # Do this one all in one print statement without saving any variables
    print((34.2 - 32) * 5/9)
# '''
# Now, can you convert back?
# '''

def convert_5_to_fahrenheit():
#     # Convert a temperature of 5 degrees celsius to fahrenheit and print it out
    convert_5_to_farenheit = ((5 * 9/5) + 32)
    print(convert_5_to_farenheit)

def hotter_temp():
#     # What is hotter, a temperature of 30.2 degrees celsius, or a temperature of 85.1 degrees fahrenheit?
#     # Print out the hotter temp: '30.2 degrees celsius' or '85.1 degrees fahrenheit', respectively
    print('30.2 degrees celsius')

def convert_num_to_celcius(x):
    x =  int(input('Enter a number'))
    convert_num_to_celcius = (x - 32) * 5/9
    print(convert_num_to_celcius)
convert_num_to_celcius(5)

def convert_num_to_fahrenheit(x):
    x = int(input('Enter a number'))
    convert_num_to_fahrenheit = ((x * 9/5) + 32)
    print(convert_num_to_fahrenheit)
convert_num_to_fahrenheit(5)