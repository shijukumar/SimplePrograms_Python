#Program to find the sum of first n numbers

total = 0
n = int(input('enter the nth number : '))
for num in range (n+1):
    total = total + num 
print(total)

#sum of first n numbers using while

total = 0
n = int(input('enter the nth number : '))
while  n >=0:
    total = total + n 
    n -= 1
print(total)
