def solution(sizes):
    answer = max1 = row1 = row2 = col1 = col2 = tmp = 0
    for i in range(len(sizes)):
        for j in range(len(sizes[i])):
            if max1 < sizes[i][j]:
                max1 = sizes[i][j]
                row1 = i
                col1 = j

    for i in range(len(sizes)):
        for j in range(len(sizes[i])):
            if sizes[i][j] > sizes[i][col1]:
                col2 = j
                tmp = sizes[i][col1]
                sizes[i][col1] = sizes[i][j]
                sizes[i][j] = tmp

    max2 = sizes[0][col2]
    for i in range(len(sizes)):
        if max2 < sizes[i][col2]:
            max2 = sizes[i][col2]
    answer = max1 * max2
    print(answer)                     
    return answer
  
  
#   ==========================================================
#   이렇게 하면 일단 시간 복잡도가 O(n^2)이 나와서 좋은 코드는 아님.
#   처음 풀었던 나의 풀이(위)와 다른 사람의 풀이(아래)는 결국에는 같은 행동을 하는 코드이지만 
#   아래의 풀이가 효율성도 좋고 굳이 생각하지 않아도 되는 것에 대해서는 빼버리고 작성한 코드라 더 좋은 거 같다. 
    
    
def solution(sizes):

    row = col = 0
    
    for i, j in sizes:
        if i < j:
            i, j = j, i
        row = max(row, i)
        col = max(col, j)
    return row * col
