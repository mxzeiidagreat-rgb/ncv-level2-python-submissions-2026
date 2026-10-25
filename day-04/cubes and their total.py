#num = int(input("Enter number "))
#cube = num ** (3)
#print (cube)

total = 0
n = int(input("Enter number "))
for x in range(1, n+1):
    cube = x**3
    print(cube, end = ",")
    total = total + cube