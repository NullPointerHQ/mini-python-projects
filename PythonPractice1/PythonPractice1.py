#Design a temperature converter
#Function Definitions Block

# Farenheit -> X functions
def farenheitTokelvin (degrees):
    result = degrees - 32
    result = result * 5
    result = result / 9
    result = result + 273.15
    return result;

def farenheitTocelsius (degrees):
    result = degrees - 32
    result = result * 5
    result = result / 9
    return result;

# Celsius -> X Functions
def celsiusTokelvin (degrees):
    result = degrees + 273.15
    return result

def celsiusTofarenheit (degrees):
    result = degrees * 9
    result = result / 5
    result = result + 32
    return result

# Kelvin -> X Functions

def kelvinTocelsius (degrees):
    result = degrees - 273.15
    return result;

def kelvinTofarenheit (degrees):
    result = degrees - 273.15
    result = result * (9/5)
    result = result + 32    
    return result;

print("Hello user,", end=' ')
userInput = input("Please enter your temperature and unit seperated by a space: ")
degrees, unit = userInput.split()#Should Split the User's input into two values
print("")#New Line Thing
degrees = int(degrees)#Converts Degrees from a string variable to an integer variable - TYPE CASTING

#Handles Conversions
if(unit == 'K'):
    print(f"Converted to Fahrenheit: {kelvinTofarenheit(degrees):.4f},\nConverted to Celsius: {kelvinTocelsius(degrees):.4f}")

if(unit == 'C'):
    print(f"Converted to Fahrenheit: {celsiusTofarenheit(degrees):.2f},\nConverted to Kelvin: {celsiusTokelvin(degrees):.2f}")
if(unit == 'F'):
    print(f"Converted to Celsius: {farenheitTocelsius(degrees):.2f}\nConverted to Kelvin: {farenheitTokelvin(degrees):.2f}")