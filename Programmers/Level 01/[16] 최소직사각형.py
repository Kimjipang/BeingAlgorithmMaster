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
  
  
  
