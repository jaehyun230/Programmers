def solution(s):
    answer = s
    while 'zero' in answer:
        answer = answer.replace('zero', '0')
    while 'one' in answer:
        answer = answer.replace('one', '1')
    while 'two' in answer:
        answer = answer.replace('two', '2')
    while 'three' in answer:
        answer = answer.replace('three', '3')
    while 'four' in answer:
        answer = answer.replace('four', '4')
    while 'five' in answer:
        answer = answer.replace('five', '5')
    while 'six' in answer:
        answer = answer.replace('six', '6')
    while 'seven' in answer:
        answer = answer.replace('seven', '7')
    while 'eight' in answer:
        answer = answer.replace('eight', '8')
    while 'nine' in answer:
        answer = answer.replace('nine', '9')
    
    answer = int(answer)

    return answer
