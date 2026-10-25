mark = int(input("Enter a mark "))

if mark >= 0 and mark <= 100:
    if mark >= 75:
        print ("Passed with Distinction")
    
    if mark < 50:
        print ("Failed")
    else:
        print ("Passed")
       