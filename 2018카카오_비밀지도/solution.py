def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n) :
        #arr = (bin(arr1[i])[2:]).zfill(n) or (bin(arr2[i])[2:]).zfill(n)
        temp1 = (bin(arr1[i])[2:]).zfill(n)
        temp2 = (bin(arr2[i])[2:]).zfill(n)
        temp3 = ''
        for i in range (n) :
            if temp1[i] == '1' or temp2[i] == '1':
                temp3 += '#'
            else :
                temp3 += ' '

        answer.append(temp3)
        
    return answer
