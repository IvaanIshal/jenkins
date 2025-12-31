import sys
 
if len(sys.argv) != 3:
    print("Usage: python3 test.py <number1> <number2>")
    sys.exit(1)
 
number1 = float(sys.argv[1])
number2 = float(sys.argv[2])
 
def add_numbers(num1, num2):
    return num1 + num2
 
result = add_numbers(number1, number2)
 
print(f"The sum of {number1} and {number2} is: {result}")

