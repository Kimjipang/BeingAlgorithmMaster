🧑‍💻 프로그래머스의 [삼총사] 문제이다. 주어진 리스트(number)에는 학생들의 정수 번호가 담겨 있다. 그 중 3개의 번호를 더했을 때 0이 되는 경우의 수를 구하면 된다.



```python
from itertools import combinations
def solution(number):
    answer = 0
    
    for num in combinations(number, 3):
        if sum(num) == 0:
            answer += 1
    return answer
```



***📝 풀이법***

1. 우선 리스트에 있는 요소들 중 모든 경우의 수를 따져보아야 하기 때문에 조합 공식을 사용해야 했다. 찾아보니 파이썬에는 combinations라는 라이브러리를 지원하고 있어 해당 라이브러리를 활용하는 방식으로 풀이를 했다.
2. combinations 라이브러리를 활용해 number를 3개씩 조합한다. 그 후, num의 합(sum)이 0일 때 answer += 1을 해준다.

