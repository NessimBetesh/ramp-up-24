def oddeven(i):
    i = int(i)
    if i % 2 == 0:
       print("Even")
    elif i % 2 != 0:
        print("Odd")
    else:
        print("Error")

oddeven(input("Put a number \n"))