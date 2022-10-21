def solution(arr):
        
    answer = 0
    for i in arr:
        answer += i
    
    return answer / len(arr)
  
  
================== 새로 알게된 것 ===================
파이썬에서는 for문 없이 배열의 모든 요소를 더해주는 sum 함수가 있다. 
아래의 코드는 이를 반영한 코드.



def solution(arr):
    
    return sum(arr) / len(arr)
