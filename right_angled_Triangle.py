def rightTrianglePattern(n):
    arr=[]
    for i in range(1,n+1):
        star=""

        for j in range(1,i+1):
            #print("*" ,end=" ")
            star+="*"
        arr.append(star)
    print(arr)

rightTrianglePattern(5)
