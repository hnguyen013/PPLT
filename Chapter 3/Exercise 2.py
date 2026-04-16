sum_odd = 0
sum_even = 0
n = int(input("Enter n: "))
for i in range (1,n+1):
    if (i%2 == 0):
        sum_even = sum_even + i
    else: 
        sum_odd = sum_odd + i
print(f"Sum odd: {sum_odd}")
print(f"Sum even: {sum_even}")