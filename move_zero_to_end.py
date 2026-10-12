def move_zero(number):
    result=[]
    zero_count=0
    for num in number:
        if(num==0):
            zero_count+=1
        else:
           result .append(num)
    for i in range(zero_count):
        result.append(0)
    return result
number=[0,1,0,3,12,0,5]
final=move_zero(number)
print(final)
