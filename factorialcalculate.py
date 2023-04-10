def faktorial(x):
    result = 1
    for i in range(1, x+1):
        result *= i
    return result

x = int(input("Enter a number: "))
print(faktorial(x))
