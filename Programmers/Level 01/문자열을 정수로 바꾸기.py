def solution(s):
    result = 0
    neg = 0;
    if s[0] == '-':
        neg = 1
    for i in range(neg, len(s)):
        result = result * 10 + int(s[i])
    if neg == 1:
        return result * -1
    return result


==== 위와 같이 하면 테스트 코드는 통과하는데 제출 시 런타임 에러가 난다. 어떤 이유에서 잘못된지 찾는 중 ====


def solution(s):
    return int(s)
  
==== Pythonic한 코드 ====
