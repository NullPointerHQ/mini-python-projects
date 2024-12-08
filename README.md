# Collection of Mini Python Projects 
![Figure 0: Cover Image](https://realpython.com/cdn-cgi/image/width=960,format=auto/https://files.realpython.com/media/Newbie_Watermarked.a9319218252a.jpg)

⚖️ _Image Credits: Real Python. (n.d.). Are You Learning Python, But You’re Not Sure Where to Start and_ 
_What the “Roadmap” Looks Like? Real Python. Retrieved December 7, 2024, [Link](https://realpython.com/python-basics/)_

## 🔖Table of Contents
1. [Introduction](https://github.com/NullPointerHQ/mini-python-projects#introductory)
    - [Project Objectives](https://github.com/NullPointerHQ/mini-python-projects?tab=readme-ov-file#project-objectives)
    - [Universal Prerequisites](https://github.com/NullPointerHQ/mini-python-projects?tab=readme-ov-file#universal-prerequisites)
 2. [isPrime](https://github.com/NullPointerHQ/mini-python-projects?tab=readme-ov-file#-isprime)
    -  [Overview](https://github.com/NullPointerHQ/mini-python-projects?tab=readme-ov-file#overview)
    - [Prerequisites](https://github.com/NullPointerHQ/mini-python-projects?tab=readme-ov-file#prerequisites)
    - [Configuration and Usage](https://github.com/NullPointerHQ/mini-python-projects?tab=readme-ov-file#configuration-and-usage)
    - [Configurable Options](https://github.com/NullPointerHQ/mini-python-projects?tab=readme-ov-file#configurable-options)
    - [Usage](https://github.com/NullPointerHQ/mini-python-projects?tab=readme-ov-file#usage)
3. [Temperature Converter](https://github.com/NullPointerHQ/mini-python-projects?tab=readme-ov-file#temperature-converter) 
    - [Overview](https://github.com/NullPointerHQ/mini-python-projects?tab=readme-ov-file#overview-1)
    - [Prerequisites](https://github.com/NullPointerHQ/mini-python-projects?tab=readme-ov-file#prerequisites-1)
    - [Configuration and Usage](https://github.com/NullPointerHQ/mini-python-projects?tab=readme-ov-file#configuration-and-usage-1)
    - [Configurable Options](https://github.com/NullPointerHQ/mini-python-projects?tab=readme-ov-file#configurable-options-1)
    - [Usage](https://github.com/NullPointerHQ/mini-python-projects?tab=readme-ov-file#usage-1)

# 👋Introductory
### Project Objectives
These programs were made as I was studying the foundations of Python, having come from `C` and `C++` I wanted to study a more commonly used language with programs that I already understood on a theoretical level.
Thanks to these programs I was able to understand the syntaxes for variables, basic arithmetic, and so on. Each of thse programs also serve their own purpose listed below:
1. isPrime
    - Takes any number, and determines whether the number is prime.
2. Temperature Converter
     - Known as: PythonPractice1 in the repository
     - Converts any temperature provided to a different unit. (e.g Fahrenheit to Celsius, Celsius to Kelvin)
### Universal Prerequisites
- Language Used: Python Version 3.9
- IDE: [Microsoft's Visual Studio](https://visualstudio.microsoft.com/#vs-section)
  - These programs should be able to run in other IDEs.


# 🔢 isPrime
### Overview
[Convenient Source Code Link](isPrime/isPrime.py)

This program will prompt you for a number, determine whether it is prime or not, and ask if you would like to continue. The program will repeat until you would like it to stop. 

There are three conditions a number must meet to be considered prime
1. The number is greater than 2
```python
def is_two_or_less(number):
    #print("Received")
    if(number <= 2):#The number is 2 or less
        #print("Returning as TRUE")
        return True
    else:
        #print("Returning as FALSE")
        return False
```
2. The number is odd (i.e not divisible by two)
```python
def is_even (number):
    #Checks if the number given can easily be split by two
    if (number % 2 == 0):
        return True
    else:
        return False
```
3. The number is only divisible by 1 and itself
```python
def divisible (number):
    for i in range( 3 , int(( math.sqrt(n) + 1 ))):
        if (is_even(i) == False and n % i == 0):
            return True#Number is divisible by another number
    return False#Number is not divisible by another number
```

If all of the functions above return `FALSE`, then the number is prime.
### Prerequisites
1. The program requires the usage of the Python 'math' library
## Configuration and Usage
### Configurable Options
This program uses standard mathematical conventions for determining the prime status of a number, the program cannot be configured in any way.
### Usage
1. Run the program in your preferred IDE
2. Enter a **whole** number (e.g 7, 8, 9)
3. Enter Y to repeat or N to end the program
# 🌡Temperature Converter 
### Overview
[Convenient Source Code Link](PythonPractice1/PythonPractice1.py)

This program will take a `temperature` and `unit` and converts it to the other two units for temperatures (e.g Celsius and Kelvin if you provide a Fahrenheit temperature) when entering values be sure to seperate
the quantity from the unit via a space (e.g 100 F). The program will automatically seperate your input:
```python
degrees, unit = userInput.split()#Should Split the User's input into two values
```
and call the appropriate functions:
```python
#Handles Conversions
if(unit == 'K'):
    print(f"Converted to Fahrenheit: {kelvinTofarenheit(degrees):.4f},\nConverted to Celsius: {kelvinTocelsius(degrees):.4f}")

if(unit == 'C'):
    print(f"Converted to Fahrenheit: {celsiusTofarenheit(degrees):.2f},\nConverted to Kelvin: {celsiusTokelvin(degrees):.2f}")
if(unit == 'F'):
    print(f"Converted to Celsius: {farenheitTocelsius(degrees):.2f}\nConverted to Kelvin: {farenheitTokelvin(degrees):.2f}")
```
The conversion functions do simple step-by-step arithmetic using standard conversion formulas, `fahrenheitTocelsius` as an example:
```python
def farenheitTocelsius (degrees):
    result = degrees - 32
    result = result * 5
    result = result / 9
    return result;
```
### Prerequisites
This program has no additional prerequisites
## Configuration and Usage
### Configurable Options
There are no options that can be configured pre-runtime
### Usage
1. Open your preferred IDE and run the program
2. Enter a temperature value and unit seperated by a space
3. Observe the results.
