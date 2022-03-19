def solution(rows, columns, queries):
    answer = []
    array = []
    
    for i in range (rows) :
        add_arr = []
        for j in range (columns) :
            add_arr.append(i*(columns)+j+1)
        array.append(add_arr)
    
    
    for x1,y1,x2,y2 in queries:
        tmp = array[x1-1][y1-1]
        minimum = tmp

        #왼쪽 세로
        for k in range(x1-1,x2-1):
            temp = array[k+1][y1-1]
            array[k][y1-1] = temp
            minimum = min(minimum, temp)
        
        #아래 가로
        for k in range(y1-1,y2-1):
            temp = array[x2-1][k+1]
            array[x2-1][k] = temp
            minimum = min(minimum, temp)

        #오른쪽 세로
        for k in range(x2-1,x1-1,-1):
            temp = array[k-1][y2-1]
            array[k][y2-1] = temp
            minimum = min(minimum, temp)

        #위쪽 가로
        for k in range(y2-1,y1-1,-1):
            temp = array[x1-1][k-1]
            array[x1-1][k] = temp
            minimum = min(minimum, temp)
        
        array[x1-1][y1] = tmp
        answer.append(minimum)

    return answer
