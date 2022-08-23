#To find the twin primes from 2 to given number

def checkTwinPrime(number):
    factorcount = 0
    for m in range(1, number+1):
        if number % m == 0:
            factorcount = factorcount + 1
    
    if factorcount == 2:
        return True

num = int(input('Enter the ending number: '))
print('The twin primes from 2 to', num, 'are :')

for m in range(2, num):
    if (checkTwinPrime(m) == True and checkTwinPrime(m+2) == True):
        print('('+str(m)+','+str(m+2)+')', end='  ')
