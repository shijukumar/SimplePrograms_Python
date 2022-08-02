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


#sum of first n numbers using function

def sumofN(n):
    total = 0
    for num in range (n+1):
        total = total + num
    print(f"Sum of Natural Numbers from 1 to {n} is  {total}")


#calling the function sumofN
sumofN(5)

#sum of n natural number using recursion

def sumofn_rec(num):
    if(num == 1):
        return num
    else:
        return (num + sumofn_rec(num - 1))
    
number = int(input("Please Enter any Number: "))

total_value = sumofn_rec(number)

print(f"Sum of Natural Numbers from 1 to {number} is  {total_value}")
