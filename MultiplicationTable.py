#Print the multiplication Table

tableof = int(input('Enter the table to be printed: '))
for i in range(1, 11):
    print(tableof, "x", i, "=", tableof*i)


#Print the multiplication Table upto userdefined value

tableof = int(input('Enter the table to be printed: '))
maxval = int(input('Enter the maxValue of muliplier: '))
multiplier = 1
while(multiplier <= maxval):
    print(tableof, "x", multiplier, "=", tableof*multiplier)
    multiplier += 1
