number_list = [8,9,5,6,7,1,3,13,15,99,100,1000,2,17,4]

def ascending(number_list):
    for i in range(len(number_list)-1):
        if number_list[i] > number_list[i+1]:
            return False
    return True

def sorting():
    while ascending(number_list) == False:
        for j in range(len(number_list) - 1):
            if number_list[j] > number_list[j+1]:
                a = number_list[j]
                b = number_list[j+1]
                number_list[j] = b
                number_list[j+1] = a

sorting()
print number_list
