def solution(x):
    answer = True
    sum = 0
    for i in str(x):
        sum += int(i)
    
    if(x % sum != 0):
        return False
    return answer


# =============== map 함수 쓰는 거 기억해두자 =============== 
# x = 1234
# sum(list(map(int, str(x)))) // x = [1,2,3,4]
