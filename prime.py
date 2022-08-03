#program to check if a number is prime

n = int(input('Enter the number: '))
#1 is neither prime nor composite
if n == 1:
    print( "1 is Neither prime nor composite")
factors = []
for i in range(1, n+1):
    rem = n%i
    if rem == 0:
        factors.append(rem)
if len(factors) == 2:
    print(f"{n} is prime")
elif len(factors) > 2:
    print(f"{n} is composite")
    
