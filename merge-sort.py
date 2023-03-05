# Input: Array A
# Output: Sortiertes Array A
def mergesort(A):
    
    if len(A) <= 1:
        return A 
    
    h = int((len(A)/2))
    L = mergesort(A[:h])
    R = mergesort(A[h:])
    
    return merge(L, R)

def merge(A, B):
    S = []

    while len(A) > 0 and len(B) > 0:
        if A[0] > B[0]:
            S.append(B[0])
            B.pop(0)
        else:
            S.append(A[0])
            A.pop(0)
            
    while len(A) > 0:
        S.append(A[0])
        A.pop(0)
        
    while len(B) > 0:
        S.append(B[0])
        B.pop(0)

    return S
