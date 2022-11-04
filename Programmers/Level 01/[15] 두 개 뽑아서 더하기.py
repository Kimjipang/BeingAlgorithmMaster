def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            num = numbers[i] + numbers[j]
            if num in answer:
                continue
            else:
                answer.append(num)
    answer.sort()
    return answer
  
  
  
  
  ======= 나의 풀이는 리스트 answer에 없는 수를 저장하는 것이었는데 파이썬의 set(집합)의 중복된 수를 가지지 않는다는 점을 이용하여 해결할 수 있다. =======
                                  -> 일단 다 저장하고 set() 메서드를 이용하여 중복된 수를 거르는 것이다.
  
def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])

    return sorted(set(answer))
