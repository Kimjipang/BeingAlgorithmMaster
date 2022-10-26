======== 나의 풀이 ========

def solution(n):
    answer = 0
    for i in range(2, n):
        if(n % i == 1):
            answer = i 
            break
    return answer


======== 다른 풀이 ========

def solution(n):    
    
    return [i for i in range(2, n) if(n % i == 1)][0]

# 효율성 면에서는 위에가 나아보임! 아래는 무조건 for문을 다 돌려서 list를 만들기 때문에 시간복잡도가 같은 O(n)이긴 해도 다름.
