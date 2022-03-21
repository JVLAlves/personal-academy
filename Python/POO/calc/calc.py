
array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sArray = []
i = 0
for a in array:
    print(i)
    index = array.index(a)
    if index != len(array)-1:
        sum = a + array[(index+1)]
        sArray.append(sum)
    else:
        continue
    i+= 1
print(sArray)


def IsOperator(op):
    OpList = ["+", "-", "/", "*", "%"]
    for oper in OpList:
        if op == oper
            return True
    return False
