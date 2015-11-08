#not an empty file anymore
def f(A):
    i = 0
    j = 0
    while i < len(A):
        if A[i] == 0:
            A[i], A[j] = A[j], A[i] #swap elements
            for x in range (0, len(A)):
                print(A[x], endl=" ")
            j += 1
        i += 1
    return j >= 1
    
