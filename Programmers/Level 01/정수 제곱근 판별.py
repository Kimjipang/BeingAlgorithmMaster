def solution(n):
    
    answer = n ** (1/2)
    if(answer % 1 == 0):
        return (answer + 1) ** 2    
    return -1
