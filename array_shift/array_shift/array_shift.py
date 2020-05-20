# aa = [3,4,5,6,7,4]

def array_shift(array, val):
    new_number = int(val)
    A = array 
    B = A[:len(A)//2]
    C = A[len(A)//2:]

    B.append(new_number)

    B.append(C) 

    print(B)


# print(array_shift(aa, 4))
