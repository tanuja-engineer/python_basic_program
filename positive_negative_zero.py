def check(num):
    if (num>0):
        print("number is positive")
    elif(num<0):
        print("number is negative")
    else:
        print("number is zero")
num=int(input("Enter the number:"))
check(num)