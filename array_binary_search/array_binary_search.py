__version__ = '0.1.0'

# test_array = [4,2,3,1,5,6]

def BinarySearch(array, key):
    a = array
    try: 
        b = a.index(key)
        print(b)
    except ValueError:
        print(-1)
   

# BinarySearch(test_array, 4)