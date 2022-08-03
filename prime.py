#program to check if a number is prime

n = int(input('Enter the number: '))
#1 is neither prime nor composite
if n == 1:
    print( "1 is Neither prime nor composite")
factors = []
for i in range(1, n+1):
    rem = n%i
    if rem == 0:
        factors.append(i)
if len(factors) == 2:
    print(f"{n} is prime")
elif len(factors) > 2:
    print(f"{n} is composite")

    
#program to check if a number is prime and to find the factors

n = int(input('Enter the number: '))
#1 is neither prime nor composite
if n == 1:
    print( "1 is Neither prime nor composite")
factors = []
for i in range(1, n+1):
    rem = n%i
    if rem == 0:
        factors.append(i)
if len(factors) == 2:
    print(f"{n} is prime\n The factors are {factors}")
elif len(factors) > 2:
    print(f"{n} is composite\n The factors are {factors}")
