def solution(s):
    result = []
    s = s[2:-2]
    s = s.split('},{')
    s.sort(key = lambda x:len(x))
    for tuples in s :
        element = tuples.split(',')
        for num in element :
            if int(num) not in result :
                result.append(int(num))
    return result
