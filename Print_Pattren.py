
#user = int(input("Input number of rows: "))
#rows = 0
#while rows < user:
#    num  = rows+ 1
#    while num>0:
#        print("5", end="")
#        num = num - 1
#    rows = rows+1
#    print()


num = int(input("Enter number of rows: "))
row = 0
while row<num:
    p = row + 1
    while p>0:
        print("*", end=" ")
        p = p-1
    row = row + 1
    print()