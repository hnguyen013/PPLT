amount = 0
n = int(input("Enter the number of kilometers: "))
if (n == 1):
    amount = 15000
elif (n < 21):
    amount = 15000 + (n-1) * 12000
else: 
    amount = 15000 + 19*12000 + 10000 * (n-20)
print(f"The total amount is {amount} VND")