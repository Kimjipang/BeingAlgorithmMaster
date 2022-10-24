def solution(s):
    answer = True
    
    countP = s.count('p') + s.count('P')
    countY = s.count('y') + s.count('Y')
    
    if(countP != countY):
        return False
    
    return answer
