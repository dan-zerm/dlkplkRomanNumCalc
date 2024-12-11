import translations

def main():
    userNumber = input("Roman numeral calculaton\nThis program supports addition, subtraction, multiplication, and division\nEnter a calculation in the form: 'number operator number'\nEnter calculation: ").strip()

    splitInput = userNumber.split()
    if len(splitInput) != 3:
        print("Invalid input! Please enter a calculation in the form: 'number operator number'")
        return
    
    romanA = splitInput[0].upper()
    operator = splitInput[1]
    romanB = splitInput[2].upper()

    if operator not in ['+', '-', '*', '/']:
        print("Invalid operator! Please use +, -, *, /")
        return

    translations.calculate(romanA, operator, romanB)

main()



