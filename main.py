print("Program starting.\n\nCheck multiplicative persistence.")
num = input("Insert an integer: ")
steps=0
while len(num) > 1:
    result = 1
    for digit in num:
        result = result * int(digit)
    print(" * ".join(num), "=", result)
    num = str(result)
    steps = steps + 1
print(f"\nNo more steps.\nThis program took {steps} steps\nProgram ending.") 