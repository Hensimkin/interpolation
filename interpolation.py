from random import choice


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
    else:

        mat=[[1],[1],[1]]
        vec=[[],[],[]]
        a=choice(table)
        if a==table[len(table)-2] or a==table[len(table)-1]:
            a=table[len(table)-3]
        mat[0].append(a[0])
        mat[0].append(a[0]**2)
        vec[0].append(a[1])
        b=a
        while b==a or (b[0]<a[0]):
            b=choice(table)
        if b==table[len(table)-1]:
            b=table[len(table)-2]
        mat[1].append(b[0])
        mat[1].append(b[0] ** 2)
        vec[1].append(b[1])
        c=a
        while (c==a or c==b) or c[0]<b[0]:
            c=choice(table)
        mat[2].append(c[0])
        mat[2].append(c[0] ** 2)
        vec[2].append(c[1])
        """""
        mat=[[1,1,1],[1,2,4],[1,3,9]]
        vec=[[0.8415],[0.9093],[0.1411]]
        mat=getMatrixInverse(mat)
        
        mat = [[1, 2, 4], [1, 3, 9], [1, 4, 16]]
        vec = [[0.9093], [0.1411],[-0.7568]]
        """""
        mat=getMatrixInverse(mat)
        g=mult(mat,vec)
        sum=g[0][0]+(g[1][0]*point)+(g[2][0]*(point**2))
        print(sum)




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
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]
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

def mult(matrix1,matrix2):
    res=[[0 for x in range(len(matrix2[0]))] for y in range(len(matrix1))]
    size=len(matrix1)
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                res[i][j] += matrix1[i][k] * matrix2[k][j]
    return res


def multiply(v, G):
    result = []
    for i in range(len(G[0])):
        total = 0
        for j in range(len(v)):
            total += v[j] * G[j][i]
        result.append(total)
    return result




mat3=[[1,1,1],[1,2,4],[1,3,9]]
arr=[[0,0],[1,0.8415],[2,0.9093],[3,0.1411],[4,-0.7568],[5,-0.9585],[6,-0.2794]]
point=2.5
#linear(arr,point)
polynom(arr,point)
