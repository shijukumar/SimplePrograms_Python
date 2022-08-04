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


#To print the prime numbers between given values
start = int(input('Enter the starting number: '))
stop = int(input("Enter the ending number: "))

prime = []
for n in range (start, stop):
    factors = []
    for i in range(1, n+1):
        rem = n%i
        if rem == 0:
            factors.append(i)
    if len(factors) == 2:
        prime.append(n)
                
print(prime)


#Check for prime numbers and list the factors using function

def is_prime(n):
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

#calling the function

is_prime(7)

for x in range(41240,41260):
    is_prime(x)
