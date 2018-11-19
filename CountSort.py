def main():
    A = [2,5,3,0,2,3,0,3]
    B = [None,0,0,0,0,0,0,0,0]
    print('A lista é A:'+str(A))
    countsort(A,B)
    print('\nOrdenada fica B:'+str(B))

def countsort(A,B):
    c=[]
    for i in range(max(A)+1):
        c.append(0)
    for x in range(len(A)):
        z = A.count(A[x])
        c[A[x]] = z
    for i in range(len(c)):
        if i is not 0:
            c[i] = c[i]+c[i-1]
    for x in range(len(A)):
        B[c[A[x]]] = A[x]
        c[A[x]] = c[A[x]]-1
    return B

if __name__ == "__main__":
    main()