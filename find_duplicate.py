def duplicates(number):
    for i in range(len(number)):
        for j in range(i+1,len(number)):
          if number[i] ==number[j]:
            return True
        return False
number=[10,20,30,10,40,10,]
result=duplicates(number)
if result:
    print("duplicates")
else:
    print("no duplicates")
    