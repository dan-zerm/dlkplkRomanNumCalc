symbolValues = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
valueZero = 0

def intToRoman(num):
    values = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    translatedValue = ""
    for value, symbol in values:
        while num >= value: 
            translatedValue += symbol
            num -= value
    return translatedValue

def romanToInt(roman):
    total = 0
    prevValue = 0
    originalRoman = roman
    for character in roman:
        if character not in symbolValues:
            print("Invalid roman numeral. Please refer to this list of valid roman numerals: I, V, X, L, C, D, M")
            return -1
        value = symbolValues[character]
        if value > prevValue: 
            total += value - 2 * prevValue
        else:
            total += value
        prevValue = value
    
    reconvertedValue = intToRoman(total)
    if originalRoman != reconvertedValue: #check if the roman numeral is valid
        print("Invalid roman numeral entered. Please use the correct convention.")
        return -1
    return total

def calculate(romanA, operator, romanB):
    maxValueCheck = 3999  
    num1 = romanToInt(romanA)
    if num1 == -1:
       return
    num2 = romanToInt(romanB)
    if num2 == -1:
        return

    if operator == "+": #adding
        result = (num1+num2)
        if maxValueCheck > (result):
            print(f"{romanA} {operator} {romanB} = {intToRoman(result)}")
            return 
        else:
            print("Roman numeral exceeds maximum value of 3999.")
            return -1

    elif operator == "-": #subtracting
        result = (num1 - num2)
        if result <= valueZero:
            print("Result is not a valid roman numeral (negative or zero)")
        if result > 3999:
            print("Calculation exceeds max value of 3999.")       
            return -1     
        else:
            print(f"{romanA} {operator} {romanB} = {intToRoman(result)}")
        return
    
    elif operator == "*":
        result = (num1 * num2) #multiplying
        if result <= valueZero:
            print("Result is not a valid roman numeral (negative or zero)")
        if result > 3999:
            print("Calculation exceeds max value of 3999.")
            return -1
        else:
            print(f"{romanA} {operator} {romanB} = {intToRoman(result)}")
        return
    
    elif operator == '/': #dividing
        result = (num1 / num2)
        if num2 == valueZero: #prevent division by 0
            print("Cannot divide by zero")
        if result > 3999:
            print("Calculation exceeds max value of 3999.")
            return -1
        else:
            print(f"{romanA} {operator} {romanB} = {intToRoman(result)}")
        return
    else:
        ValueError("Invalid operator, use +,-,*,/")
        return -1