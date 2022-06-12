'''
for 문으로 확인하는 방법.
Hash로는 어떻게 풀 수 있을까?
'''
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return answer