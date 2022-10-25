def add(*data):
    sum=0
    data=list(data)
    data[0]=0
    for i in data:
        sum+=i
    return sum

print(add(1,2,3,4))
