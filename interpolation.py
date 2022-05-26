def f(x1,y1,x2,y2,point):
    return(((y1-y2)/(x1-x2))*point)+((y2*x1-y1*x2)/(x1-x2))


def linear(table,point):
    i=0
    while table[i][0]<=point:
        i+=1
    i=i-1
    if i==len(table)-1 or i==0:
        print("The point is outside bounds")
    elif i==point:
        print(table[i][0],table[i][1])
    else:
        p=round(f(table[i][0],table[i][1],table[i+1][0],table[i+1][1],point),6)
        print("the point is",p)



def polynom(table,point):
    if len(table)<3:
        print("cant calculate")






def transposeMatrix(m):
    a= list(map(list,zip(*m)))
    return a

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors



mat3=[[1,1,1],[1,2,4],[1,3,9]]
print(getMatrixInverse(mat3))


































arr=[[0,0],[1,0.8415],[2,0.9093],[3,0.1411],[4,-0.7568],[5,-0.9585],[6,-0.2794]]
point=2.5
linear(arr,point)
