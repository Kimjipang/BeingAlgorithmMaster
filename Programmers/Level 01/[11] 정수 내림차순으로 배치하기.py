def solution(n):
    answer = 0
    li = list(map(int, str(n)))
    li.sort(reverse = True)
    for i in li:
        answer = answer * 10 + i
    return answer
