base = int(input("Enter you base: "))
power = int(input("Enter your power: "))

result = 1

for i in range(power):
    result = result * base

print("The result is:",result)