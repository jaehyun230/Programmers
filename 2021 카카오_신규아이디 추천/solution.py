import re

def solution(new_id):

    #대문자 소문자로 변경
    new_id = new_id.lower()
    #숫자 알파벳을 - _ . 제외하고 모두 제거
    new_id = re.sub('[^0-9a-z-_.]', '', new_id)
    #연속된 .을 1개로 치환
    new_id = re.sub('(([.])\\2{1,})', '.', new_id) # 연속된 같은 문자 변환 (2개이상)
    #마침표가 처음이나 끝에 위치할 경우 제거
    new_id  = new_id.strip('.')
    #빈 문자열 일경우
    if len(new_id) == 0 :
        new_id = "a"
    #16자 이상일 경우 15자까지 제거
    if len(new_id) > 15 :
        new_id = new_id[:15]
    #끝에 마침표 문자일경우 제거
    new_id  = new_id.rstrip('.')
    #문자열 길이가 2자 이하 일 경우 마지막 문자를 길이가 3이 될때까지 추가
    while len(new_id) <= 2 :
        new_id += new_id[-1]
    
    return new_id
