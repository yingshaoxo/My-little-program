def get_number(base_number):
    A = 10*base_number+1

    additional_number = int(base_number/5)
    if (additional_number != 0):
        for i in range(0, additional_number-1):
            A+=i*5
        A+=base_number%5

    B = A+10
    B+=additional_number
    
    return list(range(A, B)), B-A, additional_number


for i in range(4, 21):
    print(get_number(i))

