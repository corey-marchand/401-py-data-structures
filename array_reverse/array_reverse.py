numbers = [0, 1, 2, 3, 4, 5, 6]
 
def reverseArray(array):
    L = len(numbers)

    for i in range(int(L/2)):
        n = numbers[i]
        numbers[i] = numbers[L-i-1]
        numbers[L-i-1] = n

    print(numbers)

reverseArray(numbers)