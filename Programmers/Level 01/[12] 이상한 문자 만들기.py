def solution(s):
    answer = list(s)
    count = 0
    for i in range(0, len(s)):
        if(s[i] == ' '):
            count = 0
            continue
        if(count % 2 == 0):
            answer[i] = s[i].upper()
            count += 1
        else:
            answer[i] = s[i].lower()
            count += 1
    return "".join(answer)
